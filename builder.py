"""Construye y despliega la aplicación en nuestro servidor live"""

import os
import spur
import requests
import time

# Constantes
LIVE_USER = os.environ['LIVE_USER']
LIVE_HOST = os.environ['LIVE_HOST']
LIVE_PASS = os.environ['LIVE_PASS']
APP_PATH = os.environ['APP_PATH']

STOP = ['systemctl', 'stop', 'gunicorn']
CHECKOUT = ['git', 'checkout', '.']
# PULL = ['git', 'pull', 'origin', 'master']
PULL = ['git', 'pull', 'origin', 'dev-branch']
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

def checkout():
    shell = spur.SshShell(hostname=LIVE_HOST, username=LIVE_USER, password=LIVE_PASS, missing_host_key=spur.ssh.MissingHostKey.accept)
    with shell:
        print('Sanando la carpeta del live server...')
        result = shell.run(CHECKOUT, cwd=APP_PATH)
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

def chequeo_sitio():
    print('Comprobando que el sitio ande...')
    url = 'http://108.161.135.53/admin/'
    time.sleep(3)
    req = requests.get(url) 
    if req.ok:
        print ('El sitio parece andar bien')
        return  0
    else:
        print('Por alguna razón, el sitio no anda')
        return 1

if __name__ == '__main__':
    stop()
    checkout()
    pull()
    start()
    chequeo_sitio()
    print('Despliegue del sitio en servidor live terminado')
    print('************************************************************')