import schedule
import time
import subprocess
import psutil
import threading

def start_cozylofi_docker():
    subprocess.run(['python3', 'script.py'])

def start_cozylofi_stream():
    t = threading.Thread(target=subprocess.run, args=(['python3', 'start_stream_cozylofi.py'],))
    t.start()

def stop_stream():
    def terminate_script_by_name(script_name):
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            if script_name in proc.info['cmdline']:
                print(f"Terminating {proc.info['name']} (PID: {proc.info['pid']})")
                proc.terminate()  # or proc.kill() for immediate termination

    subprocess.run(['pkill', '-f', 'ffmpeg'])
    subprocess.run(['pkill', '-f', 'docker'])
    terminate_script_by_name("script.py")

# Start Stream
schedule.every().day.at("04:27").do(start_cozylofi_stream)
schedule.every().day.at("04:27:05").do(start_cozylofi_docker)

# Stop Stream
schedule.every().day.at("09:00").do(stop_stream)

# Run the schedule
while True:
    schedule.run_pending()
    time.sleep(1)
