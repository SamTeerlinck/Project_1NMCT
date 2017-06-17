import easygui
import glob

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
			btn_message = "Now playing " + lst_choices[index] + "."
			btn_choice = easygui.buttonbox(btn_message, btn_title, btn_choices)

	if btn_choice == "Different song":
		btn_choice = "";
		continue
	elif btn_choice == "Pause/Play":
		btn_choice = "";
		easygui.msgbox("Pause", "Playing Song")
	elif btn_choice == "Quit":
		btn_choice = "";
		break
	else:
		btn_choice = "";
		break