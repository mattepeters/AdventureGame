import common;
import player;

# define actions

class World:

	player1 = player.Player()

	def Start(self, player1):
		self.player1 = player1
		self.EnterDogYard()

	## -----------------------------------------------------------------
	## -------- The Dog Yard --------------------------------------------
	def EnterDogYard(self):
		common.Clear()
		print "You are standing in a dog yard with dogs. "
		if (self.player1.dog != "Lucy"):
			print "Lucy, the psycho Lab."
		if (self.player1.dog != "Maggie"):
			print "Maggie the mean chihuahua."
		if (self.player1.dog != "Cassi"):
			print "Cassi the kind Lab."
		print "What do you want to do?";
		print ""
		print "Your choices are:"
		if (self.player1.dog != "Lucy"):
			print "1. choose Lucy"
		if (self.player1.dog != "Maggie"):
			print "2. choose Maggie"
		if (self.player1.dog != "Cassi"):
			print "3. choose Cassi"
		print ""
		action = int(raw_input("Enter your choice:"))
		if action == 1:
			self.player1.dog = "Lucy"
		if action == 2:
				self.player1.dog = "Maggie"
		if action == 3:
				self.player1.dog = "Cassi"
		common.Clear();

		print ""
		print self.player1.dog, " is now walking with you."
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
				self.EnterPark();
		if action == 2:
				self.EnterForest();
		if action == 3:
				self.EnterHome();
		if action == 4:
			self.EnterBeach();


	## -----------------------------------------------------------------
	## -------- The Park -----------------------------------------------
	def EnterPark(self):
		common.Clear();
		print "You are standing in a park";
		print "You are surrounded by a gang of bulldogs.  What do you want to do?"
		print "Your choices are:"
		print "1. ", self.player1.dog, " befriends bulldogs"
		print "2. ", self.player1.dog, " attacks bulldogs"
		print "3. run away"
		print ""
		action = int(raw_input("Enter your choice:"))
		if action == 1 and self.player1.dog == "Lucy":
			print "The bulldogs are now your friends.  You may continue."
			player1.friends = "bulldogs"
		if action == 1 and self.player1.dog == "Maggie":
			print "The bulldogs are scared and run away"
		if action == 1 and self.player1.dog == "Cassi":
			print "The bulldogs are now your friends.  You may continue."
			self.player1.friends = "bulldogs"
		if action == 2 and self.player1.dog == "Lucy":
			print "Lucy falls down and lets the bulldogs attack her."
		if action == 2 and self.player1.dog == "Maggie":
			print "Maggie defeats the bulldogs."
		if action == 2 and self.player1.dog == "Cassi":
			print "Cassi gets scared and runs away"
			self.player1.dog = ""
		
		print "Which way do you want to go?"
		print "Your choices are:"
		print "1. go North"
		print "2. go South"
		print "3. go East" 
		print "4. go West"
		print ""
		action = int(raw_input("Enter your choice:"))
		if action == 1:
			self.EnterMountains();
		if action == 2:
			self.EnterDogYard();
		if action == 3:
			self.EnterGrandmasHouse();
		if action == 4:
			self.EnterBeach()

		

		
			


	## -----------------------------------------------------------------
	## -------- The Forest --------------------------------------------
	def EnterForest(self):
		common.Clear();
		print "You are standing in a forest"

	## -----------------------------------------------------------------
	## -------- Home --------------------------------------------
	def EnterHome(self):
		common.Clear()
		print "You are at home"

	## -----------------------------------------------------------------
	## -------- The Beach --------------------------------------------
	def EnterBeach(self):
		common.Clear()
		print "You are standing on the beach"
		print "A crab runs up and starts chasing your dog"
		if self.player1.dog == "Maggie":
			print "Maggie eats the crab";
		if self.player1.dog == "Lucy":
			print "Lucy jumps into the water";
			print "Your choices are:"
			print "1. Go after her in the water";
			print "2. Let her go."
			action = int(raw_input("Enter your choice:"))
			if action == 1:
				self.EnterWater();
			if action == 2:
				self.player1.dog = "";
		if self.player1.dog == "Cassi":
			print "Cassi runs back to the dog yard"
			self.player1.dog = "";
		print ""
		print "Which way do you want to go?"
		print ""
		print "1. Go East"
		action = int(raw_input("Enter your choice:"))
		if action == 1:
				self.EnterDogYard();
		
		

