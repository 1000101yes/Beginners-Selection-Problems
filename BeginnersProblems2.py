print("You are exploring a rainforest in search of treasure. Legend has it that there are some buried on a nearby island.")

option = input("You come across a lake. Do you want to swim across, or wait for a boat? (swim/wait)")

if option == "swim":
    print("You get eaten by a hungry shark. Game over:(")
elif option == "wait":
    print("A boat arrives and you get to the island safely")
    option = input("You come to a cave. Do you want to venture in or walk on? (venture/walk)")
    
if option == "venture":
    print("You are squished by boulders and are never to be seen again. Game over.")
elif option == "walk":
    print("You avoid trouble safely and move on to the next area") 
    option = input("You're at a crossroads. One way leads to treasure; so, do you go (left/right/straight)?")

if option == "left":
    print("You are trampled by a wild herd of wildebeest. Game over.")
elif option == "straight":
    print("You are stung by a poisonous wasp. Game over.")
elif option ==  "right":
    print("You march on and find the buried treasure! YIPPEEEE!!!!!")
