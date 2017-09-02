import common;

# define actions

def EnterDogYard(player1):
	common.Clear()
	print "You are standing in a dog yard with dogs. "
	if (player1.dog != "Lucy"):
		print "Lucy, the psycho Lab."
	if (player1.dog != "Maggie"):
		print "Maggie the mean chihuahua."
	if (player1.dog != "Cassi"):
		print "Cassi the kind Lab."
	print "What do you want to do?";
	print ""
	print "Your choices are:"
	if (player1.dog != "Lucy"):
		print "1. choose Lucy"
	if (player1.dog != "Maggie"):
		print "2. choose Maggie"
	if (player1.dog != "Cassi"):
		print "3. choose Cassi"
	print ""
	action = int(raw_input("Enter your choice:"))
	if action == 1:
  	      player1.dog = "Lucy"
	if action == 2:
	        player1.dog = "Maggie"
	if action == 3:
	        player1.dog = "Cassi"
	common.Clear();

	print ""
	print player1.dog, " is now walking with you."
	print "You can go North, South, East, or West"
	print ""
	print "Your choices are:"
	print "1. go North"
	print "2. go South"
	print "3. go East"
	print "4. go West"
	print ""
	action = int(raw_input("Enter your choice:"))
	if action == 1:
        	EnterPark(player1);
	if action == 2:
        	EnterForest(player1);
	if action == 3:
        	EnterHome(player1);
	if action == 4:
		EnterBeach(player1);


def EnterPark(player1):
	common.Clear();
	print "You are standing in a park";
	print "You are surrounded by a gang of bulldogs.  What do you want to do?"
	print "Your choices are:"
	print "1. ", player1.dog, " befriends bulldogs"
	print "2. ", player1.dog, " attacks bulldogs"
	print "3. run away"
	print ""
	action = int(raw_input("Enter your choice:"))
	if action == 1 and player1.dog == "Lucy":
		print "The bulldogs are now your friends.  You may continue."
		player1.friends = "bulldogs"
	if action == 1 and player1.dog == "Maggie":
		print "The bulldogs are scared and run away"
	if action == 1 and player1.dog == "Cassi":
		print "The bulldogs are now your friends.  You may continue."
		player1.friends = "bulldogs"
	if action == 2 and player1.dog == "Lucy":
		print "Lucy falls down and lets the bulldogs attack her."
	if action == 2 and player1.dog == "Maggie":
		print "Maggie defeats the bulldogs."
	if action == 2 and player1.dog == "Cassi":
		print "Cassi gets scared and runs away"
		player1.dog = ""
	
	print "Which way do you want to go?"
	print "Your choices are:"
	print "1. go North"
	print "2. go South"
	print "3. go East" 
	print "4. go West"
	print ""
	action = int(raw_input("Enter your choice:"))
	if action == 1:
	        EnterMountains(player1);
	if action == 2:
	        EnterDogYard(player1);
	if action == 3:
	        EnterGrandmasHouse(player1);
	if action == 4:
		EnterBeach(player1)

	

	
		



def EnterForest():
	common.Clear();
	print "You are standing in a forest"

def EnterHome():
	common.Clear()
	print "You are at home"

def EnterBeach(player1):
	common.Clear()
	print "You are standing on the beach"
	print "A crab runs up and starts chasing your dog"
	if player1.dog == "Maggie":
		print "Maggie eats the crab";
	if player1.dog == "Lucy":
		print "Lucy jumps into the water";
		print "Your choices are:"
		print "1. Go after her in the water";
		print "2. Let her go."
		action = int(raw_input("Enter your choice:"))
		if action == 1:
	        	EnterWater(player1);
		if action == 2:
			player1.dog = "";
	if player1.dog == "Cassi":
		print "Cassi runs back to the dog yard"
		player1.dog = "";
	print ""
	print "Which way do you want to go?"
	print ""
	print "1. Go East"
	action = int(raw_input("Enter your choice:"))
	if action == 1:
	       	EnterDogYard(player1);
	
		

