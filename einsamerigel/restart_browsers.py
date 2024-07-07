import subprocess
import time

def get_browser_container_names():
    try:
        # Get the names of all running containers with "b" prefix
        output = subprocess.check_output(['docker', 'ps', '--format', '{{.Names}}'], text=True).split()

        # Filter container names based on naming structure "b" + "number"
        browser_container_names = [name for name in output if name.startswith('b')]

        return browser_container_names

    except subprocess.CalledProcessError as e:
        print(f"Error listing Docker containers: {e}")
        return []


def restart_browser_containers(container_names):
    while True:
        for container_name in container_names:
            try:
                subprocess.run(['docker', 'restart', container_name], check=True)
                print(f"Container {container_name} restarted successfully")
                time.sleep(60)

            except subprocess.CalledProcessError as e:
                print(f"Error restarting container {container_name}: {e}")


# Get browser container names
#browser_container_names = get_browser_container_names()

# Restart browser containers sequentially
#estart_browser_containers(browser_container_names)
