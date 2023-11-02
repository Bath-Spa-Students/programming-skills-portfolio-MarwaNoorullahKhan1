invitations = ["Loisa ♡🖤♥" , "Kairi ♡🖤♥" , "Rinoa ♡🖤♥" , "Pheobe ♡🖤♥" , "Aysa ♡🖤♥"]

for invitation in invitations:
    print("Welcome to my dinner party {}".format(invitation))
    
print()    
   
print("{} can't make it to the party".format(invitations[4])) #Adding a print call to tell who won't be coming
invitations.pop(2) # removing the person that won't be coming
print()

invitations.append("Kairi") #Adding the person that will be coming
for invitation in invitations:
    print("Welcome to my dinner party {}".format(invitation)) #printing updated list who will come
print()
    
print("People, just found a bigger table and more people will be joining us this evening")
print()
invitations.insert(0, "Lingxao ♡🖤♥") #inserting new name to the beginning of the list.
invitations.insert(2, "Sheikha") #inserting new name to the middle of the list.
invitations.append("Badr") #adding a name to the last list using append

for invitation in invitations:
    print("Welcome to my dinner party {}".format(invitation))
print()
print("I can invite only 4 people") #printing that only two people will show up

invitations.pop(0) #removing Sheldon from the list
print("Lingxao, good bye")
invitations.pop(1) #removing Amy from the list
print("Sheikha, good bye")
invitations.pop(0) #removing Michael from the list
print("Aysa, good bye")
invitations.pop(1) # removing Jackie chan from the list
print("Badr, good bye")

print("{0} , {1} , {2} & {3} you guys are still invited".format(invitations[0], invitations[1], invitations[2], invitations[3]))
del invitations[0] # deleting both of them and at the end it shows empty list. 
del invitations[0]
print(invitations)
