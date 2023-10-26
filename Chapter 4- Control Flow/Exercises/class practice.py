'''sales = float(input("Enter sales :"))
bonus = 0
if sales > 45000 :
   bonus = 900
else :
      bonus = 0
print("Your bonus : "+str(bonus))'''

#Nested Decision Structure
earning = int(int(input("Enter your earning per year: ")))
total_lands_owned = int(input("Enter the total lands that is owned : "))

if earning > 45000:
    if total_lands_owned  >=1.5:
        print(" you are eligible for the position")
    else:
        print(" sorry your work experience is less than 1.5 years ")
else:
        print("your earning is less than 45000")  
          
