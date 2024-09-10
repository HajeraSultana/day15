exit = ""
while exit != "yes":
 print("Let's play Sound Safari")
 print()
 print("Press 1 for a cow, 2 for a cat, 3 for a dog, and 4 for a frog.")
 animal = int(input("Which animal do you want?"))
 if animal == 1:
   print("Moo")
   exit = input("Exit?: ")
 elif animal == 2:
   print("Meow")
   exit = input("Exit?: ")
 elif animal == 3:
   print("Woof")
   exit = input("Exit?: ")
 elif animal == 4:
   print("Ribbit")
   exit = input("Exit?: ")
 else:
   print("That's not an option.")
   exit = input("Exit?: ")
   print("Thank you for playing")