invitations = ["Loisa ♡🖤♥" , "Kairi ♡🖤♥" ,"Aysa ♡🖤♥"  , "Pheobe ♡🖤♥" , "Rinoa ♡🖤♥"]

for invitation in invitations:
    print("Welcome to my dinner party {}".format(invitation))
    
print()    
   
print("{} can't make it to the party".format(invitations[2])) #Adding a print call to tell who won't be coming
invitations.pop(2) # removing the person that won't be coming
print()

invitations.append("Pheobe") #Adding the person that will be coming
for invitation in invitations:
    print("Welcome to my dinner party {}".format(invitation)) #printing updated list who will come
print()
    
print("People, just found a bigger table and more people will be joining us this evening")
print()
invitations.insert(0, "Lingxao ♡🖤♥")
invitations.insert(2, "Jianjian ♡🖤♥")
invitations.append("Badr ♡🖤♥")

for invitation in invitations:
    print("Welcome to my dinner party {}".format(invitation))
