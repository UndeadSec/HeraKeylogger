######################################################
#                                                    #
#       HeraChromeKeylogger                          #
#                                                    #
# by:     UNDEADSEC                                  #
#                                                    #
# Telegram Group: https://t.me/UndeadSec             #
# YouTube Channel: https://youtube.com/c/UndeadSec   #
# Twitter: https://twitter.com/UndeadSec                #
#                                                    #
######################################################
from os import system
from huepy import *

def clear():
    system('clear')

def phpNot():
    print(red("\n\n[!] PHP installation not found. Please install PHP and run me again. http://www.php.net/ "))

def head():
    clear()
    print(cyan('''
UNDEADSEC | t.me/UndeadSec | youtube.com/c/UndeadSec - BRAZIL

██  ██ ████
██  ██ ██   ██   ██████
██████ ████ ████ ██  ██ v1.0
██  ██ ██   ██   ██████
██  ██ ████ ██   ██  ██ Twitter: https://twitter.com/UndeadSec
   CHROME KEYLOGGER
      EXTENSION'''))

def printQue(text):
    print(que(text))

def done():
    print(good('Done. Load your extension in Chrome. (/MaliciousExtension/)'))
    print(good('Your logs will be saved as logs.txt'))


def checkEd():
    print(red(" [!] Do you agree to use this tool for educational purposes only? (y/N) "), end = '')
    if input('> ').upper() != 'Y':
        clear()
        print(red('\n[ YOU ARE NOT AUTHORIZED TO USE THIS TOOL ]\n'))
        exit(0)

def end():
    clear()
    print(cyan('''
         ,-`{-`/
      ,-~ , \ {-~~-,
    ,~  ,   ,`,-~~-,`,        ██  ██ ████
  ,`   ,   { {      } }       ██  ██ ██   ██   ██████               }/
 ;     ,--/`\ \    / /        ██████ ████ ████ ██  ██      }/      /,/
;  ,-./      \ \  { {  (      ██  ██ ██   ██   ██████     /,;    ,/ ,/
; /   `       } } `, `-`-.___ ██  ██ ████ ██   ██  ██    / `,  ,/  `,/
 \|         ,`,`    `~.___,---} CHROME KEYLOGGER        / ,`,,/  ,`,;
  `        { {                      EXTENSION      __  /  ,`/   ,`,;
        /   \ \                                 _,`, `{  `,{   `,`;`
       {     } }       /~\         .-:::-.     (--,   ;\ `,}  `,`;
       \\._./ /      /` , \      ,:::::::::,     `~;   \},/  `,`;     ,-=-
        `-..-`      /. `  .\_   ;:::::::::::;  __,{     `/  `,`;     {
                   / , ~ . ^ `~`\:::::::::::<<~>-,,`,    `-,  ``,_    }
                /~~ . `  . ~  , .`~~\:::::::;    _-~  ;__,        `,-`
       /`\    /~,  . ~ , '  `  ,  .` \::::;`   <<<~```   ``-,,__   ;
      /` .`\ /` .  ^  ,  ~  ,  . ` . ~\~                      ascii by xiong

> Watch us on YouTube: https://youtube.com/c/UndeadSec 
> Follow me on Twitter: https://twitter.com/A1S0N_ 
> Contribute on Github: https://github.com/UndeadSec/HeraKeylogger 
> Join our Telegram Group(Portuguese Brazil): https://t.me/UndeadSec \n'''))
