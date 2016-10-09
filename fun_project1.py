import msvcrt
import time

finish=10
finish1=20
finish2=30
count=0
count1=10
count2=20

print " press enter key to get started!"

raw_input()
s_time=time.time()

while (1):
		key1=msvcrt.getch()
		if key1=='d':
					count=count+1
					print "-",
					if count==finish:
								print "TURN DOWN"
								break
while (1):
		key2=msvcrt.getch()
		if key2=='s':
					count1=count1+1
					print "          "
					print "                   |"
					if count1==finish1:
								print "TURN RIGHT"
								print "                   ",
								break
while (1):
		key3=msvcrt.getch()
		if key3=='d':

					count2=count2+1
					print "-",
					
					if count2==finish2:
								break
time_elapsed=time.time()-s_time
print "congrats you have finished the game"
print "time taken is" +str(time_elapsed)

'''
1. Mention controls for the game.
2. The game should be lost on pressing the wrong key
'''
