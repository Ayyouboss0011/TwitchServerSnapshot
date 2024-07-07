import schedule
import time
import subprocess
import psutil
import threading

def start_einsamerigel_docker():
    subprocess.run(['python3', 'script.py'])

def start_einsamerigel_stream():
    t = threading.Thread(target=subprocess.run, args=(['python3', 'start_stream_einsamerigel.py'],))
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

# Schedule the tasks
schedule.every().day.at("09:06").do(start_einsamerigel_docker)
schedule.every().day.at("09:06:05").do(start_einsamerigel_stream)

schedule.every().day.at("15:00").do(stop_stream)

# Run the schedule
while True:
    schedule.run_pending()
    time.sleep(1)
