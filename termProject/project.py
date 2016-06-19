import direct.directbase.DirectStart #initializes the base for the environment
from panda3d.core import * #import panda modules
from panda3d.core import CollisionTraverser,CollisionNode #used for collision detection
from panda3d.core import CollisionHandlerQueue,CollisionRay #used for collision detection
from panda3d.core import Filename,AmbientLight,DirectionalLight #used for lighting
from panda3d.core import PandaNode,NodePath,Camera,TextNode #used for setting the camera, setting nodes and displaying text respectively
from panda3d.core import Vec3,Vec4,BitMask32 #used for collision detection
from direct.gui.OnscreenText import OnscreenText #used for displaying text
from direct.actor.Actor import Actor #used for designating actors
from direct.showbase.DirectObject import DirectObject #used for creating direct objects (eg. both the World and the Pokemon class are direct objects)
from panda3d.core import WindowProperties #used for setting window properties
from direct.gui.OnscreenImage import OnscreenImage #used for displaying images
from direct.gui.DirectGui import * #used for graphical user interface components
import random, sys, os, math #used for random number generation, system operations, and math operations respectively
import pygame,sys,pygame.mixer #used for the main GUI in the game as well as for music
from pygame.locals import * #importing pygame modules for the GUI
from panda3d.ai import * #used for artificial intelligence for the Pokemon class
from pandac.PandaModules import TransparencyAttrib #Enables images to have transparent backgrounds
import urllib #used to write and read files
import inputbox #used to accept text input from the user (pygame), credit to Timothy Downs
import time #used for timing each catching session
import datetime #used to convert the time to a more visually pleasing format


speed = 0.75


def start(): #loads the GUI

    bif = "models/text/pokemonbg.jpg" #loads background images
    new_game_bg = "models/text/new_game_bg.jpg"
    pygame.init()
    screen = pygame.display.set_mode((1280,710),0,32) #designates the size of the screen
    background = pygame.image.load(bif).convert()
    myfont = pygame.font.Font("models/text/Pokemon.ttf", 72) #loads custom font
    myfont2 = pygame.font.SysFont("monospace", 50) #loads system font
    myfont3 = pygame.font.SysFont("monospace", 14) 
    label1 = myfont.render("THE SAFARI ZONE",1,(0,0,0)) #creates labels
    labelName = myfont3.render("Created by Dhruv Ranjan", 1, (0,0,0))
    label2 = myfont2.render("New Game",1,(0,0,0))
    label3 = myfont2.render("Load Game",1,(0,0,0))
    label4 = myfont2.render("Instructions",1,(0,0,0))
    screen.blit(background, (0,0)) #places background and labels onto the screen
    screen.blit(label1,(600,0))
    screen.blit(label2,(800,100))
    screen.blit(label3,(800,200))
    screen.blit(label4,(800,300))
    screen.blit(labelName,(800,80))
    pygame.display.update()

    while True:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            """if event.type == KEYDOWN:
                if event.key == K_n:
                    pygame.quit()
                    w = World()
                    run()"""
            if event.type == MOUSEBUTTONDOWN:
                (x,y) = pygame.mouse.get_pos()
                if x > 800 and x < 1040 and y > 100 and y < 147: #These numbers correspond to the x and y bounds of clickable text on the screen
                    newGame()
                elif x > 800 and x < 1070 and y > 200 and y < 247:
                    loadGame()
                elif x > 800 and x < 1156 and y > 300 and y < 347:
                    loadInstructions()

def loadInstructions(): #loads a picture which contains the controls and instructions for the game 

    pygame.init()
    instructions = "models/text/instructions.png"
    screen4 = pygame.display.set_mode((1280,800), 0, 32)
    background = pygame.image.load(instructions).convert()
    screen4.blit(background,(0,0))
    myfont2 = pygame.font.SysFont("monospace", 25)
    label1 = myfont2.render("Click to return to main Menu",1,(0,0,0))
    screen4.blit(label1,(10,650))
    pygame.display.update()

    while True:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                (x,y) = pygame.mouse.get_pos()
                if x > 10 and x < 429: #enables the user to go back to the start screen
                    if y > 655 and y < 674:
                        start()
                       

def loadGame(): #allows the user to load a previously existing game

    pygame.init()
    global PokemonScore
    PokemonScore = 0
    load_game_bg = "models/text/load_game_bg.jpg"
    screen3 = pygame.display.set_mode((1280,800), 0, 32)
    background = pygame.image.load(load_game_bg).convert()
    screen3.blit(background, (0,0))
    myfont = pygame.font.Font("models/text/Pokemon.ttf", 72)
    myfont2 = pygame.font.SysFont("monospace", 50)
    myfont3 = pygame.font.SysFont("monospace", 20)
    label1 = myfont.render("LOAD GAME",1,(0,0,0))
    screen3.blit(label1, (500,0))
    fileList = listFiles("saves")
    label2 = myfont2.render("Files: ",1,(0,0,0))
    screen3.blit(label2,(100,200))
    filestring = ""
    fileList2 = []
    for filename in fileList:
        filestring += filename[6:len(filename)-4] + ", " 
    label3 = myfont3.render(filestring,1,(0,0,0))
    screen3.blit(label3,(300,225))
    label4 = myfont3.render("Type file name from above in the box: ",1,(0,0,0))
    label5 = myfont3.render("Press enter to confirm",1,(0,0,0))
    label6 = myfont2.render("Click to start",1,(0,0,0))
    label7 = myfont2.render("File does not exist",1,(0,0,0))
    screen3.blit(label4, (90,385))
    screen3.blit(label5, (100,500))
    screen3.blit(label6, (500,600))
    answer = inputbox.ask(screen3,"") #accepts an input from the user. After the user presses "Enter", the variable answer will hold that input.
    
    pygame.display.update()

    while True:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if answer != "":
                    global name_of_file
                    global file_name
                    file_name = answer
                    name_of_file = "saves/" + answer + ".txt" #sets the name of the file, which is important for saving captured pokemon and setting high scores
                    if name_of_file not in fileList: #if the input is not the name of an existing game, the input is not accepted.
                        name_of_file = ""
                        loadGame()
                    else:
                        pygame.quit()
                        w = World()
                        run()
                        loadInstructions()

def listFiles(path): 
    if (os.path.isdir(path) == False):
        # base case:  not a folder, but a file, so return singleton list with its path
        return [path]
    else:
        # recursive case: it's a folder, return list of all paths
        files = [ ]
        for filename in os.listdir(path):
            files += listFiles(path + "/" + filename)
        return files
    
def newGame(): #allows the user to create a new game
    
    pygame.init()
    global PokemonScore
    PokemonScore = 0
    fileList = listFiles("saves")
    new_game_bg = "models/text/new_game_bg.jpg"
    screen2 = pygame.display.set_mode((1280,800),0,32)
    background = pygame.image.load(new_game_bg).convert()
    screen2.blit(background, (0,0))
    myfont = pygame.font.Font("models/text/Pokemon.ttf", 72)
    myfont2 = pygame.font.SysFont("monospace", 50)
    myfont3 = pygame.font.SysFont("monospace", 30)
    label1 = myfont.render("NEW GAME",1,(0,0,0))
    label2 = myfont2.render("Enter Name: ", 1,(0,0,0))
    label3 = myfont2.render("Click to start", 1,(0,0,0))
    label4 = myfont3.render("press enter to submit name", 1,(0,0,0))
    screen2.blit(label1, (500,100))
    screen2.blit(label2, (500,200))
    screen2.blit(label3, (500,500))
    screen2.blit(label4, (500,300))
    answer = inputbox.ask(screen2,"Name")
    pygame.display.update()

    while True:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if answer != "":
                    global name_of_file
                    global file_name
                    file_name = answer
                    name_of_file = "saves/" + answer + ".txt"
                    if name_of_file in fileList:
                        newGame()
                    else:
                        writeFile("saves/" + answer + ".txt", "") #creates a new file, where all of this users pokemon are stored
                        writeFile("scores/" + answer + ".txt", "") #creates a new file, where all of this users scores are stored
                        pygame.quit()
                        w = World() #creates the game world
                        run() #initiates the world
                
             
def addText(pos, msg): #allows easy display of text on the screen
    return OnscreenText(text=msg, style=1, fg=(1,1,1,1),
                        pos=(-1.3, pos), align=TextNode.ALeft, scale = .05)

def addMsg(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(1,1,1,1),
                        pos=(-1.3, pos), align=TextNode.ALeft, scale = .1)


class World(DirectObject):
    #initialize class attributes
    talkCount = 0
    map0 = 1
    map1 = 0
    pokeText = ""
    pokeNum = ""
    time = 0

    def __init__(self):

        pygame.init() #re-initialize pygame, to be used for sounds
        self.keyMap = {"left":0, "right":0, "forward":0, "backward":0, "cam-right":0, "cam-left":0, "fly":0} #used for movement
        self.pokeMap = {"bulbasaur":1, "venusaur":3, "charmander": 4, "charmeleon": 5, "charizard":6, "squirtle":7, "blastoise":9, "caterpie": 10,
                        "metapod":11,"butterfree":12,"diglett":50,"dugtrio":51,"golduck":55,"mankey":56,"primeape":57,"abra":63,"geodude":74,"magnemite":81,
                        "gastly":92,"haunter":93,"gengar":94,"marowak":105,"staryu":120,"scyther":123,"gyarados":130,"eevee":133,"vaporeon":134,"aerodactyl":142,
                        "dragonair":148,"dragonite":149,"mewtwo":150,"feraligatr":160,"umbreon":197,"murkrow":198,"misdreavus":200,"scizor":212,"teddiursa":216,
                        "ursaring":217,"suicune":245,"tyranitar":248,"lugia":249,"mudkip":258,"surskit":283,"sableye":302,"wailord":321,"tropius":357,"salamence":373,"metagross":376,
                        "latias":380,"latios":381,"groudon":383,"rayquaza":384,"deoxys":386,"piplup":393,"prinplup":394,"empoleon":395,"starly":396,"staravia":397,
                        "staraptor":398,"mismagius":429,"honchkrow":430,"gible":443,"garchomp":445,"munchlax":446,"magnezone":462,"leafeon":470,"dusknoir":477,"manaphy":490,
                        "darkrai":491,"shaymin":492,"snivy":495,"servine":496,"roggenrola":524,"boldore":525,"gigalith":526,"petilil":548,"lilligant":549,"klink":599,
                        "klang":600,"klinklang":601,"litwick":607,"lampent":608,"chandelure":609,"axew":610,"fraxure":611,"haxorus":612,"pawniard":624,"bisharp":625,
                        "hydreigon":635,"reshiram":643,"zekrom":644,"landorus":645 } #a dictionary mapping each Pokemon name to its corresponding picture, which is used in the Pokedex
        
        base.win.setClearColor(Vec4(0,0,0,1))
        
        props = WindowProperties()
        props.setCursorHidden(True) 
        base.win.requestProperties(props)
        
        self.throwSound = pygame.mixer.Sound("sounds/throw.wav") #this sound plays whenever the user throws a Pokeball
        pygame.mixer.music.load("sounds/bg.mp3") #initiates background music 
        pygame.mixer.music.play(-1) #sets the background music on an infinite loop
                                               
        self.timer = 0
        self.time1 = 0
        self.time2 = 0
        self.pokeballs = 0
        self.highscoresOn = 0
        self.loadInstructions()
        self.loadMap()
        self.loadPlayer()
        self.loadFloater()
        self.loadControls()
        self.loadCollisions()
        self.loadLights()

    def loadInstructions(self): #displays instructions on the screen for the user
        
        self.inst1 = addText(0.90, "[A]: Rotate Left")
        self.inst2 = addText(0.85, "[D]: Rotate Right")
        self.inst3 = addText(0.80, "[W]: Move Forward")
        self.inst4 = addText(0.75, "[Q]: Rotate Camera Left")
        self.inst5 = addText(0.70, "[E]: Rotate Camera Right")
        self.inst6 = addText(0.65, "[C]: Talk")
        self.inst7 = addText(0.60, "[Click]: Throw Pokeball")
        self.inst8 = addText(0.55, "[R]: Return to Base")
        self.inst9 = addText(0.50, "[F]: Display/Hide Pokedex")
        self.inst12 = addText(0.35, "[G]: Display/Hide High Scores")
        self.inst10 = addText(0.45, "[Left Control]: Next Pokedex entry")
        self.inst11 = addText(0.40, "[Left Alt]: Previous Pokedex entry")
        self.instTime = OnscreenText(text="Time: ", style = 1, fg = (1,1,1,1), pos = (0.8,0.9),scale = .1)
        self.instBalls = OnscreenText(text="Balls: ", style = 1, fg = (1,1,1,1), pos = (0.8,0.7),scale = .1)
        self.scoreText = OnscreenText(text="Score: ", style=1, fg = (1,1,1,1), pos=(0.8,0.5), scale = .1)
     
    def loadMap(self): #loads the first environment

        self.sky = loader.loadModel("models/blue_sky_sphere.egg")
        self.sky.reparentTo(render)
        self.sky.setPos(0,0,0)
        sky_texture = loader.loadTexture("models/sky.tif") #sets this texture to the model
        self.sky.setTexture(sky_texture,0)

        self.ground = loader.loadModel("models/Ground2.egg")
        self.ground.reparentTo(render)
        self.ground.setPos(0,0,0)
        
        self.environ = loader.loadModel("models/pond.egg")
        self.environ.reparentTo(render)
        self.environ.setPos(-20,-50,0)

        self.trainer = loader.loadModel("models/trainer.x") #loads the person you talk to to start the game
        self.trainer.reparentTo(render)
        self.trainer.setScale(.3)
        self.trainer.setPos(-20,-80,0)


    def loadPlayer(self):

        
        self.isThrown = 0
        startPos = (0,-100,0)
        self.box = loader.loadModel("models/gible.x") #loads the players model. It doesn't really matter which model this is, as the game is in first person, so the model is hidden anyway.
        self.box.reparentTo(render)
        self.box.setScale(3)
        self.box.setPos(startPos)

        if base.mouseWatcherNode.hasMouse(): #sets the Pokeball the user uses to catch Pokemon at the mouse position
            x = base.mouseWatcherNode.getMouseX()
            y = base.mouseWatcherNode.getMouseY()
            self.sphere.setPos(x-.1,y-.1,y-.1)
        self.sphere = loader.loadModel("models/sphere.egg")
        self.sphere.reparentTo(render2d) #renders the sphere in 2d, unlike the other 3D models, as the sphere is used as the mouse cursor
        self.pokeBallScale = .1
        self.sphere.setScale(self.pokeBallScale)
        texture = loader.loadTexture("models/pokeball2.jpg") #sets the pokeball texture to the sphere
        self.sphere.setTexture(texture,0)
        
        
    def loadFloater(self): #the floater is located at the camera, and is used for various calculations
        
        self.floater = NodePath(PandaNode("floater"))
        self.floater.reparentTo(render)

    def loadControls(self): #enables keyboard and mouse inputs
        
        self.accept("escape", sys.exit)
        self.accept("mouse1", self.throwSoundPlay)
        self.accept("a", self.setKey, ["left", 1])
        self.accept("d", self.setKey, ["right", 1])
        self.accept("w", self.setKey, ["forward", 1])
        self.accept("s", self.setKey, ["backward", 1])
        self.accept("q", self.setKey, ["cam-left", 1])
        self.accept("e", self.setKey, ["cam-right", 1])
        self.accept("c", self.talk)
        self.accept("r", self.returnToBase)
        self.accept("f", self.pokedex)
        self.accept("g", self.readScores)
        self.accept("a-up", self.setKey, ["left", 0])
        self.accept("d-up", self.setKey, ["right", 0])
        self.accept("w-up", self.setKey, ["forward", 0])
        self.accept("s-up", self.setKey, ["backward", 0])
        self.accept("q-up", self.setKey, ["cam-left", 0])
        self.accept("e-up", self.setKey, ["cam-right", 0])
        self.accept("6", self.map6)
        self.accept("5", self.map5)
        self.accept("4", self.map2)
        self.accept("3", self.map3)
        self.accept("2", self.map4)
        self.accept("1", self.map1)
        self.accept("0", self.map0)

        taskMgr.add(self.move,"moveTask") #adds the function self.move to the task manager

        base.disableMouse() #disables panda3d special mouse controls (ie. mouse wheel to zoom etc.)
        base.camera.setPos(self.box.getX(),self.box.getY()+10,2) #sets the camera at the player model
        self.pokedexOn = 0

    @classmethod 
    def getTalkCount(cls): #gets the number of times the user has talked to the trainer
        return World.talkCount

    def throwSoundPlay(self): #plays the throw sounds whenever the user clicks

        self.throwSound.play()
        x = base.mouseWatcherNode.getMouseX()
        y = base.mouseWatcherNode.getMouseY()
        if World.map1 == 1:
            self.pokeballs -= 1 #if the user is in a safari zone map, the number of available pokeballs goes down by 1
    
    def map0(self):
        
        if World.talkCount == 3: #if the user has talked to the trainer 3 times and selected map0
            self.map.destroy() #removes the map image
            self.environ.removeNode() #removes the current environment
            self.timer = 0
            self.time1 = time.time() #used to calculate how long the user has before the game ends
            
            global PokemonScore
            PokemonScore = 0 #holds the users score
            
            pygame.mixer.music.load("sounds/bg.mp3") #loads the music for this particular map
            pygame.mixer.music.play(-1)
            
            World.map1 = 0 #map1 is equal to 0 when the user is not in a safari zone map, and is equal to 1 if they are in one
            World.map0 = 1
            World.talkCount = 0

            self.environ = loader.loadModel("models/pond.egg")
            self.ground = loader.loadModel("models/Ground2.egg")
            self.environ.reparentTo(render)
            self.ground.reparentTo(render)
            self.ground.setPos(0,0,0)
            self.environ.setPos(0,0,0) #sets the position of the environment
            self.box.setPos(0,-100,0) #sets the position of the player
            self.trainer.setPos(-20,-80,0) #sets the position of the trainer

    def map1(self):

        if World.talkCount == 3:
            if World.map1 != 1:
                self.pokeballs = 50 #the user starts with 50 pokeballs
                self.timer = 0
                self.time1 = time.time()
            pygame.mixer.music.load("sounds/bg1.mp3")
            pygame.mixer.music.play(-1)
            self.map.destroy()
            self.environ.removeNode()
            self.environ = loader.loadModel("models/world.egg")
            self.environ.reparentTo(render)
            self.environ.setPos(self.box.getX(), self.box.getY(), self.box.getZ())
            self.ground.removeNode()
            self.trainer.setZ(self.environ.getZ()-1)
            World.map1 = 1
            World.map0 = 0
            World.talkCount = 0
            minimum, maximum = self.environ.getTightBounds()
            size = maximum - minimum
            self.generatePokemon(15,1)

    def map2(self):

        if World.talkCount == 3:
            if World.map1 != 1:
                self.pokeballs = 50
                self.timer = 0
                self.time1 = time.time()
            pygame.mixer.music.load("sounds/bg2.mp3")
            pygame.mixer.music.play(-1)
            self.map.destroy()
            self.environ.removeNode()
            self.environ = loader.loadModel("models/moonsurface.egg")
            self.environ.reparentTo(render)
            self.environ.setPos(0,0,0)
            self.environ.setScale(.125)
            self.ground.removeNode()
            self.trainer.setZ(self.environ.getZ())
            World.map1 = 1
            World.map0 = 0
            World.talkCount = 0
            minimum, maximum = self.environ.getTightBounds()
            size = maximum - minimum
            self.generatePokemon(15,2)


    def map3(self):

        if World.talkCount == 3:
            if World.map1 != 1:
                self.pokeballs = 50
                self.timer = 0
                self.time1 = time.time()
            pygame.mixer.music.load("sounds/bg3.mp3")
            pygame.mixer.music.play(-1)
            self.map.destroy()
            self.environ.removeNode()
            self.environ = loader.loadModel("models/CityTerrain.egg")
            self.environ.reparentTo(render)
            self.environ.setPos(0,0,0)
            self.ground.removeNode()
            self.trainer.setZ(self.environ.getZ())
            World.map1 = 1
            World.map0 = 0
            World.talkCount = 0
            minimum, maximum = self.environ.getTightBounds()
            size = maximum - minimum

            self.generatePokemon(25,3)

    def map4(self):

        if World.talkCount == 3:
            if World.map1 != 1:
                self.pokeballs = 50
                self.timer = 0
                self.time1 = time.time()
            pygame.mixer.music.load("sounds/bg5.mp3")
            pygame.mixer.music.play(-1)
            self.map.destroy()
            self.environ.removeNode()
            self.environ = loader.loadModel("models/HauntedHouse.egg")
            self.environ.reparentTo(render)
            self.environ.setPos(self.box.getX(), self.box.getY(), self.box.getZ())
            self.ground.removeNode()
            self.trainer.setPos(15,-90,98)
            self.environ.setScale(3)
            World.map1 = 1
            World.map0 = 0
            World.talkCount = 0
            minimum, maximum = self.environ.getTightBounds()
            size = maximum - minimum
            self.generatePokemon(15,4)

    def map5(self):

        if World.talkCount == 3:
            if World.map1 != 1:
                self.pokeballs = 50
                self.timer = 0
                self.time1 = time.time()
            pygame.mixer.music.load("sounds/bg4.mp3")
            pygame.mixer.music.play(-1)
            self.map.destroy()
            self.environ.removeNode()
            self.environ = loader.loadModel("models/Ground2.egg")
            self.environ.reparentTo(render)
            self.environ.setPos(self.box.getX(), self.box.getY(), self.box.getZ())
            self.ground.removeNode()
            self.trainer.setZ(self.box.getZ())
            World.map1 = 1
            World.map0 = 0
            World.talkCount = 0
            minimum, maximum = self.environ.getTightBounds()
            size = maximum - minimum
            self.generatePokemon(30,5)

    def map6(self):

        if World.talkCount == 3:
            if World.map1 != 1:
                self.pokeballs = 50
                self.timer = 0
                self.time1 = time.time()
            pygame.mixer.music.load("sounds/bg6.mp3")
            pygame.mixer.music.play(-1)
            self.map.destroy()
            self.environ.removeNode()
            self.environ = loader.loadModel("models/MtFuji.egg")
            self.environ.reparentTo(render)
            self.environ.setScale(1.5)
            self.environ.setPos(self.box.getX(), self.box.getY(), self.box.getZ()- 609)
            self.ground.removeNode()
            World.map1 = 1
            World.map0 = 0
            World.talkCount = 0
            self.trainer.setPos(self.box.getX(), self.box.getY(), self.box.getZ())
            minimum, maximum = self.environ.getTightBounds()
            size = maximum - minimum
            self.generatePokemon(15,6)

    def generatePokemon(self,num,mapNum): #creates Pokemon by calling the Pokemon class

        for i in xrange(num):
            Pokemon(mapNum)
        
 
    def talk(self): #lets the user speak to the trainer if he's near enough

        if math.fabs(self.trainer.getX() - self.box.getX()) < 20 and math.fabs(self.trainer.getY() - self.box.getY()) < 20 and math.fabs(self.trainer.getZ() - self.box.getZ()) < 20:
            if self.getTalkCount() == 0:
                self.msg1 = addMsg(-.1, "Hello! Welcome to the Safari Zone.")
                World.talkCount += 1
            elif self.getTalkCount() == 1:
                self.msg1.destroy()
                self.msg1 = addMsg(-.1, "Which area would you like to Travel to?")
                World.talkCount += 1
            elif self.getTalkCount() == 2:
                self.msg1.destroy()
                self.map = OnscreenImage(image="models/text/map.png", pos=(0,0,0))
                World.talkCount += 1
            elif self.getTalkCount() == 3:
                self.map.destroy()
                World.talkCount = 0

    def pokedex(self): #lets the user see the Pokemon they've caught so far, as well as how many 

        if self.highscoresOn == 0:
            if self.pokedexOn == 0:
                self.pokedexOn = 1
                self.pokedex = OnscreenImage(image="models/text/pokedex.png", pos=(0,0,0)) #loads the pokedex image
                self.pokedex.setTransparency(True)
                World.pokeText = OnscreenText(text="", style=1, pos=(0,-.5), scale = .1)
                World.pokeNum = OnscreenText(text="", style=1, pos=(0,-.7), scale = .1)
                self.pokeImage = OnscreenImage(image= "models/Battlers/0.png", pos=(0,.5,.5),scale=.2) #loads the initial blank image
                self.pokeImage.setTransparency(True)
                self.pokeString = readFile(name_of_file) #reads the users file containing all Pokemon captured and returns them as a string
                self.pokeArray = []
                self.currentPokemonNum = 0
                for char in xrange(len(self.pokeString)): #removes the spaces in the Pokemon string and places the Pokemon names in an array
                    if self.pokeString[char] == " ":
                        nameString = ""
                        for letters in xrange(char+1,len(self.pokeString)):
                            if self.pokeString[letters] != " ":
                                nameString += self.pokeString[letters]
                            else:
                                self.pokeArray.append(nameString)
                                break
                            if letters == len(self.pokeString)-1:
                                self.pokeArray.append(nameString)
                                break
                self.pokeArray.sort() #sorts the array, so the Pokemon are displayed alphabetically
                self.pokeSet = set(self.pokeArray)
                self.pokeArray2 = list(self.pokeSet)
                self.pokeArray2.sort()
                self.accept("lcontrol", self.readPokemon) #go to the next Pokemon
                self.accept("lalt", self.readPokemonBack) #go to the previous Pokemon
            else:
                self.pokedex.destroy() #removes the pokedex
                World.pokeText.setText("")
                World.pokeNum.setText("")
                self.pokeImage.destroy()
                self.pokedexOn= 0

    def readPokemon(self): #displays the current Pokemon by checking the Pokemons name in a dictionary mapping the name to its picture, and then displays the picture
        if self.pokedexOn == 1:
            if self.currentPokemonNum < len(self.pokeArray2):
                self.currentPokemon = self.pokeArray2[self.currentPokemonNum]
            if self.currentPokemon in self.pokeMap and self.currentPokemonNum < len(self.pokeArray2):
                self.currentPokemonNum += 1
                if self.currentPokemonNum >= len(self.pokeArray2):
                    self.currentPokemonNum = 0
                picNum = self.pokeMap[self.currentPokemon]
                num = self.pokeArray.count(self.currentPokemon)
                self.pokeImage.setImage("models/Battlers/"+str(picNum)+".png")
                World.pokeText.setText(self.currentPokemon)
                World.pokeNum.setText(str(num))

    def readPokemonBack(self): #same as the previous function, but in reverse
        if self.pokedexOn == 1:
            if self.currentPokemonNum >= 0:
                self.currentPokemon = self.pokeArray2[self.currentPokemonNum]
            if self.currentPokemon in self.pokeMap and self.currentPokemonNum >= 0:
                self.currentPokemonNum -= 1
                if self.currentPokemonNum < 0:
                    self.currentPokemonNum = len(self.pokeArray2)-1
                picNum = self.pokeMap[self.currentPokemon]
                num = self.pokeArray.count(self.currentPokemon)
                self.pokeImage.setImage("models/Battlers/"+str(picNum)+".png")
                World.pokeText.setText(self.currentPokemon)
                World.pokeNum.setText(str(num))

    def writeScore(self): #writes the users score to their own score file after they complete a game, and to the universal high scores file if they have one of the top 3 scores out of all users
        
        global file_name
        global PokemonScore
        fileName = "scores/" + file_name + ".txt"
        score = " " + str(PokemonScore)
        scoreString = readFile(fileName)
        fileContents = scoreString + score
        writeFile(fileName, fileContents) #writes the score to the users own score file 
        highscoreString = readFile("highscores/highscores.txt")
        highscoreList = []
        score2 = ""
        score3 = ""
        for char in xrange(len(highscoreString)): #removes spaces from the highscore string
            if highscoreString[char] == " ":
                nameString = ""
                for letters in xrange(char+1,len(highscoreString)):
                    if highscoreString[letters] != " ":
                        nameString += highscoreString[letters]
                    else:
                        highscoreList.append(nameString)
                        break
                    if letters == len(highscoreString)-1:
                        highscoreList.append(nameString)
                        break
        highscoreListNoNames = []
        for score in xrange(len(highscoreList)): #removes the names from the highscore list, so the scores can be compared
            for letter in xrange(len(highscoreList[score])):
                if highscoreList[score][letter] == ":":
                    scoreString = ""
                    for letters in xrange(letter+1,len(highscoreList[score])):
                        scoreString += highscoreList[score][letters]
                    highscoreListNoNames.append(scoreString)
                    break
        highscoreListNoNames.sort() #sorts the scores, so that they are displayed from highest to lowest
        if PokemonScore < int(highscoreListNoNames[0]) and PokemonScore < int(highscoreListNoNames[1]) and PokemonScore > int(highscoreListNoNames[2]): #compares and places the scores, and removes the lowest
            highscoreList[2] = file_name + ":" + str(PokemonScore)
        if PokemonScore < int(highscoreListNoNames[0]) and PokemonScore > int(highscoreListNoNames[1]):
            highscoreList[2] = highscoreList[1]
            highscoreList[1] = file_name + ":" + str(PokemonScore)
        if PokemonScore > int(highscoreListNoNames[0]):
            highscoreList[2] = highscoreList[1]
            highscoreList[1] = highscoreList[0]
            highscoreList[0] = file_name + ":" + str(PokemonScore)
        finalString = ""
        for score in highscoreList:
            finalString += " " + score
        writeFile("highscores/highscores.txt", "")
        writeFile("highscores/highscores.txt", finalString) #adds the final string of high scores the the high scores file
                   

    def readScores(self): #displays the high scores and the users personal best score
        if self.pokedexOn == 0:
            if self.highscoresOn == 0:
                highscoreString = readFile("highscores/highscores.txt")
                highscoreList = [] 
                for char in xrange(len(highscoreString)): #removes spaces from the high score string
                    if highscoreString[char] == " ":
                        nameString = ""
                        for letters in xrange(char+1,len(highscoreString)):
                            if highscoreString[letters] != " ":
                                nameString += highscoreString[letters]
                            else:
                                highscoreList.append(nameString)
                                break
                            if letters == len(highscoreString)-1:
                                highscoreList.append(nameString)
                                break
                global file_name
                fileName = "scores/" + file_name + ".txt"
                selfScoreString = readFile(fileName)
                selfScoreList = []
                for char in xrange(len(selfScoreString)): #removes the spaces from the selfscore string
                    if selfScoreString[char] == " ":
                        nameString = ""
                        for letters in xrange(char+1,len(selfScoreString)):
                            if selfScoreString[letters] != " ":
                                nameString += selfScoreString[letters]
                            else:
                                selfScoreList.append(nameString)
                                break
                            if letters == len(selfScoreString)-1:
                                selfScoreList.append(nameString)
                                break
                selfScoreList.sort()
                self.highscoresOn = 1
                self.pokedex = OnscreenImage(image="models/text/pokedex.png", pos=(0,0,0))
                self.pokedex.setTransparency(True)
                self.selfScoreLabel = OnscreenText(text="Personal Best", style=1, pos=(0,.5), scale = .1) #displays the users personal best score
                self.selfScore = OnscreenText(text=str(selfScoreList[len(selfScoreList)-1]), style = 1, pos = (0,.4), scale = .1)
                self.highScoreLabel = OnscreenText(text="HIGHSCORES", style=1, pos=(0,-.35), scale = .1)
                self.highScore1 = OnscreenText(text=highscoreList[0], style=1, pos=(0,-.5), scale = .1) #displays the top 3 high scores
                self.highScore2 = OnscreenText(text=highscoreList[1], style=1, pos=(0,-.6), scale = .1)  
                self.highScore3 = OnscreenText(text=highscoreList[2], style=1, pos=(0,-.7), scale = .1)
            else:
                self.selfScoreLabel.setText("")
                self.highScoreLabel.setText("")
                self.highScore1.setText("")
                self.highScore2.setText("")
                self.highScore3.setText("")
                self.selfScore.setText("")
                self.pokedex.destroy()
                self.highscoresOn = 0
        
            
    def returnToBase(self): #this function is called whenever the time runs out, the user runs out of pokeballs, or they press [r] to return to base, to return the user to the first environment
        if World.map1 == 1:
            self.map.destroy()
            self.environ.removeNode()
            self.writeScore()
            global PokemonScore
            PokemonScore = 0
            pygame.mixer.music.load("sounds/bg.mp3")
            pygame.mixer.music.play(-1)
            
            World.map1 = 0
            World.map0 = 1
            World.talkCount = 0

            self.environ = loader.loadModel("models/pond.egg")
            self.ground = loader.loadModel("models/Ground2.egg")
            self.environ.reparentTo(render)
            self.ground.reparentTo(render)
            self.box.setPos(0,-100,0)
            self.ground.setPos(0,0,0)
            self.environ.setPos(0,0,0)
            self.trainer.setPos(-20,-80,1)

    def loadCollisions(self): #Allows collisions to be detected
        
        self.cTrav = CollisionTraverser() #initiates a collision traverser
        
        self.boxGroundRay = CollisionRay()
        self.boxGroundRay.setOrigin(0,0,1000)
        self.boxGroundRay.setDirection(0,0,-1)
        self.boxGroundCol = CollisionNode('boxRay')
        self.boxGroundCol.addSolid(self.boxGroundRay)
        self.boxGroundCol.setFromCollideMask(BitMask32.bit(0))
        self.boxGroundCol.setIntoCollideMask(BitMask32.allOff())
        self.boxGroundColNp = self.box.attachNewNode(self.boxGroundCol)
        self.boxGroundHandler = CollisionHandlerQueue()
        self.cTrav.addCollider(self.boxGroundColNp, self.boxGroundHandler)

        self.camGroundRay = CollisionRay()
        self.camGroundRay.setOrigin(0,0,1000)
        self.camGroundRay.setDirection(0,0,-1)
        self.camGroundCol = CollisionNode('camRay')
        self.camGroundCol.addSolid(self.camGroundRay)
        self.camGroundCol.setFromCollideMask(BitMask32.bit(0))
        self.camGroundCol.setIntoCollideMask(BitMask32.allOff())
        self.camGroundColNp = base.camera.attachNewNode(self.camGroundCol)
        self.camGroundHandler = CollisionHandlerQueue()
        self.cTrav.addCollider(self.camGroundColNp, self.camGroundHandler)
        

    def loadLights(self): #loads lighting. From the panda3d website. 
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(.3, .3, .3, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(Vec3(-5, -5, -5))
        directionalLight.setColor(Vec4(1, 1, 1, 1))
        directionalLight.setSpecularColor(Vec4(1, 1, 1, 1))
        render.setLight(render.attachNewNode(ambientLight))
        render.setLight(render.attachNewNode(directionalLight))
            
    def setKey(self,key,value): #used in movement from keyboard input
        self.keyMap[key] = value
            
    def move(self,task): #allows movement, and checks for game completion.
        
        self.box.hide() #hides the player model, as the game is in first person
        if World.map1 == 1:
            self.timer += 1
            self.time2 = time.time()
            self.instTime.setText("Time: " + str(datetime.timedelta(seconds=300 - (self.time2 - self.time1)))) #displays the time left until the end of the game
            self.instBalls.setText("Balls: " + str(self.pokeballs)) #displays the number of pokeballs left until the user runs out
            if self.pokeballs <= 0: #if the user runs out of pokeballs, the game ends
                self.returnToBase()
                self.instTime.setText("Out of pokeballs!")
                self.timer = 0
            if self.time2 - self.time1 >= 300: #if the user runs out of time (5 minutes), the game ends
                self.returnToBase()
                self.instTime.setText("Out of time!")
                self.timer = 0
                self.time2 = 0
        else:
            self.timer = 0
            
        base.camera.lookAt(self.box) #makes the camera look at the player model
        startpos = self.box.getPos()
        if not (self.trainer.getX() - self.box.getX() < 20 and self.trainer.getY() - self.box.getY() < 20 and self.trainer.getZ() - self.box.getZ() < 20) and World.talkCount != 0:
            self.msg1.destroy() #if the user is talking to the trainer and then starts to move away, the text on the screen is removed, and the map is removed
            if World.talkCount == 3:
                self.map.destroy()
        if base.mouseWatcherNode.hasMouse(): #sets the pokeball image at the mouse position
            x = base.mouseWatcherNode.getMouseX()
            y = base.mouseWatcherNode.getMouseY()
            self.sphere.setPos(x-.1,y-.1,y-.1)
        #used for moving the player model according to keyboard inputs
        if self.keyMap["cam-left"]!=0:
            base.camera.setX(base.camera, -20 * globalClock.getDt())
        if self.keyMap["cam-right"]!=0:
            base.camera.setX(base.camera, +20 * globalClock.getDt())
        if self.keyMap["left"]!=0:
            self.box.setH(self.box.getH() + 300 * globalClock.getDt())
            base.camera.setX(base.camera, +20 * globalClock.getDt())
            self.box.setY(self.box, -25 * globalClock.getDt())
        if self.keyMap["right"]!=0:
            self.box.setH(self.box.getH() - 300 * globalClock.getDt())
            base.camera.setX(base.camera, -20 * globalClock.getDt())
            self.box.setY(self.box, -25 * globalClock.getDt())
        if self.keyMap["forward"]!=0:
            self.box.setY(self.box, -25 * globalClock.getDt())
        if self.keyMap["backward"]!=0:
            self.box.setZ(self.box, +25 * globalClock.getDt())
        camvec = self.box.getPos() - base.camera.getPos()
        camvec.setZ(0)
        camdist = camvec.length()
        camvec.normalize()
        if (camdist > 10.0):
            base.camera.setPos(base.camera.getPos() + camvec*(camdist-10))
            camdist = 10.0
        if (camdist < 5.0):
            base.camera.setPos(base.camera.getPos() - camvec*(5-camdist))
            camdist = 5.0

        self.cTrav.traverse(render)
        #sets the users Z coordinates when walking over uneven terrain
        #additionally, this code makes the player model unable to walk through obstacles
        entries = []
        for i in range(self.boxGroundHandler.getNumEntries()):
            entry = self.boxGroundHandler.getEntry(i)
            entries.append(entry)
        entries.sort(lambda x,y: cmp(y.getSurfacePoint(render).getZ(),
                                     x.getSurfacePoint(render).getZ()))
        if (len(entries)>0) and (entries[0].getIntoNode().getName() == "terrain"):
            self.box.setZ(entries[0].getSurfacePoint(render).getZ())
        else:
            self.box.setPos(startpos)
        
        entries = []
        for i in range(self.camGroundHandler.getNumEntries()):
            entry = self.camGroundHandler.getEntry(i)
            entries.append(entry)
        entries.sort(lambda x,y: cmp(y.getSurfacePoint(render).getZ(),
                                     x.getSurfacePoint(render).getZ()))
        if (len(entries)>0) and (entries[0].getIntoNode().getName() == "terrain"):
            base.camera.setZ(entries[0].getSurfacePoint(render).getZ()+1.0)
        if (base.camera.getZ() < self.box.getZ() + 2.0):
            base.camera.setZ(self.box.getZ() + 2.0)
        
        self.floater.setPos(self.box.getPos())
        self.floater.setZ(self.box.getZ() + 2.0)
        base.camera.lookAt(self.floater)

        return task.cont

class Pokemon(DirectObject): #this class allows Pokemon models to be loaded and placed in an environment
    #load class attributes
    isCaught = 0
    msgText = ""
    score = 0
    scoreText = ""

    
    def __init__(self,mapNum):

        self.isCaught = 0
        self.ballCount = 50
        Pokemon.scoreText = OnscreenText(text="", style=1, fg = (1,1,1,1), pos=(1.1,.5), scale = .1) #initializes the on screen score display
        Pokemon.msgText = addMsg(-.5, "")
        self.mapNum = mapNum
        self.AIworld = AIWorld(render) #initializes AI
        self.timer = 0
        self.loadModel()
        self.loadCollisions()
        self.timer2 = 0
        self.time1 = time.time()
        self.time2 = 0
        self.throwSound = pygame.mixer.Sound("sounds/throw.wav")
        removePokemon = 0


    def loadForest(self): #creates a randomly generated forest for the forest map

        self.treeX = random.randint(-500,500)
        self.treeY = random.randint(-500,500)
        self.tree2X = random.randint(-500,500)
        self.tree2Y = random.randint(-500,500)
        self.tree3X = random.randint(-500,500)
        self.tree3Y = random.randint(-500,500)
        self.tree4X = random.randint(-500,500)
        self.tree4Y = random.randint(-500,500)
        self.tree = loader.loadModel("models/GroomedTree.egg")
        self.tree.reparentTo(render)
        self.tree.setScale(15)
        self.tree.setPos(self.treeX, self.treeY, 0)
        self.tree2 = loader.loadModel("models/bush.egg")
        self.tree2.reparentTo(render)
        self.tree2.setScale(1)
        self.tree2.setPos(self.tree2X, self.tree2Y, 0)
        self.tree3 = loader.loadModel("models/bush2.egg")
        self.tree3.reparentTo(render)
        self.tree3.setScale(8)
        self.tree3.setPos(self.tree3X, self.tree3Y, 0)
        self.tree4 = loader.loadModel("models/sapling.egg")
        self.tree4.reparentTo(render)
        self.tree4.setScale(5)
        self.tree4.setPos(self.tree4X, self.tree4Y, 0)

    def loadCity(self): #creates a randomly generated city for the city map

        self.treeX = random.randint(-700,700)
        self.treeY = random.randint(-700,700)
        self.tree2X = random.randint(-700,700)
        self.tree2Y = random.randint(-700,700)
        self.tree3X = random.randint(-700,700)
        self.tree3Y = random.randint(-700,700)
        self.tree4X = random.randint(-700,700)
        self.tree4Y = random.randint(-700,700)
        self.tree = loader.loadModel("models/BuildingCluster1.egg")
        self.tree.reparentTo(render)
        self.tree.setScale(1)
        self.tree.setPos(self.treeX, self.treeY, 0)
        self.tree2 = loader.loadModel("models/BuildingCluster2.egg")
        self.tree2.reparentTo(render)
        self.tree2.setScale(1)
        self.tree2.setPos(self.tree2X, self.tree2Y, 0)
        self.tree3 = loader.loadModel("models/BuildingCluster3.egg")
        self.tree3.reparentTo(render)
        self.tree3.setScale(1)
        self.tree3.setPos(self.tree3X, self.tree3Y, 0)
        self.tree4 = loader.loadModel("models/BuildingCluster5.egg")
        self.tree4.reparentTo(render)
        self.tree4.setScale(1)
        self.tree4.setPos(self.tree4X, self.tree4Y, 0)


    def loadMap3(self): #loads all the Pokemon models and textures for the city map

        self.coordX = random.randint(-500,500) #sets the bounds for the X coordinate spawn points of the Pokemon
        self.coordY = random.randint(-500,500) #sets the bounds for the Y coordinate spawn points of the Pokemon
        self.pokeH = random.randint(0,20000) #sets the starting orientation of the Pokemon
        pokecheck = random.randint(1,100) #creates a random number which corresponds to a particular pokemon
        isnegx = random.randint(0,1) #determines if the Pokemon spawns in a positive or negative X position
        isnegy = random.randint(0,1) #determines if the Pokemon spawns in a positive or negative Y position
        self.loadCity() #loads the building for the city
        #The following code loads Pokemon models and textures depending on the "pokecheck" variable
        if pokecheck > 0 and pokecheck <= 15:
            self.poke = loader.loadModel("models/magnemite.x") #loads the model
            self.poke.reparentTo(render) #renders the model
            self.poke.setScale(1) #sets the scale of the model
            self.poke.setTag("name", "magnemite") #sets the name of the model
            self.poke.setTag("catchP", "90") #sets the catch percentage of the model
        elif pokecheck > 15 and pokecheck <= 30: 
            self.poke = loader.loadModel("models/starly.x") 
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/MukkuruDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "starly")
            self.poke.setTag("catchP", "90")
        elif pokecheck > 30 and pokecheck <= 40: 
            self.poke = loader.loadModel("models/staravia.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/MukubirdDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "staravia")
            self.poke.setTag("catchP", "70")
        elif pokecheck > 40 and pokecheck <= 45: 
            self.poke = loader.loadModel("models/staraptor.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/MukuhawkDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "staraptor")
            self.poke.setTag("catchP", "40")
        elif pokecheck == 46:
            self.poke = loader.loadModel("models/deoxys.x")
            self.poke.reparentTo(render)
            self.poke.setScale(.5)
            poke_texture = loader.loadTexture("models/Deoxys000Dh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "deoxys")
            self.poke.setTag("catchP", "10")
        elif pokecheck > 50 and pokecheck <= 60:
            self.poke = loader.loadModel("models/munchlax.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/GonbeDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "munchlax")
            self.poke.setTag("catchP", "90")
        elif pokecheck > 47 and pokecheck <=50:
            self.poke = loader.loadModel("models/magnezone.x")
            self.poke.reparentTo(render)
            self.poke.setScale(.5)
            poke_texture = loader.loadTexture("models/JibacoilDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "magnezone")
            self.poke.setTag("catchP", "30")
        elif pokecheck > 60 and pokecheck <= 70:
            self.poke = loader.loadModel("models/Abra.x")
            self.poke.reparentTo(render)
            self.poke.setScale(.5)
            self.poke.setTag("name", "abra")
            self.poke.setTag("catchP", "60")
        elif pokecheck > 70 and pokecheck <= 75:
            self.poke = loader.loadModel("models/eevee.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/EievuiDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "eevee")
            self.poke.setTag("catchP", "50")
        elif pokecheck > 75 and pokecheck <= 80:
            self.poke = loader.loadModel("models/klink.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/GiaruNl.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "klink")
            self.poke.setTag("catchP", "50")
        elif pokecheck > 80 and pokecheck <= 85:
            self.poke = loader.loadModel("models/klang.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/GigiaruNl.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "klang")
            self.poke.setTag("catchP", "40")
        elif pokecheck > 85 and pokecheck <= 90:
            self.poke = loader.loadModel("models/klinklang.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/GigigiaruNl.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "klinklang")
            self.poke.setTag("catchP", "30")
        elif pokecheck > 90 and pokecheck <= 95:
            self.poke = loader.loadModel("models/pawniard.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/KomatanaBodyNl.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "pawniard")
            self.poke.setTag("catchP", "50")
        elif pokecheck > 95 and pokecheck <= 100:
            self.poke = loader.loadModel("models/bisharp.x")
            self.poke.reparentTo(render)
            self.poke.setScale(.5)
            poke_texture = loader.loadTexture("models/KirikizanBodyNl.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "bisharp")
            self.poke.setTag("catchP", "30")
        elif pokecheck == 47:
            self.poke = loader.loadModel("models/mewtwo.x")
            self.poke.reparentTo(render)
            self.poke.setScale(.4)
            self.poke.setTag("catchP", "5")
            self.poke.setTag("name", "mewtwo")

        self.poke.setTag("pickable", "true") #states that the pokemon can be captured
        self.poke.setPos(self.coordX,self.coordY,0) #sets the randomly generated position of the pokemon
        self.poke.setH(self.pokeH * globalClock.getDt()) #sets the randomly generated orientation of the Pokemon
        self.AIchar = AICharacter("wanderer", self.poke,100,.05,25) #makes the Pokemon randomly wander about
        self.AIchar = AICharacter("fleer", self.poke,100,.05,50) #makes the Pokemon speed up if the player gets too close
        self.AIworld.addAiChar(self.AIchar)
        self.AIbehaviors = self.AIchar.getAiBehaviors()
        self.AIbehaviors.flee(base.camera, 25, 25,1) #here, base.camera is synonomous to the player, as the camera follows the player around
        self.AIbehaviors.wander(2,0,500,.1)

    def loadMap5(self): #creates the forest map similarly to the previous one 

        self.coordX = random.randint(-500,500)
        self.coordY = random.randint(-500,500)
        self.pokeH = random.randint(0,20000)
        pokecheck = random.randint(1,100)
        isnegx = random.randint(0,1)
        isnegy = random.randint(0,1)
        self.loadForest()
        

        if pokecheck > 0 and pokecheck <= 10 or (pokecheck > 90 and pokecheck <= 100):
            self.poke = loader.loadModel("models/caterpie.x")
            self.poke.reparentTo(render)
            self.poke.setScale(2)
            self.poke.setTag("name", "caterpie")
            self.poke.setTag("catchP", "90")
        elif pokecheck > 10 and pokecheck <= 20:
            self.poke = loader.loadModel("models/Transel.x")
            self.poke.reparentTo(render)
            self.poke.setScale(2)
            self.poke.setTag("name", "metapod")
            self.poke.setTag("catchP", "90")
        elif pokecheck > 20 and pokecheck <= 30:
            self.poke = loader.loadModel("models/petilil.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/ChurineBodyNl.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "petilil")
            self.poke.setTag("catchP", "90")
        elif pokecheck > 30 and pokecheck <= 35:
            self.poke = loader.loadModel("models/lilligant.x")
            self.poke.reparentTo(render)
            self.poke.setScale(.5)
            poke_texture = loader.loadTexture("models/lilligant.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "lilligant")
            self.poke.setTag("catchP", "50")
        elif pokecheck > 35 and pokecheck <= 40:
            self.poke = loader.loadModel("models/snivy.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/TsutarjaBodyNl.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "snivy")
            self.poke.setTag("catchP", "90")
        elif pokecheck > 40 and pokecheck <= 45:
            self.poke = loader.loadModel("models/servine.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/JanovyBodyNl.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "servine")
            self.poke.setTag("catchP", "50")
        elif pokecheck > 45 and pokecheck <= 50:
            self.poke = loader.loadModel("models/Scyther.x")
            self.poke.reparentTo(render)
            self.poke.setScale(10)
            poke_texture = loader.loadTexture("models/StrikeDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "scyther")
            self.poke.setTag("catchP", "40")
        elif pokecheck > 50 and pokecheck <= 52:
            self.poke = loader.loadModel("models/leafeon.x")
            self.poke.reparentTo(render)
            self.poke.setScale(.5)
            poke_texture = loader.loadTexture("models/LeafiaDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "leafeon")
            self.poke.setTag("catchP", "30")
        elif pokecheck > 55 and pokecheck <= 70:
            self.poke = loader.loadModel("models/Bulbasaur.x")
            self.poke.reparentTo(render)
            self.poke.setScale(.5)
            self.poke.setTag("name", "bulbasaur")
            self.poke.setTag("catchP", "80")
        elif pokecheck > 70 and pokecheck <= 75:
            self.poke = loader.loadModel("models/Venusaur.x")
            self.poke.reparentTo(render)
            self.poke.setScale(.5)
            poke_texture = loader.loadTexture("models/FushigibanaDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "venusaur")
            self.poke.setTag("catchP", "30")
        elif pokecheck > 75 and pokecheck <= 80:
            self.poke = loader.loadModel("models/butterfree.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/ButterfreeDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "butterfree")
            self.poke.setTag("catchP", "50")
        elif pokecheck > 52 and pokecheck <= 54:
            self.poke = loader.loadModel("models/scizor.x")
            self.poke.reparentTo(render)
            self.poke.setScale(.5)
            poke_texture = loader.loadTexture("models/HassamDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "scizor")
            self.poke.setTag("catchP", "20")
        elif pokecheck > 80 and pokecheck <= 90:
            self.poke = loader.loadModel("models/tropius.x")
            self.poke.reparentTo(render)
            self.poke.setScale(.5)
            poke_texture = loader.loadTexture("models/TropiusDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "tropius")
            self.poke.setTag("catchP", "40")
        elif pokecheck == 55:
            self.poke = loader.loadModel("models/shaymin.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/Shaymin001Dh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "shaymin")
            self.poke.setTag("catchP", "10")

        self.poke.setTag("pickable", "true")
        self.poke.setPos(self.coordX,self.coordY,0)
        self.poke.setH(self.pokeH * globalClock.getDt())
        self.AIchar = AICharacter("wanderer", self.poke,100,.05,25)
        self.AIchar = AICharacter("fleer", self.poke,100,.05,80)
        self.AIworld.addAiChar(self.AIchar)
        self.AIbehaviors = self.AIchar.getAiBehaviors()
        self.AIbehaviors.flee(base.camera, 25, 25,1)
        self.AIbehaviors.wander(2,0,500,.1)

        

    def loadMap4(self): #creates the haunted house map

        self.coordX = random.randint(-200,200)
        self.coordY = random.randint(-230,230)
        self.pokeH = random.randint(0,20000)
        pokecheck = random.randint(1,100)
        isnegx = random.randint(0,1)
        isnegy = random.randint(0,1)
        
        if pokecheck > 0 and pokecheck <= 15:
            self.poke = loader.loadModel("models/gastly.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/GhosDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "gastly")
            self.poke.setTag("catchP", "90")
        elif pokecheck > 15 and pokecheck <= 25:
            self.poke = loader.loadModel("models/haunter.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/GhostDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "haunter")
            self.poke.setTag("catchP", "60")
        elif pokecheck > 25 and pokecheck <= 30:
            self.poke = loader.loadModel("models/gengar.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/GangarDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "gengar")
            self.poke.setTag("catchP", "30")
        elif pokecheck > 30 and pokecheck <= 35:
            self.poke = loader.loadModel("models/umbreon.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/BlackyDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "umbreon")
            self.poke.setTag("catchP", "30")
        elif pokecheck > 35 and pokecheck <= 45:
            self.poke = loader.loadModel("models/murkrow.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/YamikarasuDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "murkrow")
            self.poke.setTag("catchP", "80")
        elif pokecheck > 45 and pokecheck <= 55:
            self.poke = loader.loadModel("models/misdreavus.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/MumaDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "misdreavus")
            self.poke.setTag("catchP", "75")
        elif pokecheck > 55 and pokecheck <= 65:
            self.poke = loader.loadModel("models/sableye.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/YamiramiDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "sableye")
            self.poke.setTag("catchP", "75")
        elif pokecheck > 65 and pokecheck <= 70:
            self.poke = loader.loadModel("models/mismagius.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/MumargiDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "mismagius")
            self.poke.setTag("catchP", "30")
        elif pokecheck > 70 and pokecheck <= 75:
            self.poke = loader.loadModel("models/honchkrow.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/DongkarasuDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "honchkrow")
            self.poke.setTag("catchP", "30")
        elif pokecheck > 95 and pokecheck <= 99:
            self.poke = loader.loadModel("models/dusknoir.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/YonoirDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "dusknoir")
            self.poke.setTag("catchP", "20")
        elif pokecheck == 100:
            self.poke = loader.loadModel("models/darkrai.x")
            self.poke.reparentTo(render)
            self.poke.setScale(.1)
            poke_texture = loader.loadTexture("models/DarkraiBossBodyNl.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "darkrai")
            self.poke.setTag("catchP", "5")
        elif pokecheck > 75 and pokecheck <= 85:
            self.poke = loader.loadModel("models/litwick.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/HitomoshiBodyNl.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "litwick")
            self.poke.setTag("catchP", "90")
        elif pokecheck > 85 and pokecheck <= 91:
            self.poke = loader.loadModel("models/Lampent.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            self.poke.setTag("name", "lampent")
            self.poke.setTag("catchP", "60")
        elif pokecheck > 91 and pokecheck <= 95:
            self.poke = loader.loadModel("models/Chandelure.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            self.poke.setTag("name", "chandelure")
            self.poke.setTag("catchP", "25")


        self.poke.setTag("pickable", "true")
        self.poke.setPos(self.coordX,self.coordY,0)
        self.poke.setH(self.pokeH * globalClock.getDt())
        self.AIchar = AICharacter("wanderer", self.poke,100,.05,25)
        self.AIchar = AICharacter("fleer", self.poke,100,.05,50)
        self.AIworld.addAiChar(self.AIchar)
        self.AIbehaviors = self.AIchar.getAiBehaviors()
        self.AIbehaviors.flee(base.camera, 25, 25,1)
        self.AIbehaviors.wander(2,0,500,.1)

    def loadMap1(self): #creates the beach map

        self.coordX = random.randint(-500,400)
        self.coordY = random.randint(-300,650)
        self.pokeH = random.randint(0,20000)
        pokecheck = random.randint(1,100)
        isnegx = random.randint(0,1)
        isnegy = random.randint(0,1)

        if pokecheck > 0 and pokecheck <= 10:
            self.poke = loader.loadModel("models/mudkip.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/mudkip.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "90")
            self.poke.setTag("name", "mudkip")
        elif pokecheck > 10 and pokecheck <= 20:
            self.poke = loader.loadModel("models/staryu.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/HitodemanBodyNl.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "80")
            self.poke.setTag("name", "staryu")
        elif pokecheck > 20 and pokecheck <= 30:
            self.poke = loader.loadModel("models/surskit.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            ts = TextureStage("ts")
            poke_texture = loader.loadTexture("models/AmetamaBodyNl.png")
            poke_texture_2 = loader.loadTexture("models/AmetamaEyeNl.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "90")
            self.poke.setTag("name", "surskit")
        
        elif pokecheck > 60 and pokecheck <= 62:
            self.poke = loader.loadModel("models/wailord.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/WhalohDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "20")
            self.poke.setTag("name", "wailord")
        elif pokecheck > 30 and pokecheck <= 35:
            self.poke = loader.loadModel("models/vaporeon.x")
            self.poke.reparentTo(render)
            self.poke.setScale(20)
            self.poke.setTag("catchP", "30")
            self.poke.setTag("name", "vaporeon")
        elif pokecheck > 35 and pokecheck <= 40:
            self.poke = loader.loadModel("models/golduck.x")
            self.poke.reparentTo(render)
            self.poke.setScale(.4)
            self.poke.setTag("catchP", "50")
            self.poke.setTag("name", "golduck")
        elif pokecheck > 62 and pokecheck <= 66:
            self.poke = loader.loadModel("models/gyarados.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/GyaradosDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "25")
            self.poke.setTag("name", "gyarados")
        elif pokecheck > 66 and pokecheck <= 71:
            self.poke = loader.loadModel("models/feraligatr.x")
            self.poke.reparentTo(render)
            self.poke.setScale(.5)
            poke_texture = loader.loadTexture("models/OrdileDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "40")
            self.poke.setTag("name", "feraligatr")
        elif pokecheck > 91 and pokecheck <= 93:
            self.poke = loader.loadModel("models/suicune.x")
            self.poke.reparentTo(render)
            self.poke.setScale(.5)
            poke_texture = loader.loadTexture("models/SuicuneDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "10")
            self.poke.setTag("name", "suicune")
        elif pokecheck > 40 and pokecheck <= 50:
            self.poke = loader.loadModel("models/piplup.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/PochamaDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "piplup")
            self.poke.setTag("catchP", "90")
        elif pokecheck > 71 and pokecheck <= 81:
            self.poke = loader.loadModel("models/prinplup.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/PottaishiDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "50")
            self.poke.setTag("name", "prinplup")
        elif pokecheck > 81 and pokecheck <= 86:
            self.poke = loader.loadModel("models/empoleon.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/EmperteDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "30")
            self.poke.setTag("name", "empoleon")
        elif pokecheck > 93 and pokecheck <= 95:
            self.poke = loader.loadModel("models/manaphy.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/ManaphyDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("name", "manaphy")
            self.poke.setTag("catchP", "10")
        elif pokecheck > 50 and pokecheck <= 60 or (pokecheck > 95 and pokecheck <= 99):
            self.poke = loader.loadModel("models/squirtle.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/ZenigameDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "90")
            self.poke.setTag("name", "squirtle")
        elif pokecheck > 86 and pokecheck <= 91:
            self.poke = loader.loadModel("models/Kamex.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/KamexDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "35")
            self.poke.setTag("name", "blastoise")
        elif pokecheck == 100:
            self.poke = loader.loadModel("models/lugia.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/Lugia_B.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "5")
            self.poke.setTag("name", "lugia")
            
        self.poke.setTag("pickable", "true")
        self.poke.setPos(self.coordX,self.coordY,0)
        self.poke.setH(self.pokeH * globalClock.getDt())
        self.AIchar = AICharacter("wanderer", self.poke,100,.05,25)
        self.AIchar = AICharacter("fleer", self.poke,100,.05,50)
        self.AIworld.addAiChar(self.AIchar)
        self.AIbehaviors = self.AIchar.getAiBehaviors()
        self.AIbehaviors.flee(base.camera, 25, 25,1)
        self.AIbehaviors.wander(2,0,500,.1)

    def loadMap2(self): #creates the desert map

        self.coordX = random.randint(-750,750)
        self.coordY = random.randint(-750,750)
        self.pokeH = random.randint(0,20000)
        pokecheck = random.randint(1,100)
        isnegx = random.randint(0,1)
        isnegy = random.randint(0,1)

        if pokecheck > 0 and pokecheck <= 10:
            self.poke = loader.loadModel("models/gible.x")
            self.poke.reparentTo(render)
            self.poke.setScale(10)
            self.poke.setTag("catchP", "80")
            self.poke.setTag("name", "gible")
        elif pokecheck > 20 and pokecheck <= 25:
            self.poke = loader.loadModel("models/Dugtrio.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            self.poke.setTag("catchP", "40")
            self.poke.setTag("name", "dugtrio")
        elif pokecheck > 10 and pokecheck <= 20:
            self.poke = loader.loadModel("models/Diglett.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            self.poke.setTag("catchP", "90")
            self.poke.setTag("name", "diglett")
        elif pokecheck > 25 and pokecheck <= 35:
            self.poke = loader.loadModel("models/Mankey.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            self.poke.setTag("catchP", "70")
            self.poke.setTag("name", "mankey")
        elif pokecheck > 35 and pokecheck <= 40:
            self.poke = loader.loadModel("models/Primeape.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            self.poke.setTag("catchP", "40")
            self.poke.setTag("name", "primeape")
        elif pokecheck > 40 and pokecheck <= 50:
            self.poke = loader.loadModel("models/Geodude.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/IsitsubuteDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "90")
            self.poke.setTag("name", "geodude")
        elif pokecheck > 50 and pokecheck <= 55:
            self.poke = loader.loadModel("models/marowak.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/GaragaraDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "50")
            self.poke.setTag("name", "marowak")
        elif pokecheck > 90 and pokecheck <= 92:
            self.poke = loader.loadModel("models/aerodactyl.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/PteraDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "25")
            self.poke.setTag("name", "aerodactyl")
        elif pokecheck > 55 and pokecheck <= 65:
            self.poke = loader.loadModel("models/teddiursa.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/HimegumaDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "90")
            self.poke.setTag("name", "teddiursa")
        elif pokecheck > 65 and pokecheck <= 70:
            self.poke = loader.loadModel("models/ursaring.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/RingumaDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "40")
            self.poke.setTag("name", "ursaring")
        elif pokecheck == 93:
            self.poke = loader.loadModel("models/tyranitar.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/BangirasDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "15")
            self.poke.setTag("name", "tyranitar")
        elif pokecheck == 94:
            self.poke = loader.loadModel("models/Groudon.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/GroudonDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "5")
            self.poke.setTag("name", "groudon")
        elif pokecheck > 94 and pokecheck <= 96:
            self.poke = loader.loadModel("models/metagross.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/MetagrossDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "15")
            self.poke.setTag("name", "metagross")
        elif pokecheck > 96 and pokecheck <= 98:
            self.poke = loader.loadModel("models/garchomp.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/GaburiasDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "15")
            self.poke.setTag("name", "garchomp")
        elif pokecheck > 70 and pokecheck <= 80:
            self.poke = loader.loadModel("models/roggenrola.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/DangoroBodyNl.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "90")
            self.poke.setTag("name", "roggenrola")
        elif pokecheck > 75 and pokecheck <= 85:
            self.poke = loader.loadModel("models/boldore.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/GantleBodyNl.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "60")
            self.poke.setTag("name", "boldore")
        elif pokecheck > 85 and pokecheck <= 90:
            self.poke = loader.loadModel("models/gigalith.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/GigaiathBodyNl.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "30")
            self.poke.setTag("name", "gigalith")
        elif pokecheck > 98 and pokecheck <= 100:
            self.poke = loader.loadModel("models/landorus.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/LandLosNl.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "10")
            self.poke.setTag("name", "landorus")

        self.poke.setTag("pickable", "true")
        self.poke.setPos(self.coordX,self.coordY,0)
        self.poke.setH(self.pokeH * globalClock.getDt())
        self.AIchar = AICharacter("wanderer", self.poke,100,.05,25)
        self.AIchar = AICharacter("fleer", self.poke,100,.05,50)
        self.AIworld.addAiChar(self.AIchar)
        self.AIbehaviors = self.AIchar.getAiBehaviors()
        self.AIbehaviors.flee(base.camera, 25, 25,1)
        self.AIbehaviors.wander(2,0,750,.1)

    def loadMap6(self): #creates the mountain map

        self.coordX = random.randint(-400,400)
        self.coordY = random.randint(-500,500)
        self.pokeH = random.randint(0,20000)
        pokecheck = random.randint(1,100)
        isnegx = random.randint(0,1)
        isnegy = random.randint(0,1)

        if pokecheck > 0 and pokecheck <= 15:
            self.poke = loader.loadModel("models/axew.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/KibagoBodyNl.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "60")
            self.poke.setTag("name", "axew")
        elif pokecheck > 15 and pokecheck <= 25:
            self.poke = loader.loadModel("models/fraxure.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/OnondBodyNl.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "30")
            self.poke.setTag("name", "fraxure")
        elif pokecheck > 25 and pokecheck <= 30:
            self.poke = loader.loadModel("models/haxorus.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/OnonokusBodyNl.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "15")
            self.poke.setTag("name", "haxorus")
        elif pokecheck > 30 and pokecheck <= 35:
            self.poke = loader.loadModel("models/hydreigon.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/SazandoraNl.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "15")
            self.poke.setTag("name", "hydreigon")
        elif pokecheck > 35 and pokecheck <= 40:
            self.poke = loader.loadModel("models/charizard.x")
            self.poke.reparentTo(render)
            self.poke.setScale(.5)
            self.poke.setTag("catchP", "20")
            self.poke.setTag("name", "charizard")
        elif pokecheck > 85 and pokecheck <= 88:
            self.poke = loader.loadModel("models/rayquaza.x")
            self.poke.reparentTo(render)
            self.poke.setScale(25)
            self.poke.setTag("catchP", "5")
            self.poke.setTag("name", "rayquaza")
        elif pokecheck > 88 and pokecheck <= 91:
            self.poke = loader.loadModel("models/Reshiram.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/ReshiramBodyNl.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "5")
            self.poke.setTag("name", "reshiram")
        elif pokecheck > 91 and pokecheck <= 94:
            self.poke = loader.loadModel("models/Zekrom.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/ZekromBodyNl.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "5")
            self.poke.setTag("name", "zekrom")
        elif pokecheck > 40 and pokecheck <= 45:
            self.poke = loader.loadModel("models/salamence.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/BohmanderDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "15")
            self.poke.setTag("name", "salamence")
        elif pokecheck > 45 and pokecheck <= 50:
            self.poke = loader.loadModel("models/dragonite.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/KairyuDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "15")
            self.poke.setTag("name", "dragonite")
        elif pokecheck > 94 and pokecheck <= 97:
            self.poke = loader.loadModel("models/latias.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/LatiasDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "5")
            self.poke.setTag("name", "latias")
        elif pokecheck > 97 and pokecheck <= 100:
            self.poke = loader.loadModel("models/latios.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/LatiosDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "5")
            self.poke.setTag("name", "latios")
        elif pokecheck > 50 and pokecheck <= 60:
            self.poke = loader.loadModel("models/dragonaire.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            self.poke.setTag("catchP", "30")
            self.poke.setTag("name", "dragonair")
        elif pokecheck > 60 and pokecheck <= 75:
            self.poke = loader.loadModel("models/Hitokage.x")
            self.poke.reparentTo(render)
            self.poke.setScale(1)
            poke_texture = loader.loadTexture("models/HitokageDh.png")
            self.poke.setTexture(poke_texture,0)
            self.poke.setTag("catchP", "80")
            self.poke.setTag("name", "charmander")
        elif pokecheck > 75 and pokecheck <= 85:
            self.poke = loader.loadModel("models/charmeleon.x")
            self.poke.reparentTo(render)
            self.poke.setScale(.03)
            self.poke.setTag("catchP", "60")
            self.poke.setTag("name", "charmeleon")
        
        self.poke.setTag("pickable", "true")
        self.poke.setPos(self.coordX,self.coordY,0)
        self.poke.setH(self.pokeH * globalClock.getDt())
        self.AIchar = AICharacter("wanderer", self.poke,100,.05,25)
        self.AIchar = AICharacter("fleer", self.poke,100,.05,50)
        self.AIworld.addAiChar(self.AIchar)
        self.AIbehaviors = self.AIchar.getAiBehaviors()
        self.AIbehaviors.flee(base.camera, 25, 25,1)
        self.AIbehaviors.wander(2,0,750,.1)
    
    def loadModel(self): #loads a particular map based on the users previous keyboard input

        if self.mapNum == 1:
            self.loadMap1()
        elif self.mapNum == 2:
            self.loadMap2()
        elif self.mapNum == 3:
            self.loadMap3()
        elif self.mapNum == 4:
            self.loadMap4()
        elif self.mapNum == 5:
            self.loadMap5()
        elif self.mapNum == 6:
            self.loadMap6()

    def loadCollisions(self): #loads collisions, similar to how it was done for the player, except these collisions are loaded for each Pokemon 
        
        self.pTrav = CollisionTraverser()

        self.pokeGroundRay = CollisionRay()
        self.pokeGroundRay.setOrigin(0,0,1000)
        self.pokeGroundRay.setDirection(0,0,-1)
        self.pokeGroundCol = CollisionNode('pokeRay')
        self.pokeGroundCol.addSolid(self.pokeGroundRay)
        self.pokeGroundCol.setFromCollideMask(BitMask32.bit(0))
        self.pokeGroundCol.setIntoCollideMask(BitMask32.allOff())
        self.pokeGroundColNp = self.poke.attachNewNode(self.pokeGroundCol)
        self.pokeGroundHandler = CollisionHandlerQueue()
        self.pTrav.addCollider(self.pokeGroundColNp, self.pokeGroundHandler)
        #the following collision traverser is used for detecting mouse clicks on 3D objects. The basics of this were taken from the panda3d website.
        self.picker= CollisionTraverser() 
        self.queue=CollisionHandlerQueue() 
        self.pickerNode=CollisionNode('mouseRay') 
        self.pickerNP=camera.attachNewNode(self.pickerNode) 
        self.pickerNode.setFromCollideMask(GeomNode.getDefaultCollideMask())
        self.pickerNode.setIntoCollideMask(BitMask32.allOff())
        self.pickerRay=CollisionRay() 
        self.pickerNode.addSolid(self.pickerRay) 
        self.picker.addCollider(self.pickerNP, self.queue)

        #this holds the object that has been picked 
        self.pickedObj=None 
        
        self.accept('mouse1', self.attemptCatch) #if the user clicks, the Pokemon capture code is run

        self.accept("0", self.removeAll) #if any of the following numbers are pressed, the map is cleared
        self.accept("1", self.removeAll)
        self.accept("2", self.removeAll)
        self.accept("3", self.removeAll)
        self.accept("4", self.removeAll)
        self.accept("5", self.removeAll)
        self.accept("6", self.removeAll)
        
        self.accept("r", self.removeAll)

        taskMgr.add(self.move,"moveTask") #adds Pokemon movement to the task manager

    def getObjectHit(self, mpos): #this code is used to determine if a Pokemon is clicked on. Is mainly from the panda3d website, with some minor adjustments to fit this particular situation.
      
      self.pickedObj=None #resets the picked object
      self.pickerRay.setFromLens(base.camNode, mpos.getX()-.2,mpos.getY()-.2) #extends the mouse collision ray from the mouse position, adjusted to the Pokeball position
      self.picker.traverse(render)
      if self.queue.getNumEntries() > 0 and self.isCaught == 0: #self.queue holds all the collisions
         self.queue.sortEntries() #sorts the entries, so the nearest entries are first
         self.pickedObj=self.queue.getEntry(0).getIntoNodePath()
         self.entry = self.queue.getEntry(0)
         self.entry.getSurfacePoint(self.pickedObj)
         parent=self.pickedObj.getParent()
         self.pickedObj=None
         while parent != render: #only accept the collision if the parent isnt "render", otherwise collisions with terrain would also count
            if parent.getTag('pickable')=='true': #only accept the collision if the Pokemon is "pickable"
               self.queue.clearEntries() #remove all other entries from the queue, so only one Pokemon can be caught per click
               self.pickedObj=parent
               return parent
            else: 
               parent=parent.getParent()
      return None 

    def getPickedObj(self): 
        return self.pickedObj 

    def catch(self):
        
        b = self.getObjectHit( base.mouseWatcherNode.getMouse())
        mpos = base.mouseWatcherNode.getMouse()
        a = self.pickedObj
        if a != None: #if there was actually a collision
            #only accepts collisions if the player model is close enough to the Pokemon
            if self.poke.getTag("pickable") == "true" and Pokemon.isCaught == 0 and math.fabs(base.camera.getY() - self.poke.getY()) < 100 and math.fabs(base.camera.getX() - self.poke.getX()) < 100: 
                
                self.catchP = self.poke.getTag("catchP")
                self.num = random.randint(1,100)
               
                if self.num <= int(self.catchP): #if the randomly generated number is less than the number corresponding to the catch probability, the Pokemon is caught
                    
                    self.poke.setTag("pickable", "false") #the pokemon is caught, so it can no longer be caught
                    self.pokeCaughtName = self.poke.getTag("name")
                    Pokemon.isCaught = 1
                    Pokemon.msgText.setText("You caught a " + self.poke.getTag("name") + "!") #displays the name of the caught Pokemon
                    global PokemonScore
                    if int(self.catchP) > 10: #sets the Pokemon score depending on the caught Pokemons rarity
                        PokemonScore += 100 - int(self.catchP)
                    elif int(self.catchP) <= 10 and int(self.catchP) > 5:
                        PokemonScore += (100 - int(self.catchP)) * 3
                    else:
                        PokemonScore += (100 - int(self.catchP)) * 5
                        
                    Pokemon.scoreText.setText(str(PokemonScore)) #displays the users current score 
                    self.saveCatch() #saves the name of the caught pokemon in the users save file

                else:
                    msgNum = random.randint(0,1) #if the Pokemon is not caught, one of the following 2 messages is displayed
                    if msgNum == 0:
                        Pokemon.msgText.setText("The Pokeball bounced off!")
                    elif msgNum == 1:
                        Pokemon.msgText.setText("The Pokemon dodged the Pokeball!")
        else:
            Pokemon.msgText.setText("Missed!") #if the Pokemon is not caught, the following message is displayed
          
    def attemptCatch(self): #attempts to catch a Pokemon

        self.ballCount -= 1 #decreases the pokeballs left by 1
        if Pokemon.isCaught == 0: #if a Pokemon has not already been caught attempt to catch one
            self.catch()
            
    def saveCatch(self): #saves the name of the caught Pokemon in the users save file

        name = self.pokeCaughtName
        contents1 = readFile(name_of_file) + " " + name
        writeFile(name_of_file, contents1)

    def removeAll(self): #removes all Pokemon and environments (eg. buildings and trees) if the game ends

        try: #try and excepts are needed because not all maps use extra environments
            self.tree.removeNode()
            self.tree2.removeNode()
            self.tree3.removeNode()
            self.tree4.removeNode()
        except:
            pass
        try:
            self.poke.setTag("pickable", "false")
            self.ignoreAll()
        except:
            pass
        Pokemon.msgText.setText("")
        Pokemon.scoreText.setText("")
        
        
        
    def move(self,task): #allows movement for all Pokemon
        
        if self.poke.getTag("pickable") == "true": #the Pokemon can only move if it's still pickable

            self.pokeCaughtName = 0
            startpos = self.poke.getPos()
            self.timer += 1
            self.timer2 += 1
            self.time2 = time.time()
            if self.time2 - self.time1 > 300: #if the user runs out of time, remove all Pokemon
                self.removeAll()
                
            if self.ballCount <= 0: #if the user runs out of Pokeballs, remove all Pokemon
                self.timer2 = 10000
                self.time1 = 0
                self.removeAll()

            if self.timer >= 100: #allows a Pokemon to be caught again
                
                Pokemon.isCaught = 0

            self.AIworld.update() #updates AI movements
            
            self.pTrav.traverse(render)
            #sets terrain traversal and collision detection for Pokemon, similar to how it was done for the player model
            entries = []
            for i in range(self.pokeGroundHandler.getNumEntries()):
                entry = self.pokeGroundHandler.getEntry(i)
                entries.append(entry)
            entries.sort(lambda x,y: cmp(y.getSurfacePoint(render).getZ(),
                                         x.getSurfacePoint(render).getZ()))
            if (len(entries)>0) and (entries[0].getIntoNode().getName() == "terrain"):
                self.poke.setZ(entries[0].getSurfacePoint(render).getZ())
            else:
                self.poke.setPos(startpos)

        else:
            self.poke.removeNode() #if a pokemon is not pickable, it is removed 
            try:
                self.tree.removeNode()
                self.tree2.removeNode()
                self.tree3.removeNode()
                self.tree4.removeNode()
            except:
                pass
        
            self.ignoreAll()
            
            
        return task.cont

def readFile(filename, mode="rt"): 
    
    # rt stands for "read text"
    fin = contents = None
    try:
        fin = open(filename, mode)
        contents = fin.read()
    finally:
        if (fin != None): fin.close()
    return contents

def writeFile(filename, contents, mode="wt"):
    
    # wt stands for "write text"
    fout = None
    try:
        fout = open(filename, mode)
        fout.write(contents)
    finally:
        if (fout != None): fout.close()
    return True

start() #start the GUI
run() #run panda3d 


