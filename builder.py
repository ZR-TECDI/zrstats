"""Construye y despliega la aplicación en nuestro servidor live"""

import os
import spur

# Constantes
LIVE_USER = os.environ['LIVE_USER']
LIVE_HOST = os.environ['LIVE_HOST']
LIVE_PASS = os.environ['LIVE_PASS']
APP_PATH = os.environ['APP_PATH']

STOP = ['systemctl', 'stop', 'gunicorn']
PULL = ['git', 'pull', 'origin', 'master']
START = ['systemctl', 'start', 'gunicorn']

print('************************************************************')
print('Comenzando el despliegue del sitio en el servidor live: ')

def stop():
    shell = spur.SshShell(hostname=LIVE_HOST, username=LIVE_USER, password=LIVE_PASS, missing_host_key=spur.ssh.MissingHostKey.accept)
    with shell:
        print('Deteniendo el servicio gunicorn...')
        result = shell.run(STOP, cwd=APP_PATH)
        result = str(result.output)
        result = result.split('\n')

    for line in result:
        print(line)
    return 0

def pull():
    shell = spur.SshShell(hostname=LIVE_HOST, username=LIVE_USER, password=LIVE_PASS, missing_host_key=spur.ssh.MissingHostKey.accept)
    with shell:
        print('Pulleando últimos cambios desde master...')
        result = shell.run(PULL, cwd=APP_PATH)
        result = str(result.output)
        result = result.split('\n')

    for line in result:
        print(line)
    return 0

def start():
    print('Comenzando el servicio una vez más...')
    shell = spur.SshShell(hostname=LIVE_HOST, username=LIVE_USER, password=LIVE_PASS, missing_host_key=spur.ssh.MissingHostKey.accept)
    with shell:
        result = shell.run(START, cwd=APP_PATH)
        result = str(result.output)
        result = result.split('\n')

    for line in result:
        print(line)
    return 0  

if __name__ == '__main__':
    stop()
    pull()
    start()
    print('Despliegue del sitio en servidor live terminado')
    print('************************************************************')