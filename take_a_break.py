import webbrowser
import time


total_breaks = 3
break_count= 0

while(break_count < total_breaks):
	time.sleep(2*60*60)
	webbrowser.open("https://www.youtube.com/watch?v=StTqXEQ2l-Y")
	break_count = break_count + 1
	time.ctime()
	print ("This program started on " + time.ctime())
