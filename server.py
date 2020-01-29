import urllib.request 

# geeft de context weer van de webpagina
def readInternetpage(page): 
                        # page = de url
    fp = urllib.request.urlopen(page)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()

    return mystr

def stuurdobbelsteen(dice1, dice2, game_code):
    readInternetpage("https://project-a.christianvanos.com/index.php?actie=updatedice&een=" + str(dice1) + "&twee=" + str(dice2) + "&code=" + str(game_code))

def krijgdobbelsteen(game_code):
    mystr = readInternetpage("https://project-a.christianvanos.com/index.php?actie=getdice&code=" + str(game_code))
    return mystr

# De kaarten die je hebt
def getIndexkaarten(game_code, user_code):
    mystr = readInternetpage("https://project-a.christianvanos.com/index.php?actie=getindexkaarten&code=" + str(game_code) + "&gebruiker=" + str(user_code))
    listnumbers = [int(s) for s in mystr.split() if s.isdigit()]

    return listnumbers

# Maakt een game aan
def createGamecode(user_code):
    mystr = readInternetpage("https://project-a.christianvanos.com/index.php?actie=creategamecode&gebruiker=" + str(user_code))
    
    return int(mystr)

# Joint een game
def joinGame(user_code, game_code):
    mystr = readInternetpage("https://project-a.christianvanos.com/index.php?actie=joingame&gebruiker=" + str(user_code) + "&code=" + str(game_code))
        
    return int(mystr)

# leave een game 
def leaveGame(game_code, user_code):
    mystr = readInternetpage("https://project-a.christianvanos.com/index.php?actie=leavegame&gebruiker=" + str(user_code) + "&code=" + str(game_code))
    
    return mystr

# start een game 
def startGame(game_code):
    mystr = readInternetpage("https://project-a.christianvanos.com/index.php?actie=startgame&code=" + str(game_code))

    return bool(mystr)

# vraag status op van de game 
def statusGame(game_code):

    mystr = readInternetpage("https://project-a.christianvanos.com/index.php?actie=statusgame&code="+ str(game_code))
    
    return mystr

def stuurkaarten(kaart1, kaart2, kaart3, game_code, user_code):
    mystr =  readInternetpage("https://project-a.christianvanos.com/index.php?actie=stuurkaarten&code=" + str(game_code) + "&gebruiker=" + str(user_code) + "&kaart1=" + str(kaart1) + "&kaart2=" + str(kaart2) + "&kaart3=" + str(kaart3))

    return mystr

def final(kaart1, kaart2, kaart3, game_code, user_code):
    mystr =  readInternetpage("https://project-a.christianvanos.com/index.php?actie=final&code=" + str(game_code) + "&gebruiker=" + str(user_code) + "&kaart1=" + str(kaart1) + "&kaart2=" + str(kaart2) + "&kaart3=" + str(kaart3))

    return bool(mystr)