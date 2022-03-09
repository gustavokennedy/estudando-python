# -*- coding: utf-8 -*-
import os
import time

# Lendo arquivo
with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('Verificando o IP:', ip)
        print('-'*60)
        os.system('ping -n 2 {}'.format(ip))
        print('-'*60)
        print('IP', ip, 'verificado com sucesso!')
        time.sleep(10)