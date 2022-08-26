from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from tkinter import Frame
from tkinter import PhotoImage
import pygame
from pygame import mixer
import os

#---------------------------------------------------------------------
# Main Window
#---------------------------------------------------------------------
root = Tk()
root.geometry("250x330")
root.title("ALIMCO MP3 Player")
frame = Frame(root)
menu = Menu(frame)
root.config(menu=menu)
pygame.init()


root.current = 0
root.played = False
root.paused = True

#---------------------------------------------------------------------
# End
#---------------------------------------------------------------------

#---------------------------------------------------------------------
# Functions
#---------------------------------------------------------------------
def openFile():
    file = filedialog.askopenfilename()
    if file.endswith(".mp3"):
        if playlist.size() != 0:
            playlist.delete(playlist.curselection())
            playlist.insert(END, file)
        else:
            playlist.insert(END, file)
def openPlayList():
    file = filedialog.askdirectory()
    if file:
        os.chdir(file)
        songs = os.listdir(file)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)
def my_play():
    try:
        if root.played == False:
            play_func()

        elif root.played == True:
            pause_func()
        else:
            Message.set("Add music to play!!")
    except:
        Message.set("Add music to play!!")
def play_func():
    global song
    try:
        song = playlist.get(ACTIVE)
        mixer.music.load(song)
        for s in song:
            mixer.music.play()
            play_bt["image"] = play_img
            Message.set("Playing")
            root.played = True
            root.paused = False
            enume()
        # Note: This gives ValueError: invalid literal for int() with base 10: ' '
        for s in song:
            playlist.selection_set(int(s)-1)

    except:
        currentsong = playlist.curselection()
        song = playlist.get(currentsong)
        mixer.music.load(song)
        mixer.music.play()
    for ij in enumerate(playlist):
        print(ij)


    '''
    while mixer.music.get_endevent() == True:
        nextsong = playlist.curselection()
        nextsong = nextsong[0]+1
        if nextsong < playlist.size():
            playlist.selection_clear(0,END)
            playlist.activate(nextsong)
            playlist.selection_set(nextsong)
            temp = playlist.get(nextsong)
            mixer.music.load(temp)
            mixer.music.play()
            Message.set("Playing")
            root.paused = False
            play_bt["image"] = play_img
'''
def pause_func():
    if root.paused == True:
        mixer.music.unpause()
        root.paused = False
        root.played = True
        play_bt["image"] = play_img
        Message.set("Playing")
    else:
        mixer.music.pause()
        play_bt["image"] = pause_img
        root.paused = True
        Message.set("Paused")
        #if playlist.get(ACTIVE) == playlist.curselection():
def enume():
    for index, song in enumerate(playlist):
        print("Wqni!!!")
        print(song)
def stopsong():
    if mixer.music.get_busy() == True:
        play_bt["bg"] = "Gray"
        play_bt["text"] = "Start"
        Message.set("Stoped")
        mixer.music.fadeout(1000)
        root.played = False
        play_bt["image"] = pause_img
            #######
def previousbt():
    try:
        prev_song = playlist.curselection()
        prev_song = prev_song[0]-1
        if prev_song >= 0:
            playlist.selection_clear(0,END)
            playlist.activate(prev_song)
            playlist.selection_set(prev_song)
            if mixer.music.get_busy() == True:
                temp = playlist.get(prev_song)
                mixer.music.load(temp)
                mixer.music.play()
                root.paused = False
                play_bt["image"] = play_img
                Message.set("Playing")
    except:
        Message.set("Add music to play!!")
def nextbt():
    try:
        nextsong = playlist.curselection()
        nextsong = nextsong[0]+1
        if nextsong < playlist.size():
            playlist.selection_clear(0,END)
            playlist.activate(nextsong)
            playlist.selection_set(nextsong)
            if mixer.music.get_busy() == True:
                temp = playlist.get(nextsong)
                mixer.music.load(temp)
                mixer.music.play()
                Message.set("Playing")
                root.paused = False
                play_bt["image"] = play_img
    except:
        Message.set("Add music to play!!")

        #######
def loopsong():
    loop
def randomsong():
    randomsong
def change_vol(_=None):
    mixer.music.set_volume(vol.get())
#---------------------------------------------------------------------
# End
#---------------------------------------------------------------------


#---------------------------------------------------------------------
# ListBox
#---------------------------------------------------------------------
songFrame = LabelFrame(root, text="PlayList", bg="gray", relief=GROOVE)
songFrame.pack()

scroll_y = Scrollbar(songFrame, orient = VERTICAL)

playlist = Listbox(songFrame,yscrollcommand=scroll_y.set,selectbackground="Gold",selectmode=SINGLE,bg="Silver", fg="blue",bd=5,relief=GROOVE)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=playlist.yview)
playlist.pack(fill=BOTH)
#---------------------------------------------------------------------
# End
#---------------------------------------------------------------------
#---------------------------------------------------------------------
# Frame
#---------------------------------------------------------------------
frame0 = Frame(root)
frame1 = Frame(root)
frame2 = Frame(root)
#---------------------------------------------------------------------
# End
#---------------------------------------------------------------------

#---------------------------------------------------------------------
# b g
#---------------------------------------------------------------------
Message = StringVar()
mylabel1 = Label(frame1, textvariable=Message, bg="lightblue").pack()
Message.set("Welcome")
Msg = StringVar()
mylabel2 = Label(frame1, textvariable=Msg, bg="blue").pack()
Msg.set("Play Time")

frame1.pack()
#---------------------------------------------------------------------
# End
#---------------------------------------------------------------------

#---------------------------------------------------------------------
# my labels
#---------------------------------------------------------------------
subMenu = Menu(menu)
menu.add_cascade(label="Media", menu=subMenu)#Cascading Options on the ToolBar Such as: File Edit
subMenu.add_command(label="Open File", command=openFile)
subMenu.add_separator()
subMenu.add_command(label="Open PlayList", command=openPlayList)
subMenu.add_separator()
subMenu.add_command(label="exit", command=exit)

contactMenu = Menu(menu)
menu.add_cascade(label="Contact",menu=contactMenu)
contactMenu.add_command(label="Help")
contactMenu.add_command(label="Report Error")
contactMenu.add_command(label="Contribute")
#---------------------------------------------------------------------
# End
#---------------------------------------------------------------------

#---------------------------------------------------------------------
#my Buttons
#---------------------------------------------------------------------
next_img = PhotoImage(file='next.png')
prev_img = PhotoImage(file='previous.png')
play_img = PhotoImage(file='play.png')
pause_img = PhotoImage(file='pause.png')

prev_bt = Button(frame2, text="Prev",command=previousbt)

play_bt = Button(frame2, image=pause_img, bg="gray", command=my_play)

next_bt = Button(frame2, text="Next", command=nextbt)

prev_bt.grid(row=1, column=0)

play_bt.grid(row=1, column=1)

next_bt.grid(row=1, column=2)
frame2.pack()
#---------------------------------------------------------------------
#End
#---------------------------------------------------------------------

Button(root, text="Stop", command=stopsong).pack()
vol = Scale(root,from_=0,to=1,orient=HORIZONTAL,resolution=.1)
vol.pack()
playlist.bind('<Double-1>',my_play)

mainloop()
