invitations = ["Loisa ♡🖤♥" , "Kairi ♡🖤♥" ,"Aysa ♡🖤♥"  , "Pheobe ♡🖤♥" , "Rinoa ♡🖤♥"]
for invitation in invitations:
    print ("Welcome to my dinner party {}".format(invitation))
print()
print("{} can't make it to the party".format(invitations[2]))
#Adding a print call to tell who won't be coming

invitations.pop(2)
#Removing the person that won't be coming
print()
invitations.append("Aysa")
#Adding the person that will be coming for invitation in invitation
print("Welcome to my dinner party {}".format(invitation))
