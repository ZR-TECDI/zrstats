#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.conf import settings
"""Transforma un archivo RPT al formato que lee armastats.py."""


def leer_archivo(data):
    
    with open(settings.BASE_DIR+'\\asistencia\\ArmaStats\\'+data, 'r') as f:
        raw_data = f.readlines()



    
    for x in raw_data:
        if "OPC DATA" in x:
            original_line = x.split(" ")
            date = original_line[0]
            time = original_line[1]
            
            if len(original_line) == 6:
                name = str(original_line[4])+str(original_line[5])
                name = name.split(",")
            else:
                name = original_line[4].split(",")

            name = name[2]
            name = name.replace(" ", "")
            name = name.replace('"', '')

            linea = raw_data.index(x)
            wl = " "
            new_line = [date, time, '"ZRASISTENCIA: '+ name + ' conectado"\n']
            new_line = wl.join(new_line)
            raw_data.insert(linea+1, new_line)

        elif "OPD DATA" in x:
            original_line = x.split(" ")
            date = original_line[0]
            time = original_line[1]
            name = original_line[4].split(",")
            
            if len(original_line) == 6:
                name = str(original_line[4])+str(original_line[5])
                name = name.split(",")
            else:
                name = original_line[4].split(",")
            
            name = name[2]
            name = name.replace('"', '')

            linea = raw_data.index(x)
            wl = " "
            new_line = [date, time, '"ZRASISTENCIA: '+ name + ' desconectado"\n']
            new_line = wl.join(new_line)
            raw_data.insert(linea+1, new_line)            
    
    new_data = []
    for x in raw_data:
        new_data.append(str(x))

    with open("transformed.rpt", 'w') as f:
        f.writelines(new_data)

def main():
	"""Launcher."""
	# init the GUI or anything else
	leer_archivo("prueba.rpt")
 
if __name__ == "__main__":
	main()