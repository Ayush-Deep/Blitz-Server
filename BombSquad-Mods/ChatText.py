import bs,bsInternal
import random
from settings import *
def message():
	bsInternal._chatMessage(random.choice(messageList))


timer= bs.Timer(chatMessageTime,message,timeType='real',repeat=True)