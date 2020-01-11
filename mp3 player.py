import os # get songs and directories
from tkinter.filedialog import askdirectory # for selecting song directory
import pygame #for playing music
from mutagen.id3 import ID3, TIT2 #for tagging meta data to our songs
from tkinter import * #for UI
from tkinter import filedialog

root=Tk() #Makes empty window
root.minsize(300,300) #sets size to 300x300 wide, change as wanted

listofsongs = []
realnames=[]

v=StringVar() #UI Label that updates as the song changes or updates
songlabel= Label(root, textvariable=v,width=35)
index = 0


def ChooseDir():
    
    directory=askdirectory()
    os.chdir(directory)# os.chdir changes the current working directory to the given path

    for files in os.listdir(directory): #this for loop cycles through all files in a given directory
                                       #os.listdir lists all the files in a given directory
        if files.endswith(".mp3"):#file is added to realdir ONLY if it ends with ".mp3"

            realdir = os.path.realpath(files)
            audio = ID3(realdir)#Loads the meta data of the song into the audio variable.(A dictionary)
            realnames.append(files)
            #audio contains meta data of song,
                                                    #The title of the song is stored as "TIT2" in the meta data
            listofsongs.append(files)#adds the song file to the listofsongs list

    pygame.mixer.init() #initializes pygame
    pygame.mixer.music.load(listofsongs[0])#Loads the first song in listofsongs
    pygame.mixer.music.play()
ChooseDir()
vol=1

def updatelabel():
    global index #If you do not use global, new index variable will be defined
    global songname
    v.set(realnames[index]) # set my StringVar to the real name
    #return songname
def pausesong(event):
    pygame.mixer.music.pause()
    updatelabel()

def volumeUp(event):
     global vol
     if vol>1:
         print ("max volume is 1")
     vol=vol+0.1
     
     pygame.mixer.music.set_volume(vol)
    
    
def volumeDown(event):
     global vol
     vol=vol-0.1
     if vol<0:
         print ("min volume is 0")
     
     pygame.mixer.music.set_volume(vol)
    
    
def unpausesong(event):
    pygame.mixer.music.unpause()
    updatelabel()
def nextsong(event):
    global index # get index from globals
    index+=1#increment index
    pygame.mixer.music.load(listofsongs[index])#load next song from list
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
   global index
   index-=1
   pygame.mixer.music.load(listofsongs[index])
   pygame.mixer.music.play()
   updatelabel()

def stopsong(event):
    pygame.mixer.music.stop()#stops song currently playing
    v.set("")#sets label to empty
    #return songname


#BACKEND COMPLETE--------------------------------

label=Label(root,text="Music Player")# Sets the heading
label.pack()#packs it inside root window

listbox=Listbox(root)
listbox.pack()


#listofsongs.reverse()
realnames.reverse()

for items in realnames:
    listbox.insert(0,items)
realnames.reverse()
#listofsongs.reverse()

#Creates buttons
volup=Button(root,text="Volume Up")
volup.place(x=0,y=0)

voldown=Button(text="Volume Down")
voldown.place(x=0,y=26)


pausebutton=Button(root,text='Pause Song')
pausebutton.pack()

unpausebutton=Button(root,text='Unpause Song')
unpausebutton.pack()

nextbutton=Button(root,text='Next Song')
nextbutton.pack()

previousbutton=Button(root,text='Previous Song')
previousbutton.pack()

stopbutton=Button(root,text='Stop Music')
stopbutton.pack()

#Binds these buttons to the functions I've written above
volup.bind("<Button-1>",volumeUp)
voldown.bind("<Button-1>",volumeDown)
pausebutton.bind("<Button-1>",pausesong)
unpausebutton.bind("<Button-1>",unpausesong)
nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)

songlabel.pack()
root.mainloop()







    
