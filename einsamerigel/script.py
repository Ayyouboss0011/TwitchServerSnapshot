import time
import subprocess
from run_docker_compose import run_docker_compose
from restart_browsers import get_browser_container_names, restart_browser_containers

# Docker-Befehl "docker stop" für alle laufenden Container
running_containers = subprocess.check_output(['docker', 'ps', '-q'], text=True).splitlines()
for container_id in running_containers:
    subprocess.run(['docker', 'stop', container_id])

# Docker-Befehl "docker rm" für alle Container
all_containers = subprocess.check_output(['docker', 'ps', '-aq'], text=True).splitlines()
for container_id in all_containers:
    subprocess.run(['docker', 'rm', container_id])

# Kurze Wartezeit (5 Sekunden), um sicherzustellen, dass die Container gelöscht wurden
time.sleep(5)

# Docker-Befehl "docker ps -a" zur Überprüfung
result = subprocess.run(['docker', 'ps', '-a'], stdout=subprocess.PIPE, text=True)

# Ausgabe anzeigen
print(result.stdout)

# Führe alle Docker Compose files aus
run_docker_compose()

time.sleep(60)

# Get browser container names,Restart browser containers sequentially
browser_container_names = get_browser_container_names()
restart_browser_containers(browser_container_names)

    
        

