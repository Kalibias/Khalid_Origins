import time
import characters




def new_game():
    answer = input("Would you like to play? (yes/no) ")
    # fname, lname, age, spd, atk, dfs, money, health
    Khalid = characters.character_profile("Khalid", "Davis", 17, 2, 3, 3, 1000, 100)

    if answer.lower().strip() == "yes":
        print(f"Your name is {Khalid.get_fname()} {Khalid.get_lname()}.")
        print("Its been nearly 10 years since you were dropped at Block D's orphanage.")
        print("You're too old to be adopted at this point. You hadn't expected to be anyways.")
        print("The Caregiver has been patient with you, but they cannot afford to keep you 2 weeks past your 18th.\n")

        time.sleep(3)

        print("You don't have many options for work. Well, any that gets you closer your goals.")
        print("Regardless, you still need to find work.\n")

        time.sleep(2)

        print("Theres a STORE down the street. You may get some money working there.")
        print("Theres a GYM not to far off from here. Maybe could waste time there with your free trial.")
        print("Looks like theres a CLUB not to far off from the GYM. Not sure if you can be in there yet.\n")

        location = input("Where would you like to go first?")

        if location == "club":
            club(Khalid.money, Khalid.age)


def club(cost, age):
  if age != 18:
      print("The bouncer took your ID. He laughed in your face.")
      print("Bouncer: You ain't old enough to enter in here kid. Come back later.")
      pass

def orphanage():
   answer = input("You arrive back at the Orphanage. Would you like to go to sleep?")

   orphan_activities = {

   }

   if answer.lower().strip() == "yes":
       print("You can't stick around here to long. Not without being productive.")
       answer = input("The Caregiver asks you to help with the younger kids. Do you want to?")

       if answer.lower().strip() == "yes":
           print("You figure playing with the kids helps out.")
           print("They make you race with them. You forgot how much your energy balances out when you're older.")
           time.sleep(3)







if __name__ == '__main__':
    new_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
