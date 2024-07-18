from flask import Flask, jsonify
import os
import glob
import time

app = Flask(__name__)

def load_modules():
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')

def find_device_folder(base_dir):
    device_folders = glob.glob(base_dir + '28*')
    if device_folders:
        return device_folders[0]
    else:
        raise FileNotFoundError(f"No device folders found in directory: {base_dir}")

def read_temp_raw(device_file):
    with open(device_file, 'r') as f:
        lines = f.readlines()
    return lines

def read_temp(device_file):
    lines = read_temp_raw(device_file)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(device_file)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        return temp_c, temp_f, timestamp

@app.route('/temperature', methods=['GET'])
def temperature():
    try:
        load_modules()
        base_dir = '/sys/bus/w1/devices/'
        device_folder = find_device_folder(base_dir)
        device_file = device_folder + '/w1_slave'
        temp_c, temp_f, timestamp = read_temp(device_file)
        return jsonify({"temp_c": temp_c, "temp_f": temp_f, "timestamp": timestamp})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
