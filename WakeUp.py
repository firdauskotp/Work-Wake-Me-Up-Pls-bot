import time
from time import gmtime, strftime
from datetime import datetime
import telepot
import string
from telepot.loop import MessageLoop
import re
import random
# import pymongo
# from pymongo import MongoClient

# cluster = MongoClient("mongodb+srv://<username>:<password>@cluster0.oylmd.mongodb.net/<dbname>?retryWrites=true&w=majority")
# db=cluster["wakeup"]
# col1=db["users"]
# col2=db["time"]
usertime=0
usid=0
now=datetime.now()
validtime=0
start=datetime.now()
num1=0
num2=0
ans=-1
crepic=0
x=-1
def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    global usertime
    global now
    global usid
    global crepic
    global num1
    global num2
    global ans
    global x

    print(chat_id)

    usid = chat_id

    if command == "/help":
        WakeMeUpPlsbot.sendMessage(chat_id,str("REMINDER THAT THIS BOT USES ASIA/SINGAPORE TIMEZONE \n Use /alarm followed by the time in 24 hour format and : in the middle to set the alarm time to be spammed! Example: /alarm 01:30 \n Use /clear to clear the time you input \n Use /curtime to know the current time in Asia/Singapore timezone \n Use /curalarm to show the alarm you saved \n Want to go further? use /creepypicon to include an image. If you change your mind, use /creepypicoff. By default it is off \n Want to stop the alarm? Answer the math question given by using /curans followed by the answer"))
    elif command == "/start":
        WakeMeUpPlsbot.sendMessage(chat_id,str("Welcome! REMINDER THAT THIS BOT USES ASIA/SINGAPORE TIMEZONE \n Use /help to know what commands to use"))
        WakeMeUpPlsbot.sendPhoto(chat_id,photo="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.redd.it%2Fpb59vnz6zgk51.jpg&f=1&nofb=1")
    elif command == "/curtime":
        WakeMeUpPlsbot.sendMessage(chat_id,strftime("%H:%M"))
    elif command == "/curalarm":
        if usertime ==0:
            WakeMeUpPlsbot.sendMessage(chat_id,str("You did not set an alarm!"))
        else:
            WakeMeUpPlsbot.sendMessage(chat_id,usertime)
    elif command.find("/curans") != -1:
        l=6
        if len(command[0+l+1:])==0:
            WakeMeUpPlsbot.sendMessage(chat_id,str("Please provide an answer after /curans"))
        else:
            
            ans = command[0+l+1:].strip()
            x=int(ans)
            WakeMeUpPlsbot.sendMessage(chat_id,str("Answer stored"))
    elif command == "/clear":
        usertime = 0
        WakeMeUpPlsbot.sendMessage(chat_id,str("Alarm resetted!"))
    elif command == "/creepypicon":
        crepic=1
        WakeMeUpPlsbot.sendMessage(chat_id,str("You have a terrible fate ahead"))
    elif command == "/creepypicoff":
        crepic=0
        WakeMeUpPlsbot.sendMessage(chat_id,str("Coward :p"))
            
    elif command.find("/alarm") != -1:
        l=5
        if len(command[0+l+1:])==0:
            WakeMeUpPlsbot.sendMessage(chat_id,str("Example of using the alarm \n /alarm 15:30"))
        else:
            zone = command[0+l+1:].strip()
            if re.search('[a-zA-Z]',zone):
                WakeMeUpPlsbot.sendMessage(chat_id,str("Letters detected! Only numbers please"))
            else:
                if re.search(r'\d',zone):
                    if len(zone)>5:
                        WakeMeUpPlsbot.sendMessage(chat_id,str("Invalid time"))
                    elif len(zone)==5 and zone[2]!=":":
                        WakeMeUpPlsbot.sendMessage(chat_id,str("Invalid time"))

                    elif len(zone)==4 and zone[1]==":":
                        usertime = "0"+str(zone[0])+":"+str(zone[2])+str(zone[3])
                        WakeMeUpPlsbot.sendMessage(chat_id,str("Alarm saved!"))
                        #WakeMeUpPlsbot.sendMessage(chat_id,str(usertime))
                        num1 = random.randint(0,100)
                        num2 = random.randint(0,100)
                        

                    elif len(zone)==4 and zone[2]!=":":
                        usertime = str(zone[0]) + str(zone[1]) + ":" + str(zone[2]) + str(zone[3])
                        WakeMeUpPlsbot.sendMessage(chat_id,str("Alarm saved!"))
                        #WakeMeUpPlsbot.sendMessage(chat_id,str(usertime))
                        num1 = random.randint(0,100)
                        num2 = random.randint(0,100)
                    elif len(zone)<=3:
                        WakeMeUpPlsbot.sendMessage(chat_id,str("Invalid time"))
                    else:
                        WakeMeUpPlsbot.sendMessage(chat_id,str("Alarm saved!"))
                        usertime = str(zone)
                        #WakeMeUpPlsbot.sendMessage(chat_id,str(usertime))
                        num1 = random.randint(0,100)
                        num2 = random.randint(0,100)
                        
                else:
                    WakeMeUpPlsbot.sendMessage(chat_id,str("Letters detected! Only numbers please"))
            
    
        
    else:
        WakeMeUpPlsbot.sendMessage(chat_id,str(now.strftime("Wrong command, use /help to see available commands")))
#token
WakeMeUpPlsbot = telepot.Bot('put your bot token here')
print (WakeMeUpPlsbot.getMe())

#Calling function
WakeMeUpPlsbot.message_loop({'chat':action})
#WakeMeUpPlsbot.setWebhook()
#pause
while 1:

    #validtime = now.strftime("%H:%M")
    validtime = strftime("%H:%M")


    if usid ==0:
        pass
    else:
        
        
        if usertime==0:
            #WakeMeUpPlsbot.sendMessage(usid,str(usertime))
            pass
        elif usertime==validtime:
            while True:
                WakeMeUpPlsbot.sendMessage(usid,str("WAKE UP! WANT TO STOP? ANSWER THE QUESTION \n " + str(num1) + " + " + str(num2) + "\n YOU SHOULD BE AWAKE NOW I HOPE"))
                
                if crepic==1:
                    WakeMeUpPlsbot.sendPhoto(usid, photo="https://i.pinimg.com/originals/67/0f/44/670f448418af63954c5dc20bc7932754.jpg")
                else:
                    pass
                
                if int(num1)+int(num2) == int(x):
                    print("loop break")
                    usertime=0
                    WakeMeUpPlsbot.sendMessage(usid, str("YOU ARE FREE NOW"))
                    break
                elif x==-1:
                    pass
                else:
                    WakeMeUpPlsbot.sendMessage(usid, str("WRONGGGGGGG"))
                    x = -1
                
    time.sleep(1)
