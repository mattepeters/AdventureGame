import player;
import rooms;
import common;
common.Clear();

print ("Welcome to Adventure Game")

player1 = player.Player()
player1.setup();

common.Clear()

print "Welcome, %s.  Let's get started." % (player1.name)
print ""

rooms.EnterDogYard(player1);

print ("\n" * 10);
print "Game over."
raw_input("Press any key to end game");
common.Clear()
