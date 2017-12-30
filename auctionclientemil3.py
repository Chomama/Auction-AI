

from __future__ import print_function #I added this because it made my life a lot easier when
#the 'end = ...' function was added in the print function that I didn't know a nice way to do
#in Python 2.7, so print statements must all have brackets in this version, no need in the server though
# Echo client program
import socket
import random
import time
import os
import platform
global count
count=0
lostFirstChain=False
lostSecondChain=False
HOST = 'localhost'    # Change this to server IP if running it over the internet

# to act as a client
PORT = 50018              # The server port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


# APPLICATION

partnerid = -1 # no partner
numberbidders = 0 # will be given by server
artists = ['Picasso', 'Rembrandt', 'Van_Gogh', 'Da_Vinci']

# DO SOMETHING HERE
# you need to change this to do something much more clever
def determinebid(itemsinauction, winnerarray, winneramount, numberbidders, players, mybidderid, artists, standings, round):
    #global variables that store if we lose a chain
    global lostFirstChain
    global lostSecondChain
    #counts for each painter
    picasso=0 
    rembrandt=0
    vanGogh=0
    daVinci=0
    
    #variable for position of each painters lowest chain
    lowestChainPicasso=0
    lowestChainRembrandt=0
    lowestChainDaVinci=0
    lowestChainVanGogh=0
    
    #dicitonary that stores the lowest chains
    chains={"lowestChainPicasso": 0, "lowestChainRembrandt": 0, "lowestChainDaVinci": 0, "lowestChainVanGogh": 0}

    #loop that finds the lowest chains
    for x in range(0, len(itemsinauction)): 
        if itemsinauction[x]=="Picasso":
            picasso+=1
            if lowestChainPicasso==0 and picasso==3:
                chains["lowestChainPicasso"]=x
        elif itemsinauction[x]=="Rembrandt":
            rembrandt+=1
            if lowestChainRembrandt==0 and rembrandt==3:
                chains["lowestChainRembrandt"]=x
        elif itemsinauction[x]=="Da_Vinci":
            daVinci+=1
            if lowestChainDaVinci==0 and daVinci==3:
                chains["lowestChainDaVinci"]=x               
        elif itemsinauction[x]=="Van_Gogh":
            vanGogh+=1
            if lowestChainVanGogh==0 and vanGogh==3:
                chains["lowestChainVanGogh"]=x
                
    sortedChains= sorted(chains, key=chains.__getitem__) #list of the sorted keys
    
    indexOfChains=[] #index of the chains in order
    for x in range(0,4): 
        indexOfChains.append(chains[sortedChains[x]])
    print("indchains", indexOfChains)
    lowestChain=sortedChains[0] #lowest chain
    secondLowest=sortedChains[1] #second lowest chain
    thirdLowest=sortedChains[2] #third lowest chain
    fourthLowest=sortedChains[3]#fourth lowest chain

    if lowestChain=="lowestChainPicasso": #changes the content of the variable so can caompare with elements in itemsinauction
        lowestChain="Picasso"
    elif lowestChain=="lowestChainRembrandt":
        lowestChain="Rembrandt"
    elif lowestChain=="lowestChainVanGogh":
        lowestChain="Van_Gogh"
    elif lowestChain=="lowestChainDaVinci":
        lowestChain="Da_Vinci"
        
    if secondLowest=="lowestChainPicasso": #changes the content of the variable so can caompare with elements in itemsinauction
        secondLowest="Picasso"
    elif secondLowest=="lowestChainRembrandt":
        secondLowest="Rembrandt"
    elif secondLowest=="lowestChainVanGogh":
        secondLowest="Van_Gogh"
    elif secondLowest=="lowestChainDaVinci":
        secondLowest="Da_Vinci"

    if thirdLowest=="lowestChainPicasso": #changes the content of the variable so can caompare with elements in itemsinauction
        thirdLowest="Picasso"
    elif thirdLowest=="lowestChainRembrandt":
        thirdLowest="Rembrandt"
    elif thirdLowest=="lowestChainVanGogh":
        thirdLowest="Van_Gogh"
    elif thirdLowest=="lowestChainDaVinci":
        thirdLowest="Da_Vinci"

    #checks if we lost a chain
    if itemsinauction[round-1]==lowestChain and standings["ferox"][lowestChain]==0:
        lostFirstChain=True
    if lostFirstChain==True and itemsinauction[round-1]==secondLowest and standings["ferox"][secondLowest]==0:
        lostSecondChain=True

##    print(standings)
##    print(chains)
##    print(itemsinauction)
##    print("Round:", round)
        
    #if statement that spends all remaining money if possible win
    if standings["ferox"]["Picasso"]==2 and itemsinauction[round]== "Picasso":
        return standings["ferox"]["money"]
    if standings["ferox"]["Da_Vinci"]==2 and itemsinauction[round]== "Da_Vinci":
        return standings["ferox"]["money"]
    if standings["ferox"]["Van_Gogh"]==2 and itemsinauction[round]== "Van_Gogh":
        return standings["ferox"]["money"]
    if standings["ferox"]["Rembrandt"]==2 and itemsinauction[round]== "Rembrandt":
        return standings["ferox"]["money"]

    #if statement that goes to third chain if lost second chain
    if lostSecondChain:
        print("Going for third chain")
        if itemsinauction[round]== thirdLowest:
            if standings["ferox"]["money"]==100:
                return 34
            else:
                return 33
        else:
            return 0


    """if statement that checks if the second chain is within 2 indexes of the
        the first chain and goes for that chain if it is.  Also goes for the
        second chain if bot loses the first chain."""
    if indexOfChains[1] - indexOfChains[0] <3 or lostFirstChain:
        print("Going for second chain")
        if itemsinauction[round]== secondLowest:
            if standings["ferox"]["money"]==100:
                return 34
            else:
                return 33
        else:
            return 0

    #if statement that bids desired amount if lowest chain
    if itemsinauction[round]== lowestChain:
        if standings["ferox"]["money"]==100:
            return 34
        else:
            return 33
        

    
    

    #if statement that checks if another bot is about to win and blocks
##    for x in range(0, len(players)):
##        if standings[players[x]]["Picasso"]==2 and itemsinauction[round]== "Picasso":
##            return standings[players[x]]["money"]+1
##        if standings[players[x]]["Da_Vinci"]==2 and itemsinauction[round]== "Da_Vinci":
##            return standings[players[x]]["money"]+1
##        if standings[players[x]]["Van_Gogh"]==2 and itemsinauction[round]== "Van_Gogh":
##            return standings[players[x]]["money"]+1
##        if standings[players[x]]["Rembrandt"]==2 and itemsinauction[round]== "Rembrandt":
##            return standings[players[x]]["money"]+1
##    


    return 0    



mybidderid = raw_input("Input team / player name : ").strip()  # this is the only thing that distinguishes the clients 
while len(mybidderid) == 0 or ' ' in mybidderid:
  mybidderid = raw_input("You input an empty string or included a space in your name which is not allowed (_ or / are all allowed)\n for example Emil_And_Nischal is okay\nInput team / player name: ").strip()

moneyleft = 100 # should change over time
winnerarray = [] # who won each round
winneramount = [] # how much they paid

itemsinauction = []
myTypes = {'Picasso': 0, 'Rembrandt': 0, 'Van_Gogh': 0, 'Da_Vinci': 0, 'money': moneyleft}

# EXECUTION

# get list of items and types
getlistflag = 1
s.send(str(mybidderid))
while(getlistflag == 1):
  # print "Have sent data from ", str(mybidderid)
  data = s.recv(5024)
  x = data.split(" ")
  # print "Have received response at ", str(mybidderid), " of: ", ' '.join(x)
  #Receives first how many players are in the game and then all 200 items in auction
  if(x[0] != "Not" and len(data) != 0):
    getlistflag = 0
    numberbidders = int(x[0])
    itemsinauction = x[1:]
  else:
    time.sleep(2)

while True:
  s.send(str(mybidderid) + ' ')
  data = s.recv(5024)
  x = data.split(" ")
  #Wait until everyone has connected before bidding
  if (x[0] == 'wait'):
    continue
  #When everyone has connected the server knows all names
  #it can therefore transfer all the names after telling the client that it's ready
  players = []
  for player in range(1, numberbidders + 1):
    players.append(x[player])
  break
#Create initial standings for each player after everyone connected
standings = {name: {'Picasso': 0, 'Van_Gogh': 0, 'Rembrandt': 0, 'Da_Vinci': 0, 'money': 100} for name in players}
# now do bids
continueflag = 1
j = 0
if platform.system() == 'Windows':
  os.system('cls')
else:
  os.system('clear')
while(continueflag == 1):
  #roundStart = time.time()
  print(random.choice(["I'm doing my best, okay?", "Why aren't you cheering louder?", "Aren't you proud of me?", "Damn I'm good, and I don't even have a brain!", "And do you think you could do any better?", "I feel like it's me doing all the work, you're just chilling in your chair", "If I lose this it's your fault not mine... I'm doing EXACTLY what you told me to do!"]))
  print()
  bidflag = 1
  bid = determinebid(itemsinauction, winnerarray, winneramount, numberbidders, players, mybidderid, artists, standings, len(winnerarray))
  #sleep before sending the bid to make sure the server is ready, currently it's at a very big value 1
  #this should make it safe for any speed of computers or internet, but can probably be lower as I have had
  #it working on Wifi with my computer at 0.2
  time.sleep(1)
  s.send(str(mybidderid) + " " + str(bid))
  while(bidflag == 1):
    # print "Have sent data from ", str(mybidderid)
    data = s.recv(5024)
    x = data.split(" ")
    # print "Have received response at ", str(mybidderid), " of: ", ' '.join(x)
    if(x[0] != "Not"):
      bidflag = 0
    else:
      print("exception")
      time.sleep(2)


  resultflag = 1
  while(resultflag == 1):
    s.send(str(mybidderid))
    # print "Have sent data from ", str(mybidderid)
    data = s.recv(5024)
    x = data.split(" ")
    #Wait for all bids to be received
    if (x[0] == 'wait'):
      continue
    # print "Have received response at ", str(mybidderid), " of: ", ' '.join(x)
    #Check if the server told client that game is finished
    if len(x) >= 7 and x[7] == 'won.':
      time.sleep(5)
      continueflag = 0
      resultflag = 0
      print(data)
      print()
      print('game over')
    #Else update standings, winnerarray etc.
    if(x[0] != "ready") and (continueflag == 1):
      #roundLength = time.time()-roundStart
      #time.sleep(max(0, 5-roundLength))
      resultflag = 0
      if platform.system() == 'Windows':
        os.system('cls')
      else:
        os.system('clear')
      # print x
      winnerarray.append(x[0])
      winneramount.append(int(x[5]))
      standings[x[0]]['money'] -= int(x[5])
      standings[x[0]][x[3]] += 1
      if (x[0] == mybidderid):
        moneyleft -= int(x[5])
        myTypes[itemsinauction[j]] += 1
      # update moneyleft, winnerarray
    else:
      time.sleep(2)
  j+= 1
