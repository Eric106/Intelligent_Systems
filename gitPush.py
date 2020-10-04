# -*- coding: utf-8 -*-
from os import system
from datetime import datetime
#run_data="java -Xmx4096M -Xms4096M -jar spigot-1.14.4.jar"
#run_data="RUN.bat"

def run_server():
    try:
        system("git pull origin master")
        #system(run_data)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        gitUpdate(dt_string)
    except Exception as e:
        print(e)
        exit()
def gitUpdate(dt_string):
    # system('git init')
    system('git add *')
    system('git commit -m '+'"'+dt_string+'"')
    # system("git remote add origin https://github.com/Eric106/Intelligent_Systems.git")
    system('git push origin master')
run_server()