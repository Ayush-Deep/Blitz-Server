# this for server #To use this you need settings.py from this repo
#else if you have settings.py 
#then put following there without #
#messageList=['pranav','lol','me','egg','egg009']
#chatMessageTime=500000 #50000 means 500 sec don't change me recomend :)

#this file mads by Bltiz Modders
#credit if you want :) 
#No, altlist don't remove this 3 lines

import bs,bsInternal
import random
from settings import *
def message():
	bsInternal._chatMessage(random.choice(messageList))


timer= bs.Timer(chatMessageTime,message,timeType='real',repeat=True)
