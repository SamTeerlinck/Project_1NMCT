# Database
I couldn't install the MySQL server on my Raspberry Pi because in order to do it, I had to run the command: "sudo apt-get update".
I can't run this command because it would overwrite the kernel installed by the Touchscreen.
I couldn't find any working older versions of MySQL, so if you want to really use the database, don't use the touchscreen.

Here you can find the code I made that should work in case you're using a database.
Musicplayer.py has been modified and a new Top 5 songs script has been added to display from the database.
