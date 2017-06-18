"""
Project
Sam Teerlinck
1NMCT4
"""

"""
Imports
"""
import easygui		#easygui library for the interface
import glob			#to read file location
import pygame		#to play the music

"""
Variables
"""
#initialize mixer and load the songs
pygame.mixer.init()
playing = 0
songlist = glob.glob('/home/pi/Music/*.mp3')

#variables for the choicebox
lst_message = "Choose a song."
lst_title = "Music Player"
lst_choices = glob.glob('/home/pi/Music/*.mp3')
#remove path and extension
for index in range(len(lst_choices)):
	lst_choices[index] = lst_choices[index].replace('/home/pi/Music/','')
	lst_choices[index] = lst_choices[index].replace('.mp3','')

#variables for the buttonbox
btn_message = ""
btn_title = "Playing Song"
btn_choices = ["Different song","Pause/Play","Quit"]

"""
MusicPlayer loop
"""
#automatically start loop first time
while True:
	#open choicebox with songs
	lst_choice = easygui.choicebox(lst_message, lst_title, lst_choices)
	
	#check if your choice is a song
	for index in range(len(lst_choices)):
		if lst_choice == lst_choices[index]:
			#load song and make it ready to play
			pygame.mixer.music.load(songlist[index])
			#play the song
			pygame.mixer.music.play()
			#set integer that tells us the song is now playing
			playing = 1
			#message that tells us the song is playing
			btn_message = "Now playing " + lst_choices[index] + "."
			while True:
				#buttonbox that opens when song plays
				btn_choice = easygui.buttonbox(btn_message, btn_title, btn_choices)
				#if pause is pressed, check if song is playing or not and then go back to buttonbox
				if btn_choice == "Pause/Play":
					if playing == 1:
						pygame.mixer.music.pause()
						playing = 0
						continue
					elif playing == 0:
						pygame.mixer.music.unpause()
						playing = 1
						continue
				else:
					break

	#if different song is pressed, go back to choicebox (restart loop)
	if btn_choice == "Different song":
		btn_choice = "";
		continue
	#if quit is pressed, close app and stop music
	elif btn_choice == "Quit":
		pygame.mixer.music.stop()
		btn_choice = "";
		break
	#if nothing has been chosen, also close app and stop music
	else:
		pygame.mixer.music.stop()
		btn_choice = "";
		break
