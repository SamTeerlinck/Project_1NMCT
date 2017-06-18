import easygui
import glob
import pygame

pygame.mixer.init()
playing = 0
songlist = glob.glob('/home/pi/Music/*.mp3')

lst_message = "Choose a song."
lst_title = "Music Player"
lst_choices = glob.glob('/home/pi/Music/*.mp3')
for index in range(len(lst_choices)):
	lst_choices[index] = lst_choices[index].replace('/home/pi/Music/','')
	lst_choices[index] = lst_choices[index].replace('.mp3','')

btn_message = ""
btn_title = "Playing Song"
btn_choices = ["Different song","Pause/Play","Quit"]

while True:
	lst_choice = easygui.choicebox(lst_message, lst_title, lst_choices)

	for index in range(len(lst_choices)):
		if lst_choice == lst_choices[index]:
			pygame.mixer.music.load(songlist[index])
			pygame.mixer.music.play()
			playing = 1
			btn_message = "Now playing " + lst_choices[index] + "."
			while True:
				btn_choice = easygui.buttonbox(btn_message, btn_title, btn_choices)
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

	if btn_choice == "Different song":
		btn_choice = "";
		continue
	elif btn_choice == "Quit":
		pygame.mixer.music.stop()
		btn_choice = "";
		break
	else:
		pygame.mixer.music.stop()
		btn_choice = "";
		break
