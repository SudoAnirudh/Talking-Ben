



#made as a joke dont be a fucking bum... :)

#Talking ben's house in replit

#NOTES ON BOSS FIGHT IS IN 'boss.py'

#imports
import potions 
from potions import *
import random, replit, time
from replit import audio
from colorama import Fore
import boss
from boss import *
from begin import *
from replit import db
from os import environ as env

username = env["REPL_OWNER"]
print("Hello {}!".format(username))
time.sleep(1)
replit.clear()

#shortened commands
sleep = time.sleep
reply = ["'Yes'", "'No'", "'bleughh'", "'Hohoho'"]

#counts how many times program has been played

#RIP title

critchance = random.randint(0,10)
crit = 2
defended = random.randint(0,6)


def menub():
	if hp == 404:
		print("Your Health: Error 404. Health not found.")
	else:
		print("Your Health: {}".format(hp))
	sleep(1)
	if bosshp == 404:
		print("Ben's Health Error 404. Health not found.")
	else:
		print("Ben's Health: {}".format(bosshp))
	sleep(1)
	print("\n[Attack] - Damages Ben.\n[Defend] - Chance to block Ben's attack.\n[Heal] - Regain some of your health.\n\n")


#lines 73-123 will have no comments.
	#if you want them go to boss.py
	
#attacks enemy
def attack():
	replit.clear()
	sleep(.2)
	print("You attack Ben. \n")
	critdmg = 1
	sleep(1)
#checks crit chance
	if critchance == 10:
		critdmg = damagedealt * crit
	print("You dealt {} damage.\n".format(damagedealt * crit))
	return damagedealt * crit
#
def defend():
	replit.clear()
	sleep(.2)
	print("You prepare your defences. \n")

def heal():
	replit.clear()
	sleep(.2)
	print("You wrap yourself in bandages. \n")
	sleep(1)
	print("You gained {} health. \n".format(plushp))

def battack():
	replit.clear()
	sleep(.2)
	print("Ben attacks you. \n")
	sleep(1)
	if prompt == "DEFEND":
			print("You deflected the attack. \n")
	else:
		print("You take {} damage. \n".format(damagetaken))
#
def bdefend():
	replit.clear()
	sleep(.2)
	if prompt == "ATTACK":
			print("Ben deflected your attack. \n")
	else:
		print("Ben tried to deflect you attack...\n")
		sleep(1)
		replit.clear()
		print("... but it failed")

def bheal():
	replit.clear()
	sleep(.2)
	print("Ben regained {} health. \n".format(plusbhp))


#prints bens naughty pictures
def pic():
	#ascii art from
	#https://copypastatext.com/tag/talking-ben/
	print("⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
	print("⣿⣿⣿⣿⣿⣿⢿⢯⣛⣺⣯⣿⣿⣿⣿⣿⣿⣿⢱⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
	print("⣿⣿⣿⡿⣿⣿⢡⣿⣉⣿⡿⠿⠿⠿⡿⠿⠻⣿⡇⠸⣻⠾⣿⣿⣿⣿⣿⣿⣿⣿")
	print("⣿⣿⡿⠛⠉⠁⠹⡰⣹⣟⣧⣤⡤⠄⠄⠠⣡⣼⣷⠄⢉⢻⣿⣿⣿⣿⣿⣿⣿⣿")
	print("⣿⠟⠄⠄⠄⡀⢸⣾⣿⣯⣯⡃⠄⠄⠄⠄⠐⠙⣿⣧⡀⠩⣧⠙⣿⣿⣿⣿⣿⣿")
	print("⣿⠄⠄⠄⠈⠈⣾⣿⣿⣿⣿⣆⡀⠄⠄⠄⠄⠄⣸⣿⣿⣿⣧⠄⣼⣿⣿⣿⣿⣿")
	print("⣿⠇⠄⠄⠄⠄⠙⠛⠛⠿⠿⢿⣿⣶⣀⣶⣾⣿⣿⣿⣿⢾⣷⣇⣤⣿⣿⣿⣿⣿")
	print("⣿⣻⠄⠄⠄⠄⠄⠄⠄⠄⠠⠤⣤⣤⣌⠉⠉⠉⠁⢈⠁⠤⠛⣼⣿⣿⣿⣿⠿⠿")
	print("⠈⠈⠄⠄⠄⠄⣀⣴⡦⠴⠠⢠⣴⣶⣶⣶⣿⣿⡶⠛⠠⠄⠄⣿⣿⡿⠟⠁⠺⠿")
	print("⣀⣤⣤⣦⣤⣼⣿⡿⣣⣿⡷⣿⣿⣿⣿⣿⣿⡿⣿⡄⠄⠄⠄⢟⡁⠚⠦⠴⠤⣤")
	print("⠿⠉⠛⠟⣻⣿⠋⢁⣿⢿⣵⣭⣞⢿⣯⣽⣿⣿⣿⣿⡆⠄⠄⠄⠉⠄⠄⠄⠄⠄")
	print("⠄⠄⠄⠄⠈⠁⠄⢯⣷⣿⣿⣯⡿⣽⣾⣿⣿⠿⢿⣿⣧⡄⠄⠄⠄⠄⠄⠄⠄⠄")
	print("⠄⠄⠄⠄⠄⠄⡴⢇⠉⢹⣀⣿⣿⣿⢿⡟⣿⣧⣼⡀⡩⠻⣦⠄⠄⠄⠄⠄⠄⠄")
	print("⠄⠄⠄⠄⠰⠄⠣⣸⣶⠛⠛⠻⣿⡿⠿⢱⡟⠉⠉⠻⣿⡲⠃⠄⠄⠄⠄⠄⠄⠄")
	print("⠄⠄⠄⠄⠄⠒⠄⠈⠿⠄⠄⠄⡿⠃⠄⠘⠄⠄⢀⡠⠏⠄⠄⠄⠄⠄⠄⠄⠄⠄")


#multiple 'space' variables to line up the text
space = "    "
space2 = space + " "
space3 = "  "
space4 = space + space + " "
#menu
def menu():
  try: #errors fixed
		#checks menu input
    a = int(input(Fore.WHITE + "\n1 : Poke Ben "+space+"2 : Talk to Ben \n3 : Call Ben"+space2+"4 : Tickle feet\n5 : Apple Juice"+space3+"6 : Beans\n7 : Burp"+space4+"8 : Lab\n9 : Settings"+space+" 10: Do you love God?!\n\nNumber: "))
    return a
	#pass if it doesn't work
  except ValueError:
    pass
    

#poke ben


def poke():
	replit.clear()
	#random chance for alternate output
	r = random.randint(1,20)
	if r != 1:
		#prints ben's response
		print("\nBen: Ooogghh\n\n" + Fore.RED + "*Ben is dissapointed*" + Fore.WHITE)
	else:
		#random chance to play this message:
		print("\nBen: Ooohhff\n\n" + Fore.RED + "*Ben is almost dead you poked him too hard*" + Fore.WHITE)
		
def appleJuice():
	replit.clear()
	#prints ben's response to the drink
	print("\nBen: *glug glug glug*\n\n" + Fore.LIGHTGREEN_EX + "*Ben really enjoyed that apple juice!*" + Fore.WHITE)

def beans():
	replit.clear()
	#ben's response
	print(Fore.LIGHTGREEN_EX + "\n*Ben scoffs down the beans, delicious!*" + Fore.WHITE)

def burp():
	replit.clear()
	#burp
	print("\nBen: *Burp*")

#talk to ben
def talk():
	replit.clear()
	#obtains input
	s = str(input(Fore.LIGHTGREEN_EX + "\nBen is listening:  " + Fore.WHITE))
	#prints userinput as ben
	print("\nBen: {}".format(s))



def credits():
	#@HW556 is the best ;)
	print ("  ___________________________  \n | Ryan1408 + 22LMatt + HW556| \n |___________________________| ")

		
	


#call ben
def call():
	replit.clear()
	calling = True
	print("\nBen: 'Bæn?'")
	p = 0
#tries playing audio, pass if it does not work
	try:
		audio.play_file("sound/Ben.wav")
	except:
		pass
	#loop so that you don't have to keep calling
	while calling == True:
		if p == 0:
			#shows people how to leave
			print("To leave type 'Hang Up'")
		p=1 # doesn't repeat leave tutorial

			#obtains question
		q = str(input("\nQuestion for Ben: "))
		hang = random.randint(0,14)
		
		#checks if ben hung up
		if hang == 0:
			calling = False
			print(Fore.RED + "\n*Ben slammed the phone down*" + Fore.WHITE)
#checks if user hun up
		elif q.lower() == "hang up":
			calling = False
			replit.clear()
			print(Fore.RED + "\n *Newspaper sounds*" + Fore.WHITE)

		else: # prints ben's reply
			print("\nBen:",reply[random.randint(0,3)])
					
#tickle feet
def feet():
	replit.clear()
	print("\nBen: Ooohh ;)\n\n" + Fore.LIGHTGREEN_EX + "*Ben likes that, he really likes that...*\n" + Fore.WHITE)

#lab
def lab():
	replit.clear()
	time.sleep(.2)
	print(Fore.RED + "\n"+TheMotionOfThePotion() + Fore.WHITE) #pop fizz

#checks the difficulty of the boss fight and
	#sets health accordinly 
def difficulty(diff):
	if diff == 1:
		boss = 50
	elif diff == 2:
		boss = 100
	elif diff == 3:
		boss = 200
	elif diff == 4:
		boss = 500
	elif diff == 5:
		boss = 1500
	return boss
	
#main
pic()
while 1 == 1:
	#choose what to do
	m = menu()
	if m == 1:
		poke()
	elif m == 2:
		talk()
	elif m == 3:
		call()
	elif m == 4:
		feet()
	elif m == 5:
		appleJuice()
	elif m == 6:
		beans()
	elif m == 7:
		burp()
	elif m == 8:
		lab()
	elif m == 9:
		credits()
		# boss difficulty selection
		print("\n  1 : Boss Difficulty")
		prompt = int(input(""))
		if prompt == 1:
			replit.clear()
			print("1 : Easy")
			print("2 : Medium")
			print("3 : Hard")
			print("4 : Impossible")
			print("5 : Yeah..... you're not beating this one.")
			diff = int(input(""))
			sleep(1)
			replit.clear()
    
      
    
	elif m == 10:
	#main boss fight
# notes on code in 'boss.py'
		play = True
		hp = 20
		bosshp = 100
		maxbosshp = 100
		try:
			maxbosshp = difficulty(diff)
			bosshp = difficulty(diff)
		except:
			pass
		replit.clear()
		print("Hohoho...")
		time.sleep(1)
		replit.clear()
		print("No.")
		time.sleep(1)
		replit.clear()
		challenger()
		while play == True:
			bturn = random.randint(1,6)
			defence = random.randint(0,3)
			if maxbosshp == 1500:
				damagetaken = random.randint(6,15)
			else:
				damagetaken = random.randint(1,8)
			damagedealt = random.randint(2,10)
			plushp = random.randint(5,12)
			plusbhp = random.randint(3,7)
			if hp > 0 or bosshp > 0:
				if hp > 0:
					menub()
					prompt = input().upper()
				
					if prompt == "ATTACK":
						if bturn != 5:
							bosshp = bosshp - attack()
						sleep(1)
				
					elif prompt == "DEFEND":
						defend()
						sleep(1)
					elif prompt == "HEAL":
						replit.clear()
						heal()
						hp = hp + plushp
						if hp > 25:
							hp = 25
						sleep(1)

					elif prompt == "IVANWANG8":
						replit.clear()
						print("Ben: That's impossible....")
						print("Ben exploded leaving nothing but his middle finger behind.")
						replit.clear()
						sleep(1)
						bosshp=0
				else:
					break
			
				if bosshp > 0:
					if bturn < 5:
						battack()
						if prompt != "DEFEND":
							hp = hp - damagetaken
						sleep(1)
						replit.clear()
					elif bturn == 5:
						bdefend()
						sleep(1)
					elif bturn == 6:
						bheal()
						bosshp = bosshp + plusbhp
						if bosshp > maxbosshp:
							bosshp = maxbosshp
						sleep(1)
				else:
					break
			else:
				play = False
				break


		print("Your Health: {}".format(hp))
		print("Ben's Health: {}".format(bosshp))

		if bosshp < 0:
			bosshp = 0
		if hp < 0:
			hp = 0
		
		if bosshp <= 0:
			print("You Win!")
		elif hp <= 0:
			print("You Lose!")
	else:
		print(Fore.RED + "No." + Fore.WHITE)
    