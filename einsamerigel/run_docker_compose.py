import subprocess
import time
import os

def run_docker_compose():
    try:
        # Define the command
        command = ["docker-compose", "-f", os.path.expanduser("~/TP3/TP3-main/einsamerigel/docker-compose1.yml"), "up", "-d"]
        # Run the command
        subprocess.run(command, check=True)
        print("Docker Compose command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    time.sleep(10)

    try:
        # Define the command
        command = ["docker-compose", "-f", os.path.expanduser("~/TP3/TP3-main/einsamerigel/docker-compose2.yml"), "up", "-d"]
        # Run the command
        subprocess.run(command, check=True)
        print("Docker Compose command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    time.sleep(10)

    try:
        # Define the command
        command = ["docker-compose", "-f", os.path.expanduser("~/TP3/TP3-main/einsamerigel/docker-compose3.yml"), "up", "-d"]
        # Run the command
        subprocess.run(command, check=True)
        print("Docker Compose command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    time.sleep(10)

    try:
        # Define the command
        command = ["docker-compose", "-f", os.path.expanduser("~/TP3/TP3-main/einsamerigel/docker-compose4.yml"), "up", "-d"]
        # Run the command
        subprocess.run(command, check=True)
        print("Docker Compose command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    time.sleep(10)

    try:
        # Define the command
        command = ["docker-compose", "-f", os.path.expanduser("~/TP3/TP3-main/einsamerigel/docker-compose5.yml"), "up", "-d"]
        # Run the command
        subprocess.run(command, check=True)
        print("Docker Compose command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    time.sleep(10)

    try:
        # Define the command
        command = ["docker-compose", "-f", os.path.expanduser("~/TP3/TP3-main/einsamerigel/docker-compose6.yml"), "up", "-d"]
        # Run the command
        subprocess.run(command, check=True)
        print("Docker Compose command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


    ###########################################################################################################
    
    
    # Kurze Wartezeit (10 Sekunden), um sicherzustellen, dass die Container gestartet wurden
    time.sleep(10)
    
    # Lösche alle temporären Volume Dateien
    try:
        subprocess.run(['docker', 'system', 'prune', '-a', '--volumes'], check=True, input='y', text=True)
        print("Cleanup successful.")
    except subprocess.CalledProcessError as e:
        print(f"Error cleaning up: {e}")
