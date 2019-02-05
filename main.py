# MODULES INPORTEREN
import pygame # staat niet standaard geinstalleerd, om het te installeren ga naar cmd en type 'pip install pygame' (zonder quotes) 
import random # randomizer module
import math # wiskundige berekingen module

# ANDERE BESTANDEN INPORTEREN
import inputbox # inputbox.py -> dit bestand zorgt ervoor dat je een inputbox kan maken
import server # server.py -> dit bestand zorgt ervoor dat de juiste webpagina's worden opgevraagd met of zonder parameters voor php

# PYGAME
pygame.init() # standaard functie van pygame die altijd moet worden gedaan aan het begin van het bestand
pygame.display.set_caption('Breaking Banks') # De titel van het programma

# VARIABLES
leave = False # De mainloop van het programma wordt hiermee gedaan als deze veranderd wordt naar True betekend het eigenlijk dat je de game wilt sluiten
game_width = 400 # De standaard breedte van de game voor het menu (dat wordt het eerste laten zien)
game_height = 340 # De standaard hoogte van de game voor het menu (dat wordt het eerste laten zien)
user_code = random.randint(1,1000000000) # De user_code van de gebruiker die wordt gerandomized zo dat het voor de server duidelijk is wie, wie is
game_code = 0 # De game_code waar je in joint, dit is standaard 0, dat betekent dat je nergens in bent
joinGame = False # De variabele die als die True is aantoont dat je een game wilt joinen
createGame = False # De variabele die als die True is aantoont dat je een game wilt joinen
game_running = False # De variabele die als die True is aantoont dat je de game kan accessen, zodat er geen spelers meer kunnen joinen/dat je andere kaarten krijg
game_owner = False # De variabele die als die True is aanttont dat je de game_running variabele kan aanpassen.
gameDisplay = pygame.display.set_mode((game_width,game_height)) # Maak de actuele programma qua breedte en hoogte en zet het display in een variabele
pygame.display.set_icon(pygame.image.load('images/bank.png'))
cardsBlock_height = 0
cardsBlock_width = 0
mycards = ""
dobbelsteen1 = random.randint(1,6)
dobbelsteen2 = random.randint(1,6)

# Load variables
updatescherm = False
mainMenu = False
waitMenu = False
gameMenu = False
verdenkMenu = False
winloseMenu = False
leaveGamemenu = False

#afstreeplijst
checkboxes =  {
                0: {'x': 0, 'y': 10, 'text': "Brownsville", 'value': False, "groote": 18, "rand": 2},
                1: {'x': 5, 'y': 30, 'text': "Fort Stockton", 'value': False, "groote": 18, "rand": 2},
                2: {'x': 5, 'y': 50, 'text': "Victoria", 'value': False, "groote": 18, "rand": 2},
                3: {'x': 5, 'y': 70, 'text': "Amarillo", 'value': False, "groote": 18, "rand": 2},
                4: {'x': 5, 'y': 90, 'text': "El Dorado", 'value': False, "groote": 18, "rand": 2},
                5: {'x': 5, 'y': 110, 'text': "Dallas", 'value': False, "groote": 18, "rand": 2},
                6: {'x': 5, 'y': 130, 'text': "Houston", 'value': False, "groote": 18, "rand": 2},
                7: {'x': 5, 'y': 150, 'text': "Boston", 'value': False, "groote": 18, "rand": 2},
                8: {'x': 5, 'y': 170, 'text': "San Saba", 'value': False, "groote": 18, "rand": 2},
                9: {'x': 5, 'y': 190, 'text': "Lasso", 'value': False, "groote": 18, "rand": 2},
                10: {'x': 5, 'y': 210, 'text': "Pijl en Boog", 'value': False, "groote": 18, "rand": 2},
                11: {'x': 5, 'y': 230, 'text': "Gif", 'value': False, "groote": 18, "rand": 2},
                12: {'x': 5, 'y': 250, 'text': "Dynamiet", 'value': False, "groote": 18, "rand": 2},
                13: {'x': 5, 'y': 270, 'text': "Dolk", 'value': False, "groote": 18, "rand": 2},
                14: {'x': 5, 'y': 290, 'text': "Shotgun", 'value': False, "groote": 18, "rand": 2},
                15: {'x': 5, 'y': 310, 'text': "Revolver", 'value': False, "groote": 18, "rand": 2},
                16: {'x': 5, 'y': 330, 'text': "Hiawatha", 'value': False, "groote": 18, "rand": 2},
                17: {'x': 5, 'y': 350, 'text': "Pearl Hart", 'value': False, "groote": 18, "rand": 2},
                18: {'x': 5, 'y': 370, 'text': "Laura Ingalls", 'value': False, "groote": 18, "rand": 2},
                19: {'x': 5, 'y': 390, 'text': "Buffalo Bill", 'value': False, "groote": 18, "rand": 2},
                20: {'x': 5, 'y': 410, 'text': "Billy the Kid", 'value': False, "groote": 18, "rand": 2},
                21: {'x': 5, 'y': 430, 'text': "Clint Eastwood", 'value': False, "groote": 18, "rand": 2}
            }

# SIMPLE SIMPLE FUNCTIONS
def leaveGamevar():
    global joinGame
    global createGame
    global game_code
    global game_owner

    joinGame = False # Zet de joinGame globale variabele op False
    createGame = False # Zet de createGame globale variabele op False
    server.leaveGame(game_code, user_code)
    game_code = 0 # Zet de game_code weer op niks
    game_owner = False # Je bent niet langer de game_owner

def runGamevar():
    global game_running
    game_running = server.startGame(game_code)

def joinGamevar():
    global joinGame
    joinGame = True # Zet de joinGame globale variabele op True

def createGamevar():
    global createGame
    createGame = True # Zet de createGame globale variabele op True

def updateScherm(action = True):
    global updatescherm
    updatescherm = action

def roldobbelstenen():
    global dobbelsteen1
    global dobbelsteen2   
    dobbelsteen1 = random.randint(1,6)
    dobbelsteen2 = random.randint(1,6) 

def laatkaartzien(name, millisec):
    pygame.display.set_mode((400, 558))
    showImage(name, 0, 0, "G", 619, 865)
    if name != "22":
        checkboxes[int(name)]['value'] = True    
    pygame.display.update()
    pygame.time.delay(millisec)

def raden():
    cards = selectcard()
    global gameMenu
    global leave
    global leaveGamemenu
    gameMenu = False
    if cards != None:
        antwoord = server.final(cards[0], cards[1], cards[2], game_code, user_code)
        if antwoord == True: 
            # gewonnen
            leaveGamemenu = True
            leaveGamevar()
            pygame.display.set_mode((400,340))
            winlose_menu("gewonnen!")
        else:
            # verloren
            leaveGamemenu = True
            leaveGamevar()
            pygame.display.set_mode((400,340))
            winlose_menu("verloren!")

def verdenk():
    cards = selectcard()
    global gameMenu 
    gameMenu = False
    if cards != None:
        antwoord = server.stuurkaarten(cards[0], cards[1], cards[2], game_code, user_code)
        if antwoord.isdigit():
            laatkaartzien(antwoord, 1500)

def selectcard():
    verdenk = False
    btn0 = {'x': -3, 'y': -3, 'width': 151, 'height': 206, 'text': "", 'font': "comicsansms", 'fontsize': 20, 'color': (255, 255, 255)}
    btn1 = {'x': 147, 'y': -3, 'width': 151, 'height': 206, 'text': "", 'font': "comicsansms", 'fontsize': 20, 'color': (255, 255, 255)}
    btn2 = {'x': 297, 'y': -3, 'width': 151, 'height': 206, 'text': "", 'font': "comicsansms", 'fontsize': 20, 'color': (255, 255, 255)}
    btn3 = {'x': 447, 'y': -3, 'width': 151, 'height': 206, 'text': "", 'font': "comicsansms", 'fontsize': 20, 'color': (255, 255, 255)}
    btn4 = {'x': 597, 'y': -3, 'width': 151, 'height': 206, 'text': "", 'font': "comicsansms", 'fontsize': 20, 'color': (255, 255, 255)}
    btn5 = {'x': 747, 'y': -3, 'width': 151, 'height': 206, 'text': "", 'font': "comicsansms", 'fontsize': 20, 'color': (255, 255, 255)}
    btn6 = {'x': 897, 'y': -3, 'width': 151, 'height': 206, 'text': "", 'font': "comicsansms", 'fontsize': 20, 'color': (255, 255, 255)}
    btn7 = {'x': 1047, 'y': -3, 'width': 151, 'height': 206, 'text': "", 'font': "comicsansms", 'fontsize': 20, 'color': (255, 255, 255)}
    btn8 = {'x': -3, 'y': 202, 'width': 151, 'height': 206, 'text': "", 'font': "comicsansms", 'fontsize': 20, 'color': (255, 255, 255)}
    btn9 = {'x': 147, 'y': 202, 'width': 151, 'height': 206, 'text': "", 'font': "comicsansms", 'fontsize': 20, 'color': (255, 255, 255)}
    btn10 = {'x': 297, 'y': 202, 'width': 151, 'height': 206, 'text': "", 'font': "comicsansms", 'fontsize': 20, 'color': (255, 255, 255)}
    btn11 = {'x': 447, 'y': 202, 'width': 151, 'height': 206, 'text': "", 'font': "comicsansms", 'fontsize': 20, 'color': (255, 255, 255)}
    btn12 = {'x': 597, 'y': 202, 'width': 151, 'height': 206, 'text': "", 'font': "comicsansms", 'fontsize': 20, 'color': (255, 255, 255)}
    btn13 = {'x': 747, 'y': 202, 'width': 151, 'height': 206, 'text': "", 'font': "comicsansms", 'fontsize': 20, 'color': (255, 255, 255)}
    btn14 = {'x': 897, 'y': 202, 'width': 151, 'height': 206, 'text': "", 'font': "comicsansms", 'fontsize': 20, 'color': (255, 255, 255)}
    btn15 = {'x': 1047, 'y': 202, 'width': 151, 'height': 206, 'text': "", 'font': "comicsansms", 'fontsize': 20, 'color': (255, 255, 255)}
    btn16 = {'x': -3, 'y': 407, 'width': 151, 'height': 206, 'text': "", 'font': "comicsansms", 'fontsize': 20, 'color': (255, 255, 255)}
    btn17 = {'x': 147, 'y': 407, 'width': 151, 'height': 206, 'text': "", 'font': "comicsansms", 'fontsize': 20, 'color': (255, 255, 255)}
    btn18 = {'x': 297, 'y': 407, 'width': 151, 'height': 206, 'text': "", 'font': "comicsansms", 'fontsize': 20, 'color': (255, 255, 255)}
    btn19 = {'x': 447, 'y': 407, 'width': 151, 'height': 206, 'text': "", 'font': "comicsansms", 'fontsize': 20, 'color': (255, 255, 255)}
    btn20 = {'x': 597, 'y': 407, 'width': 151, 'height': 206, 'text': "", 'font': "comicsansms", 'fontsize': 20, 'color': (255, 255, 255)}
    btn21 = {'x': 747, 'y': 407, 'width': 151, 'height': 206, 'text': "", 'font': "comicsansms", 'fontsize': 20, 'color': (255, 255, 255)}
    btnBevestig = {'x': 900, 'y': 410, 'width': 295, 'height': 200, 'text': "Bevestigen", 'font': 'comicsansms', 'fontsize': 20, 'color': (230, 119, 0)}
    stad = None
    wapen = None
    persoon = None

    while not verdenk: 
        global verdenkMenu
        if verdenkMenu == False:
            gameDisplay = pygame.display.set_mode((1350,615))
            gameDisplay.fill((255,255,255))
            showAllcards(8, "S", 0, 0, range(0,21+1), True)            
            showAllcards(8, "S", 0, 0, range(0,21+1), False)
            button(btnBevestig['text'], btnBevestig['font'], btnBevestig['x'], btnBevestig['y'], btnBevestig['width'], btnBevestig['height'], btnBevestig['fontsize'], btnBevestig['color'])
            for item in checkboxes:
                checkboxes[item]['x'] = cardsBlock_width + 10
                pygame.draw.rect(gameDisplay, (0,0,0), (checkboxes[item]['x'], checkboxes[item]['y'], checkboxes[item]['groote'], checkboxes[item]['groote']))
                if checkboxes[item]['value'] == False:
                    pygame.draw.rect(gameDisplay, (255,255,255), (checkboxes[item]['x'] + checkboxes[item]['rand'], checkboxes[item]['y'] + checkboxes[item]['rand'], checkboxes[item]['groote'] - (2 * checkboxes[item]['rand']), checkboxes[item]['groote'] - (2 * checkboxes[item]['rand'])))
                else:
                    pygame.draw.rect(gameDisplay, (50,50,50), (checkboxes[item]['x'] + checkboxes[item]['rand'], checkboxes[item]['y'] + checkboxes[item]['rand'], checkboxes[item]['groote'] - (2 * checkboxes[item]['rand']), checkboxes[item]['groote'] - (2 * checkboxes[item]['rand'])))

                smallText = pygame.font.SysFont('comicsansms', 12) # installeer de lettertype/lettergroote
                textSurf, textRect = text_objects(checkboxes[item]['text'], smallText)  # maak een tekstobject
                textRect = ((checkboxes[item]['x'] + 30), (checkboxes[item]['y'])) # reken uit waar de tekst moet komen te staan
                gameDisplay.blit(textSurf, textRect) # zet de tekst op de button
            updateScherm()
            verdenkMenu = True

        for event in pygame.event.get(): # Krijg alle events die gebeuren
            if event.type == pygame.QUIT: # Als er op het kruisje wordt geklikt
                global leave # globale variabele opvragen om te wijzigen
                global leaveGamemenu
                leaveGamemenu = True
                leave = True # stap uit de mainloop
                verdenk = True # stap uit het menu
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if checkbinnenFiguur(pos, btn0['x'], btn0['y'], btn0['width'], btn0['height']) == True:
                        if btn0['color'] == (255,255,255):
                            btn0['color'] = (0,0,0)
                            btn1['color'] = (255,255,255)
                            btn2['color'] = (255,255,255)
                            btn3['color'] = (255,255,255)
                            btn4['color'] = (255,255,255)
                            btn5['color'] = (255,255,255)
                            btn6['color'] = (255,255,255)
                            btn7['color'] = (255,255,255)
                            btn8['color'] = (255,255,255)
                        else:
                            btn0['color'] = (255,255,255)
                    elif checkbinnenFiguur(pos, btn1['x'], btn1['y'], btn1['width'], btn1['height']) == True:
                        if btn1['color'] == (255,255,255):
                            btn1['color'] = (0,0,0)
                            btn0['color'] = (255,255,255)
                            btn2['color'] = (255,255,255)
                            btn3['color'] = (255,255,255)
                            btn4['color'] = (255,255,255)
                            btn5['color'] = (255,255,255)
                            btn6['color'] = (255,255,255)
                            btn7['color'] = (255,255,255)
                            btn8['color'] = (255,255,255)
                        else:
                            btn1['color'] = (255,255,255)
                    elif checkbinnenFiguur(pos, btn2['x'], btn2['y'], btn2['width'], btn2['height']) == True: 
                        if btn2['color'] == (255,255,255):
                            btn2['color'] = (0,0,0)
                            btn0['color'] = (255,255,255)
                            btn1['color'] = (255,255,255)
                            btn3['color'] = (255,255,255)
                            btn4['color'] = (255,255,255)
                            btn5['color'] = (255,255,255)
                            btn6['color'] = (255,255,255)
                            btn7['color'] = (255,255,255)
                            btn8['color'] = (255,255,255)
                        else:
                            btn2['color'] = (255,255,255)
                    elif checkbinnenFiguur(pos, btn3['x'], btn3['y'], btn3['width'], btn3['height']) == True: 
                        if btn3['color'] == (255,255,255):
                            btn3['color'] = (0,0,0)
                            btn0['color'] = (255,255,255)
                            btn1['color'] = (255,255,255)
                            btn2['color'] = (255,255,255)
                            btn4['color'] = (255,255,255)
                            btn5['color'] = (255,255,255)
                            btn6['color'] = (255,255,255)
                            btn7['color'] = (255,255,255)
                            btn8['color'] = (255,255,255)
                        else:
                            btn3['color'] = (255,255,255)
                    elif checkbinnenFiguur(pos, btn4['x'], btn4['y'], btn4['width'], btn4['height']) == True: 
                        if btn4['color'] == (255,255,255):
                            btn4['color'] = (0,0,0)
                            btn0['color'] = (255,255,255)
                            btn1['color'] = (255,255,255)
                            btn2['color'] = (255,255,255)
                            btn3['color'] = (255,255,255)
                            btn5['color'] = (255,255,255)
                            btn6['color'] = (255,255,255)
                            btn7['color'] = (255,255,255)
                            btn8['color'] = (255,255,255)
                        else:
                            btn4['color'] = (255,255,255)
                    elif checkbinnenFiguur(pos, btn5['x'], btn5['y'], btn5['width'], btn5['height']) == True: 
                        if btn5['color'] == (255,255,255):
                            btn5['color'] = (0,0,0)
                            btn0['color'] = (255,255,255)
                            btn1['color'] = (255,255,255)
                            btn2['color'] = (255,255,255)
                            btn3['color'] = (255,255,255)
                            btn4['color'] = (255,255,255)
                            btn6['color'] = (255,255,255)
                            btn7['color'] = (255,255,255)
                            btn8['color'] = (255,255,255)
                        else:
                            btn5['color'] = (255,255,255)
                    elif checkbinnenFiguur(pos, btn6['x'], btn6['y'], btn6['width'], btn6['height']) == True: 
                        if btn6['color'] == (255,255,255):
                            btn6['color'] = (0,0,0)
                            btn0['color'] = (255,255,255)
                            btn1['color'] = (255,255,255)
                            btn2['color'] = (255,255,255)
                            btn3['color'] = (255,255,255)
                            btn4['color'] = (255,255,255)
                            btn5['color'] = (255,255,255)
                            btn7['color'] = (255,255,255)
                            btn8['color'] = (255,255,255)
                        else:
                            btn6['color'] = (255,255,255)
                    elif checkbinnenFiguur(pos, btn7['x'], btn7['y'], btn7['width'], btn7['height']) == True: 
                        if btn7['color'] == (255,255,255):
                            btn7['color'] = (0,0,0)
                            btn0['color'] = (255,255,255)
                            btn1['color'] = (255,255,255)
                            btn2['color'] = (255,255,255)
                            btn3['color'] = (255,255,255)
                            btn4['color'] = (255,255,255)
                            btn5['color'] = (255,255,255)
                            btn6['color'] = (255,255,255)
                            btn8['color'] = (255,255,255)
                        else:
                            btn7['color'] = (255,255,255)
                    elif checkbinnenFiguur(pos, btn8['x'], btn8['y'], btn8['width'], btn8['height']) == True: 
                        if btn8['color'] == (255,255,255):
                            btn8['color'] = (0,0,0)
                            btn0['color'] = (255,255,255)
                            btn1['color'] = (255,255,255)
                            btn2['color'] = (255,255,255)
                            btn3['color'] = (255,255,255)
                            btn4['color'] = (255,255,255)
                            btn5['color'] = (255,255,255)
                            btn6['color'] = (255,255,255)
                            btn7['color'] = (255,255,255)
                        else:
                            btn8['color'] = (255,255,255)
                    elif checkbinnenFiguur(pos, btn9['x'], btn9['y'], btn9['width'], btn9['height']) == True: 
                        if btn9['color'] == (255,255,255):
                            btn9['color'] = (0,0,0)
                            btn10['color'] = (255,255,255)
                            btn11['color'] = (255,255,255)
                            btn12['color'] = (255,255,255)
                            btn13['color'] = (255,255,255)
                            btn14['color'] = (255,255,255)
                            btn15['color'] = (255,255,255)
                        else:
                            btn9['color'] = (255,255,255)
                    elif checkbinnenFiguur(pos, btn10['x'], btn10['y'], btn10['width'], btn10['height']) == True: 
                        if btn10['color'] == (255,255,255):
                            btn10['color'] = (0,0,0)
                            btn9['color'] = (255,255,255)
                            btn11['color'] = (255,255,255)
                            btn12['color'] = (255,255,255)
                            btn13['color'] = (255,255,255)
                            btn14['color'] = (255,255,255)
                            btn15['color'] = (255,255,255)
                        else:
                            btn10['color'] = (255,255,255)
                    elif checkbinnenFiguur(pos, btn11['x'], btn11['y'], btn11['width'], btn11['height']) == True: 
                        if btn11['color'] == (255,255,255):
                            btn11['color'] = (0,0,0)
                            btn9['color'] = (255,255,255)
                            btn10['color'] = (255,255,255)
                            btn12['color'] = (255,255,255)
                            btn13['color'] = (255,255,255)
                            btn14['color'] = (255,255,255)
                            btn15['color'] = (255,255,255)
                        else:
                            btn11['color'] = (255,255,255)
                    elif checkbinnenFiguur(pos, btn12['x'], btn12['y'], btn12['width'], btn12['height']) == True: 
                        if btn12['color'] == (255,255,255):
                            btn12['color'] = (0,0,0)
                            btn9['color'] = (255,255,255)
                            btn10['color'] = (255,255,255)
                            btn11['color'] = (255,255,255)
                            btn13['color'] = (255,255,255)
                            btn14['color'] = (255,255,255)
                            btn15['color'] = (255,255,255)
                        else:
                            btn12['color'] = (255,255,255)
                    elif checkbinnenFiguur(pos, btn13['x'], btn13['y'], btn13['width'], btn13['height']) == True: 
                        if btn13['color'] == (255,255,255):
                            btn13['color'] = (0,0,0)
                            btn9['color'] = (255,255,255)
                            btn10['color'] = (255,255,255)
                            btn11['color'] = (255,255,255)
                            btn12['color'] = (255,255,255)
                            btn14['color'] = (255,255,255)
                            btn15['color'] = (255,255,255)
                        else:
                            btn13['color'] = (255,255,255)
                    elif checkbinnenFiguur(pos, btn14['x'], btn14['y'], btn14['width'], btn14['height']) == True: 
                        if btn14['color'] == (255,255,255):
                            btn14['color'] = (0,0,0)
                            btn9['color'] = (255,255,255)
                            btn10['color'] = (255,255,255)
                            btn11['color'] = (255,255,255)
                            btn12['color'] = (255,255,255)
                            btn13['color'] = (255,255,255)
                            btn15['color'] = (255,255,255)
                        else:
                            btn14['color'] = (255,255,255)
                    elif checkbinnenFiguur(pos, btn15['x'], btn15['y'], btn15['width'], btn15['height']) == True: 
                        if btn15['color'] == (255,255,255):
                            btn15['color'] = (0,0,0)
                            btn9['color'] = (255,255,255)
                            btn10['color'] = (255,255,255)
                            btn11['color'] = (255,255,255)
                            btn12['color'] = (255,255,255)
                            btn13['color'] = (255,255,255)
                            btn14['color'] = (255,255,255)
                        else:
                            btn15['color'] = (255,255,255)
                    elif checkbinnenFiguur(pos, btn16['x'], btn16['y'], btn16['width'], btn16['height']) == True: 
                        if btn16['color'] == (255,255,255):
                            btn16['color'] = (0,0,0)
                            btn17['color'] = (255,255,255)
                            btn18['color'] = (255,255,255)
                            btn19['color'] = (255,255,255)
                            btn20['color'] = (255,255,255)
                            btn21['color'] = (255,255,255)
                        else:
                            btn16['color'] = (255,255,255)
                    elif checkbinnenFiguur(pos, btn17['x'], btn17['y'], btn17['width'], btn17['height']) == True: 
                        if btn17['color'] == (255,255,255):
                            btn17['color'] = (0,0,0)
                            btn16['color'] = (255,255,255)
                            btn18['color'] = (255,255,255)
                            btn19['color'] = (255,255,255)
                            btn20['color'] = (255,255,255)
                            btn21['color'] = (255,255,255)
                        else:
                            btn17['color'] = (255,255,255)
                    elif checkbinnenFiguur(pos, btn18['x'], btn18['y'], btn18['width'], btn18['height']) == True: 
                        if btn18['color'] == (255,255,255):
                            btn18['color'] = (0,0,0)
                            btn16['color'] = (255,255,255)
                            btn17['color'] = (255,255,255)
                            btn19['color'] = (255,255,255)
                            btn20['color'] = (255,255,255)
                            btn21['color'] = (255,255,255)
                        else:
                            btn18['color'] = (255,255,255)
                    elif checkbinnenFiguur(pos, btn19['x'], btn19['y'], btn19['width'], btn19['height']) == True: 
                        if btn19['color'] == (255,255,255):
                            btn19['color'] = (0,0,0)
                            btn16['color'] = (255,255,255)
                            btn17['color'] = (255,255,255)
                            btn18['color'] = (255,255,255)
                            btn20['color'] = (255,255,255)
                            btn21['color'] = (255,255,255)
                        else:
                            btn19['color'] = (255,255,255)
                    elif checkbinnenFiguur(pos, btn20['x'], btn20['y'], btn20['width'], btn20['height']) == True: 
                        if btn20['color'] == (255,255,255):
                            btn20['color'] = (0,0,0)
                            btn16['color'] = (255,255,255)
                            btn17['color'] = (255,255,255)
                            btn18['color'] = (255,255,255)
                            btn19['color'] = (255,255,255)
                            btn21['color'] = (255,255,255)
                        else:
                            btn20['color'] = (255,255,255)
                    elif checkbinnenFiguur(pos, btn21['x'], btn21['y'], btn21['width'], btn21['height']) == True: 
                        if btn21['color'] == (255,255,255):
                            btn21['color'] = (0,0,0)
                            btn16['color'] = (255,255,255)
                            btn17['color'] = (255,255,255)
                            btn18['color'] = (255,255,255)
                            btn19['color'] = (255,255,255)
                            btn20['color'] = (255,255,255)
                        else:
                            btn21['color'] = (255,255,255)
                    elif checkbinnenFiguur(pos, btnBevestig['x'], btnBevestig['y'], btnBevestig['width'], btnBevestig['height']):
                        if btn0['color'] == (0,0,0):
                            stad = 0
                        elif btn1['color'] == (0,0,0):
                            stad = 1
                        elif btn2['color'] == (0,0,0):
                            stad = 2
                        elif btn3['color'] == (0,0,0):
                            stad = 3
                        elif btn4['color'] == (0,0,0):
                            stad = 4
                        elif btn5['color'] == (0,0,0):
                            stad = 5
                        elif btn6['color'] == (0,0,0):
                            stad = 6
                        elif btn7['color'] == (0,0,0):
                            stad = 7
                        elif btn8['color'] == (0,0,0):
                            stad = 8

                        if btn9['color'] == (0,0,0):
                            wapen = 9
                        elif btn10['color'] == (0,0,0):
                            wapen = 10
                        elif btn11['color'] == (0,0,0):
                            wapen = 11
                        elif btn12['color'] == (0,0,0):
                            wapen = 12
                        elif btn13['color'] == (0,0,0):
                            wapen = 13
                        elif btn14['color'] == (0,0,0):
                            wapen = 14
                        elif btn15['color'] == (0,0,0):
                            wapen = 15

                        if btn16['color'] == (0,0,0):
                            persoon = 16
                        elif btn17['color'] == (0,0,0):
                            persoon = 17
                        elif btn18['color'] == (0,0,0):
                            persoon = 18
                        elif btn19['color'] == (0,0,0):
                            persoon = 19
                        elif btn20['color'] == (0,0,0):
                            persoon = 20
                        elif btn21['color'] == (0,0,0):
                            persoon = 21

                        verdenk = True

                    button(btn0['text'], btn0['font'], btn0['x'], btn0['y'], btn0['width'], btn0['height'], btn0['fontsize'], btn0['color'])
                    button(btn1['text'], btn1['font'], btn1['x'], btn1['y'], btn1['width'], btn1['height'], btn1['fontsize'], btn1['color'])
                    button(btn2['text'], btn2['font'], btn2['x'], btn2['y'], btn2['width'], btn2['height'], btn2['fontsize'], btn2['color'])
                    button(btn3['text'], btn3['font'], btn3['x'], btn3['y'], btn3['width'], btn3['height'], btn3['fontsize'], btn3['color'])
                    button(btn4['text'], btn4['font'], btn4['x'], btn4['y'], btn4['width'], btn4['height'], btn4['fontsize'], btn4['color'])
                    button(btn5['text'], btn5['font'], btn5['x'], btn5['y'], btn5['width'], btn5['height'], btn5['fontsize'], btn5['color'])
                    button(btn6['text'], btn6['font'], btn6['x'], btn6['y'], btn6['width'], btn6['height'], btn6['fontsize'], btn6['color'])
                    button(btn7['text'], btn7['font'], btn7['x'], btn7['y'], btn7['width'], btn7['height'], btn7['fontsize'], btn7['color'])
                    button(btn8['text'], btn8['font'], btn8['x'], btn8['y'], btn8['width'], btn8['height'], btn8['fontsize'], btn8['color'])
                    button(btn9['text'], btn9['font'], btn9['x'], btn9['y'], btn9['width'], btn9['height'], btn9['fontsize'], btn9['color'])
                    button(btn10['text'], btn10['font'], btn10['x'], btn10['y'], btn10['width'], btn10['height'], btn10['fontsize'], btn10['color'])
                    button(btn11['text'], btn11['font'], btn11['x'], btn11['y'], btn11['width'], btn11['height'], btn11['fontsize'], btn11['color'])
                    button(btn12['text'], btn12['font'], btn12['x'], btn12['y'], btn12['width'], btn12['height'], btn12['fontsize'], btn12['color'])
                    button(btn13['text'], btn13['font'], btn13['x'], btn13['y'], btn13['width'], btn13['height'], btn13['fontsize'], btn13['color'])
                    button(btn14['text'], btn14['font'], btn14['x'], btn14['y'], btn14['width'], btn14['height'], btn14['fontsize'], btn14['color'])
                    button(btn15['text'], btn15['font'], btn15['x'], btn15['y'], btn15['width'], btn15['height'], btn15['fontsize'], btn15['color'])
                    button(btn16['text'], btn16['font'], btn16['x'], btn16['y'], btn16['width'], btn16['height'], btn16['fontsize'], btn16['color'])
                    button(btn17['text'], btn17['font'], btn17['x'], btn17['y'], btn17['width'], btn17['height'], btn17['fontsize'], btn17['color'])
                    button(btn18['text'], btn18['font'], btn18['x'], btn18['y'], btn18['width'], btn18['height'], btn18['fontsize'], btn18['color'])
                    button(btn19['text'], btn19['font'], btn19['x'], btn19['y'], btn19['width'], btn19['height'], btn19['fontsize'], btn19['color'])
                    button(btn20['text'], btn20['font'], btn20['x'], btn20['y'], btn20['width'], btn20['height'], btn20['fontsize'], btn20['color'])
                    button(btn21['text'], btn21['font'], btn21['x'], btn21['y'], btn21['width'], btn21['height'], btn21['fontsize'], btn21['color'])
                    showAllcards(8, "S", 0, 0, range(0,21+1), False)
                    updateScherm()

        if updatescherm == True:
            pygame.display.update()
            updateScherm(False)
    
    if persoon != None and stad != None and wapen != None:
        return stad, wapen, persoon
    else:
        return None

# SIMPLE FUNCTIONS 

# functie om een afbeelding op het scherm te laten zien (.png)
def showImage(name, x, y, gors, width, height):
                # index is de bestandsnaam zonder extensie
                # x = is de x-coordinaat van de afbeelding (linksboven in van de afbeelding)
                # y = is de y-coordinaat van de afbeelding (linkboven in van de afbeelding)
                # gors = great or small || great -> 400x558 | small -> 145x200 ||
    filename = str(name) + str(gors) + ".png"
    image = pygame.image.load("images/" + filename)  # De betreffende afbeelding laden
    gameDisplay.blit(image, (x,y)) # De betreffende afbeelding toevoegen op het scherm

def checkbinnenFiguur(pos, x, y, width, height):
    myx = pos[0]
    myy = pos[1]

    if myx >= x and myx <= (x+width) and myy >= y and myy <= (y+height):
        return True
    return False

# functie om tekst mee te laten zien op het scherm
def text_objects(text, font):
                    # text = de tekst
                    # font = het lettertype
    textSurface = font.render(text, True, (0,0,0)) # De betreffende tekst in een object krijgen
    return textSurface, textSurface.get_rect() # return het tekstobject en de rechthoek waar die in zit
# functie om een button mee te maken
def button(text, font, x, y, width, height, fontsize, color):
            # text = de tekst op de button
            # font = het lettertype op de button
            # x = de x-coordinaat van de button (linksboven in de button)
            # y = de y-coordinaat van de button (linksboven in de button)
            # width = de breedte van de button
            # height = de hoogte van de button
            # fontsize = de lettergroote op de button
            # color = de standaard achtergrondkleur van de button
            # hovercolor = de achtergrondkleur van de button als de muis erover gaat
            # action = de functie die moet worden uitgevoerd als er op de button wordt geklikt           
    # Als de muis niet op de knop komt 
    pygame.draw.rect(gameDisplay, color, (x, y, width, height)) # maak de knop de normale color

    smallText = pygame.font.SysFont(font, fontsize) # installeer de lettertype/lettergroote
    textSurf, textRect = text_objects(text, smallText)  # maak een tekstobject
    textRect.center = ((x + (width/2)), (y + (height/2))) # reken uit waar de tekst moet komen te staan
    gameDisplay.blit(textSurf, textRect) # zet de tekst op de button

# BIG FUNCTIONS     
    
# functie om de kaarten die je hebt te laten zien
def showAllcards(cards_one_row, gors, default_x, default_y, myCards, laden): 
                # cards_one_row geeft aan hoeveel kaarten er max naast elkaar mogen staan
                # gors geeft aan welke afbeelding er moet worden gekozen bijv (index)+gosp.png
                # default_x geeft aan waar het blok begint qua x waarde
                # default_y geeft aan waar het blok begint qua y waard
    if laden == True:
        global cardsBlock_height
        global cardsBlock_width
    else:
        global gameDisplay # globale variabele opvragen om te wijzigen
    
    image_x = default_x # aan andere variable toe wijzen zodat je altijd nog het origineel heb
    image_y = default_y # aan andere variable toe wijzen zodat je altijd nog het origineel heb
   
    # in de vorm van een list met de nummers van de kaarten die je hebt
    if laden == True:
        if len(myCards) > cards_one_row: # De breedte van het blok kaarten uitrekenen als er meer dan card_one_row kaarten zijn
            cardsBlock_width = cards_one_row * 150 + default_x
        else: # anders is de breedte het aantal kaarten * breedte + default_x
            if len(myCards) > 3:
                cardsBlock_width = len(myCards) * 150 + default_x
            else:
                cardsBlock_width = 600 + default_x

        cardsBlock_height = math.ceil(len(myCards) / cards_one_row) * 205 + default_y # hoogte van het kaarten blok uitrekenen
    else: 
        for image_card in myCards: # loop door de kaarten
            showImage(image_card, image_x, image_y, gors, 145, 200) # laat de kaart zien
            if image_x + 150 + 150 <= cardsBlock_width: # als het aantal afbeeldingen op 1 regel nog niet af is
                image_x += 150 # de x waarde voor de volgende afbeelding updaten
            else: # als er genoeg afbeeldingen op de regel zijn
                image_x = default_x # terug naar default_x waarde
                image_y += 205 # ga 1 regel naar beneden
        image_x = default_x # ga terug naar default
        image_y = default_y # ga terug naar default
        updateScherm()
# menu waar je moet wachten tot de game_owner de game start
def waiting_menu():
    leavewaitingMenu = False # variabele die de loop regelt
    button1 = {'x': 50, 'y': 190, 'width': 300, 'height': 50, 'text': "Start het spel", 'font': "comicsansms", 'fontsize': 20, 'color': (230, 119, 0)}
    button2 = {'x': 50, 'y': 255, 'width': 300, 'height': 50, 'text': "Terug", 'font': "comicsansms", 'fontsize': 20, 'color': (230, 119, 0)}

    while not leavewaitingMenu: # zolang leavewaitingmenu false is    
        global waitMenu
        if waitMenu == False:
            smallText = pygame.font.SysFont('calibri', 50) # installeer lettertype/lettergroote
            textSurf, textRect = text_objects("Breaking Banks", smallText) # maak een text object aan
            textRect.center = (200, 40) # reken uit waar het moet komen te staan
            gameDisplay.blit(textSurf, textRect) # laat het zien op het scherm
            smallText = pygame.font.SysFont('calibri', 30) # installeer lettertype/lettergroote
            textSurf, textRect = text_objects("De game code is: " + str(game_code), smallText) # maak een text object aan
            textRect.center = (200, 100) # reken uit waar het moet komen te staan
            gameDisplay.blit(textSurf, textRect) # laat het zien op het scherm
            if game_owner == True: # als je de game_owner bent
                button(button1['text'], button1['font'], button1['x'], button1['y'], button1['width'], button1['height'], button1['fontsize'], button1['color']) # rungamevar # dan heb je de mogelijkheid om de game te starten
            button(button2['text'], button2['font'], button2['x'], button2['y'], button2['width'], button2['height'], button2['fontsize'], button2['color']) # leavegamevar # leave the game
            updateScherm()
            waitMenu = True
        
        for event in pygame.event.get(): # krijg alle events in pygame
            if event.type == pygame.QUIT: # als er op het kruisje wordt geklikt
                global leave # globale variabele ophalen om te wijzigen
                leave = True # algemene gameloop gaat uit
                leavewaitingMenu = True # waiting menu gaat uit
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    pos = pygame.mouse.get_pos()
                    if checkbinnenFiguur(pos, button1['x'], button1['y'], button1['width'], button1['height']) == True:
                        if game_owner == True:
                            runGamevar()
                    elif checkbinnenFiguur(pos, button2['x'], button2['y'], button2['width'], button2['height']) == True:
                        leaveGamevar()
                    
                    if joinGame == False and createGame == False: # voor de leave button zodat je uit deze loop gaat
                        leavewaitingMenu = True # ga uit deze loop
                        updateScherm()     
        
        if server.statusGame(game_code) == "True":
            global game_running # globale variabele ophalen om te wijzigen
            game_running = True       
        
        if game_running == True: # voor de start button zodat je uit deze loop gaat
            leavewaitingMenu = True # ga uit deze loop
            updateScherm()

        if updatescherm == True:
            pygame.display.update()
            updateScherm(False)

def winlose_menu(winorlose):
    leavewinlose = False
    global leave
    global winloseMenu

    while not leavewinlose:
        if winloseMenu == False:
            gameDisplay.fill((255,255,255))
            smallText = pygame.font.SysFont('calibri', 50) # instaleer het lettertype / lettergrootte
            textSurf, textRect = text_objects("Breaking Banks", smallText) # maak een tekstobject
            textRect.center = (200, 50) # reken uit waar de button moet komen te staan
            gameDisplay.blit(textSurf, textRect) # zet de tekst op de button
            smallText = pygame.font.SysFont('calibri', 20) # instaleer het lettertype / lettergrootte
            textSurf, textRect = text_objects("Je hebt " + winorlose, smallText) # maak een tekstobject
            textRect.center = (200, 120) # reken uit waar de button moet komen te staan
            gameDisplay.blit(textSurf, textRect) # zet de tekst op de button
            button("Ga naar het menu", "comicsansms", 50, 190, 300, 50, 20, (230,119,0))
            updateScherm()
            winloseMenu = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                leavewinlose = True
                leave = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if checkbinnenFiguur(pos, 50, 190, 300, 50):
                        leavewinlose = True
                        global verdenkMenu 
                        verdenkMenu = False
                        global game_running
                        game_running = False
                        global game_owner 
                        game_owner = False
                        winloseMenu = False
                        global checkboxes

                        for item in checkboxes:
                            checkboxes[item]['value'] = False
        
        if updatescherm == True:
            pygame.display.update()
            updateScherm(False)
# menu met inputbox om een game te joinen
def joining_menu():
    leaveJoiningMenu = False # als deze variabele True is dan leave je joining_menu
    join_game_code = 0 # joining game code aanmaken
    while not leaveJoiningMenu: # zolang de mainloop van joining menu True is
        for event in pygame.event.get(): # alle events in pygame opvragen
            if event.type == pygame.QUIT: # als er op het kruisje wordt geklikt
                global leave # globale variabele ophalen om te wijzigen
                leave = True # algemene mainloop gaat uit
                leaveJoiningMenu = True # joining menu gaat uit

        smallText = pygame.font.SysFont('calibri', 50) # installeer het lettertype / lettergrote
        textSurf, textRect = text_objects("Breaking Banks", smallText) # maak een tekstobject aan
        textRect.center = (200, 40) # zet de tekst op de goede plek
        gameDisplay.blit(textSurf, textRect) # laat de tekst zien op het scherm

        join_game_code = inputbox.ask(gameDisplay, "Game code", 50, 125, 300, 50) # Vraag om de code

        global joinGame # globale variabele ophalen om te wijzigen

        if (join_game_code == ""): # als de ingevulde code leeg is
            joinGame = False # ga terug naar het beginmenu
            join_game_code = 0 # game_code = 0 dus niet in een room
            leaveJoiningMenu = True
        else:
            joinGame = False # ga terug naar het beginmenu
            leaveJoiningMenu = True
        pygame.display.update()
    return int(join_game_code) # return de waarde van de ingevulde game_code
# menu met join game en create game buttons
def menu(): 
    leaveMenu = False # De mainloop van het start menu wordt hiergedaan, als deze variabele wordt gewijzigd naar True, dan leave je het menu
    button1 = {'x': 50, 'y': 125, 'width': 300, 'height': 50, 'text': "Maak een spel aan!", 'font': "comicsansms", 'fontsize': 20, 'color': (230, 119, 0)}
    button2 = {'x': 50, 'y': 190, 'width': 300, 'height': 50, 'text': "Join bij een spel!", 'font': "comicsansms", 'fontsize': 20, 'color': (230, 119, 0)}

    while not leaveMenu: # zolang de mainloop van menu True is     
        global mainMenu
        if mainMenu == False:
            smallText = pygame.font.SysFont('calibri', 50) # instaleer het lettertype / lettergrootte
            textSurf, textRect = text_objects("Breaking Banks", smallText) # maak een tekstobject
            textRect.center = (200, 50) # reken uit waar de button moet komen te staan
            gameDisplay.blit(textSurf, textRect) # zet de tekst op de button
            button(button1['text'], button1['font'], button1['x'], button1['y'], button1['width'], button1['height'], button1['fontsize'], button1['color']) # laat de create button zien
            button(button2['text'], button2['font'], button2['x'], button2['y'], button2['width'], button2['height'], button2['fontsize'], button2['color']) # laat de join button zien
            updateScherm()            
            mainMenu = True        

        for event in pygame.event.get(): # Krijg alle events die gebeuren
            if event.type == pygame.QUIT: # Als er op het kruisje wordt geklikt
                global leave # globale variabele opvragen om te wijzigen
                leave = True # stap uit de mainloop
                leaveMenu = True # stap uit het menu
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    pos = pygame.mouse.get_pos()
                    if checkbinnenFiguur(pos, button1['x'], button1['y'], button1['width'], button1['height']) == True:
                        createGamevar()
                    elif checkbinnenFiguur(pos, button2['x'], button2['y'], button2['width'], button2['height']) == True:
                        joinGamevar()

                    if createGame == True: # Als createGame True is
                        leaveMenu = True # stap uit het menu
                    elif joinGame == True: # Als joinGame True is
                        leaveMenu = True # stap uit het menu        
             
        if updatescherm == True:
            pygame.display.update() # update pygame scherm
            updateScherm(False)

def game_menu():
    global leaveGamemenu
    leaveGamemenu = False
    button1 = {'x': 0, 'y': 125, 'width': 300, 'height': 150, 'text': "Raden", 'font': "comicsansms", 'fontsize': 20, 'color': (230, 119, 0)}
    button2 = {'x': 50, 'y': 190, 'width': 300, 'height': 150, 'text': "Verdenk", 'font': "comicsansms", 'fontsize': 20, 'color': (230, 119, 0)}
    button3 = {'x': 50, 'y': 190, 'width': 350, 'height': 150, 'text': "", 'font': "comicsansms", 'fontsize': 20, 'color': (255, 255, 255)}
    kaarten = []
    los = True
    while not leaveGamemenu:
        global gameMenu
        global dobbelsteen1
        global dobbelsteen2
        if gameMenu == False:
            mycards = server.getIndexkaarten(game_code, user_code)
            kaarten = mycards
            showAllcards(7, "S", 0, 0, mycards, True)
            button1['y'] = cardsBlock_height
            button1['width'] = (cardsBlock_width-350)/2 - 10
            button2['x'] = (cardsBlock_width-350)/2
            button2['y'] = cardsBlock_height
            button2['width'] = (cardsBlock_width-350)/2 - 10
            button3['x'] = cardsBlock_width-350
            button3['y'] = cardsBlock_height
            
            if cardsBlock_height+150 < 450:
                actualHeight = 450
            else: 
                actualHeight = cardsBlock_height + 150

            gameDisplay = pygame.display.set_mode((cardsBlock_width + 150,actualHeight))
            gameDisplay.fill((255,255,255))
            showAllcards(7, "S", 0, 0, mycards, False)
            button(button1['text'], button1['font'], button1['x'], button1['y'], button1['width'], button1['height'], button1['fontsize'], button1['color']) # raden
            button(button2['text'], button2['font'], button2['x'], button2['y'], button2['width'], button2['height'], button2['fontsize'], button2['color']) # verdenk
            button(button3['text'], button3['font'], button3['x'], button3['y'], button3['width'], button3['height'], button3['fontsize'], button3['color']) # roldobbelstenen         
            showImage(("dice_" + str(dobbelsteen1)), button3['x'], button3['y'], "", 150, 150)
            showImage(("dice_" + str(dobbelsteen2)), button3['x']+200, button3['y'], "", 150, 150)

            for item in checkboxes:
                checkboxes[item]['x'] = cardsBlock_width + 10
                if item in mycards:
                    checkboxes[item]['value'] = True
                pygame.draw.rect(gameDisplay, (0,0,0), (checkboxes[item]['x'], checkboxes[item]['y'], checkboxes[item]['groote'], checkboxes[item]['groote']))
                if checkboxes[item]['value'] == False:
                    pygame.draw.rect(gameDisplay, (255,255,255), (checkboxes[item]['x'] + checkboxes[item]['rand'], checkboxes[item]['y'] + checkboxes[item]['rand'], checkboxes[item]['groote'] - (2 * checkboxes[item]['rand']), checkboxes[item]['groote'] - (2 * checkboxes[item]['rand'])))
                else:
                    pygame.draw.rect(gameDisplay, (50,50,50), (checkboxes[item]['x'] + checkboxes[item]['rand'], checkboxes[item]['y'] + checkboxes[item]['rand'], checkboxes[item]['groote'] - (2 * checkboxes[item]['rand']), checkboxes[item]['groote'] - (2 * checkboxes[item]['rand'])))

                smallText = pygame.font.SysFont('comicsansms', 12) # installeer de lettertype/lettergroote
                textSurf, textRect = text_objects(checkboxes[item]['text'], smallText)  # maak een tekstobject
                textRect = ((checkboxes[item]['x'] + 30), (checkboxes[item]['y'])) # reken uit waar de tekst moet komen te staan
                gameDisplay.blit(textSurf, textRect) # zet de tekst op de button

            updateScherm()
            gameMenu = True
            

        if kaarten != server.getIndexkaarten(game_code, user_code):
            gameMenu = False
            for item in checkboxes:
                checkboxes[item]['value'] = False
            continue

        serverdice = (server.krijgdobbelsteen(game_code)).split()
        if len(serverdice) == 0:
            leaveGamemenu = True
            leaveGamevar()
            pygame.display.set_mode((400,340))
            winlose_menu("verloren!")
        else: 
            if serverdice[0] != dobbelsteen1 and int(serverdice[0]) > 0 and int(serverdice[0]) < 7:            
                dobbelsteen1 = serverdice[0]
                showImage(("dice_" + str(dobbelsteen1)), button3['x'], button3['y'], "", 150, 150)
                updateScherm()
            if serverdice[1] != dobbelsteen2 and int(serverdice[1]) > 0 and int(serverdice[1]) < 7:            
                dobbelsteen2 = serverdice[1]
                showImage(("dice_" + str(dobbelsteen2)), button3['x']+200, button3['y'], "", 150, 150)
                updateScherm()        

        while not los:
            roldobbelstenen()
            showImage(("dice_" + str(dobbelsteen1)), button3['x'], button3['y'], "", 150, 150)
            showImage(("dice_" + str(dobbelsteen2)), button3['x']+200, button3['y'], "", 150, 150)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    los = True
                    server.stuurdobbelsteen(dobbelsteen1, dobbelsteen2, game_code)

        for event in pygame.event.get(): # Krijg alle events die gebeuren
            if event.type == pygame.QUIT: # Als er op het kruisje wordt geklikt
                global leave # globale variabele opvragen om te wijzigen
                leave = True # stap uit de mainloop
                leaveGamemenu = True # stap uit het menu 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    pos = pygame.mouse.get_pos()
                    global verdenkMenu
                    if checkbinnenFiguur(pos, button1['x'], button1['y'], button1['width'], button1['height']) == True:
                        verdenkMenu = False
                        raden()
                    elif checkbinnenFiguur(pos, button2['x'], button2['y'], button2['width'], button2['height']) == True:
                        verdenkMenu = False
                        verdenk()
                    elif checkbinnenFiguur(pos, button3['x'], button3['y'], button3['width'], button3['height']) == True:
                        los = False
                    
                    for item in checkboxes:
                        if checkbinnenFiguur(pos, checkboxes[item]['x'], checkboxes[item]['y'], (checkboxes[item]['groote'] + checkboxes[item]['rand']), (checkboxes[item]['groote'] + checkboxes[item]['rand'])):
                            checkboxes[item]['value'] = not(checkboxes[item]['value'])
                            pygame.draw.rect(gameDisplay, (0,0,0), (checkboxes[item]['x'], checkboxes[item]['y'], checkboxes[item]['groote'], checkboxes[item]['groote']))
                            if checkboxes[item]['value'] == False:
                                pygame.draw.rect(gameDisplay, (255,255,255), (checkboxes[item]['x'] + checkboxes[item]['rand'], checkboxes[item]['y'] + checkboxes[item]['rand'], checkboxes[item]['groote'] - (2 * checkboxes[item]['rand']), checkboxes[item]['groote'] - (2 * checkboxes[item]['rand'])))
                            else:
                                pygame.draw.rect(gameDisplay, (50,50,50), (checkboxes[item]['x'] + checkboxes[item]['rand'], checkboxes[item]['y'] + checkboxes[item]['rand'], checkboxes[item]['groote'] - (2 * checkboxes[item]['rand']), checkboxes[item]['groote'] - (2 * checkboxes[item]['rand'])))

                            updateScherm()


        if updatescherm == True:
            pygame.display.update() # update pygame scherm
            updateScherm(False)        

while not leave: # zolang de mainloop True is
    for event in pygame.event.get(): # Krijg alle events die gebeuren
        if event.type == pygame.QUIT: # Als er op het kruisje wordt geklikt
            leave = True # Stap uit de mainloop

    gameDisplay.fill((255,255,255)) # witte achtergrond
        
    # game_code opvragen:
    if createGame == True: # game_code opvragen door middel van "create"
        game_code = server.createGamecode(user_code) # vraag de game_code op via de server door de game te maken
        game_owner = True # Jij bent de baas van het spel
        createGame = False # Je kan niet meer een ander spel aanmaken
    if joinGame == True: # game_code opvragen door middel van "join"
        updateScherm()
        game_code = server.joinGame(user_code, joining_menu()) # vraag de game_code op via joining_menu() en check via de server als dat correct is
        if game_code > 0: # Als de game_code is ingesteld
            joinGame = False # Je kan niet meer in een ander spel joinen
        elif game_code == 0: # als game_code 0 is dan bestaat de game niet of hij zit al vol met 6 personen
            joinGame = False
            continue # Probeer het opnieuw

    # Ga naar het juiste menu
    if game_code != 0 and game_running == True: # als er een game_code is en de game is gestart
        gameMenu = False
        game_menu()
    elif game_code != 0 and game_running == False: # als er een game_code is, maar de game is nog niet gestart
        waitMenu = False
        waiting_menu() # ga naar het wachtscherm
    else: # als niks waar is
        mainMenu = False
        menu() # laat het standaard menu zien
    
    if updatescherm == True:
        pygame.display.update() # update pygame scherm
        updateScherm(False)
pygame.quit() # sluit pygame af

# commando's hieronder die erbij horen om de game te sluiten
if game_code != 0: # als je in een game zat
    server.leaveGame(game_code, user_code) # dan wordt je dr uitgeknalt op de server