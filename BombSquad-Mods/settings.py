import bs
enableTop5effects = True
enableTop5commands = True
enableCoinSystem = True

messageList=['pranav','lol','me','egg','egg009']
chatMessageTime=4000
#to become server owner go in getpermishanhashes and type your pb/accourID in ownerHashes=['id'] like thiz


TeamBoxcolors = ((0,2.55,2.55), (2.55,0,2.55))
#colors
#thanks to google 
#Black (0,0,0)
#White (2.55,2.55,2.55)
#Red (2.55,0,0)
#Lime (0,2.55,0)
#Blue (0,0,2.55)
#Yellow (2.55,2.55,0)
#Cyan / Aqua (0,2.55,2.55)
#Magenta / Fuchsia (2.55,0,2.55)
#Silver (1.92,1.92,1.92)
#Gray (1.28,1.28,1.28)
#Maroon (1.28,0,0)
#Olive (1.28,128,0)
#Green (0,1.28,0)
#Purple (1.28,0,1.28)
#Teal (0,1.28,1.28)
#Navy (0,0,1.28)
TeamNames = ((u'\ue048Team\ue048'),(u'\ue043Team2\ue043'))
#change Text under brackets 
TeamSeriesLength = 7
FFASeriesLength = 24
#change series length if you want



#change message that pop up when join server 
message = 'ARE YOU ENJOYING IN OUR SERVER?'
messageColor = (0,0,1)


#this is textOnMap 
#if you dont need anything here then right None
leftBottomText = u'leftBottomText'
rightBottomText = u'rightBottomText'
centerText = u'CenterText'
leftTopText = None
rightTopText = None
leftRotatingIcon = u'\ue042'
rightRotatingIcon = u'\ue042'
middleBottomTexts = ['Use "/shop commands" to \nsee commands available to buy.','Use "/shop effects" to see effects \navailable and their price.','Use "/me" or "/stats" to see your '+bs.getSpecialChar('ticket')+'\n and your stats in this server', 'Use "/buy" to buy \neffects that you like','Use "/donate" to give\n some of your tickets to other players','Use "/scoretocash" to convert \nsome of your score to '+bs.getSpecialChar('ticket')+'\nCurrent Rate: 5scores = '+bs.getSpecialChar('ticket')+'1']


#tips that comes when game ends

tips001 = ['hellow','welcome','join our discord seever ']


#powerupPickup Message
#change your self im bored
trippleBombsMessage = 'Noice'
landMinesEquippedMessage = 'idk'
impactBombsEquippedMessage = 'Cool'
stickyBombsEquippedMessage = 'wow'
glovesEquippedMessage = 'oof'
curseMessage = 'aaaaa'
iceBombsEquipped = 'cold'
healthMessage = 'Noice2'
#no shield message i removed and i hate shield 


#power ups distribution 
#dont touch here if you font kwon 
tripleBombs = 3
iceBombs = 3
punch = 3
impactBombs = 3
landMines = 2
stickyBombs = 3
shield = 2
health = 1
curse = 1


#change answers here 
questionDelay = 60 #seconds
questionsList = {'Who is the editor of this server?': 'god', 'What is the name of this game': 'bombsquad','Who is the owner of this server':'god','Which currency is used in this game?':'tickets',
       'add': None, 
       'multiply': None}


#chnage value of commands here 
availableCommands = {'/nv': 50, 
   '/ooh': 5, 
   '/playSound': 10, 
   '/box': 30, 
   '/boxall': 60, 
   '/spaz': 50, 
   '/spazall': 100, 
   '/inv': 40, 
   '/invall': 80, 
   '/tex': 20, 
   '/texall': 40, 
   '/freeze': 60, 
   '/freezeall': 100, 
   '/sleep': 40, 
   '/sleepall': 80, 
   '/thaw': 50, 
   '/thawall': 70, 
   '/kill': 80, 
   '/killall': 150, 
   '/end': 100, 
   '/hug': 60, 
   '/hugall': 100, 
   '/tint': 90, 
   '/sm': 50, 
   '/fly': 50, 
   '/flyall': 100, 
   '/heal': 50, 
   '/healall': 70, 
   '/gm': 50000, 
   '/custom': 250}

#change effect values here
availableEffects = {'ice': 500, 
   'sweat': 750, 
   'scorch': 500, 
   'glow': 400, 
   'distortion': 750, 
   'slime': 500, 
   'metal': 500, 
   'surrounder': 1000}


protag = 'PRO'
noobtag='NOOB'
newtag='NEW'









#this url is the url when client type /url im chat and becuz of this now give original stats page in stats link ohk 
url='https://youtube.com/channel/UCJTR74-W0YPbsjS7_Vj5e5g'