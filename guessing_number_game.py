# import random
# check_wanting = input("Are You Want To Play A Game With Me ").capitalize()
# list_of_check_wanting = ["Yes","Yeah","Y","Sure","S","Ok","Okay"]
# if check_wanting in list_of_check_wanting :
#     random_number = random.randrange(int(input("Enter Your Start Number: ")) , int(input("Enter Your end Number: ")))
#     guessing_number = int(input("guess the number: "))
#     while random_number != guessing_number :
#         if guessing_number > random_number :
#             guessing_number = int(input("Your number is larger than random number, please try again: "))
#         elif guessing_number < random_number :
#             guessing_number = int(input("Your number is smaller than random number, please try again: "))
#     else:
#         print("congratulation that's the true number")

# -------------------------------------------------------------------------------------------------------
# TODO  --Development has been made to keep the number within the range that the user specifies--  TODO # 
# -------------------------------------------------------------------------------------------------------

# import random
# check_wanting = input("Are You Want To Play A Game With Me ").capitalize()
# list_of_check_wanting = ["Yes","Yeah","Y","Sure","S","Ok","Okay"]
# # ------------That's checking wanting of playing the game------------- #
# if check_wanting in list_of_check_wanting :
#     #*------------------ My Variables ------------------*#
#     first_number = int(input("Enter Your Start Number: "))
#     last_number = int(input("Enter Your end Number: "))
#     random_number = random.randrange(first_number , last_number)
#     guessing_number = int(input("guess the number: "))
#     #*---------------------------------------------------*#
#     while random_number != guessing_number :
#         if guessing_number > random_number :
#             if guessing_number > last_number :
#                 print("ERROR! The number is out of the range")
#                 break
#             else :
#                 guessing_number = int(input("Your number is larger than random number, please try again: "))
#         elif guessing_number < random_number :
#             if guessing_number < first_number :
#                 print("ERROR! The number is out of the range")
#                 break
#             else :
#                 guessing_number = int(input("Your number is smaller than random number, please try again: "))
#     else:
#         print("congratulation that's the true number")

# -------------------------------------------------------------------------------
# TODO  --Development has been made to Determine the number of attempts--  TODO # 
# -------------------------------------------------------------------------------
import random
check_wanting = input("Are You Want To Play A Game With Me ").capitalize()
list_of_check_wanting = ["Yes","Yeah","Y","Sure","S","Ok","Okay"]
# ------------That's checking wanting of playing the game------------- #
if check_wanting in list_of_check_wanting :
    #*------------------ My Variables ------------------*#
    first_number = int(input("Enter Your Start Number: "))
    last_number = int(input("Enter Your end Number: "))
    random_number = random.randrange(first_number , last_number)
    guessing_number = int(input("guess the number: "))
    attempts = int(round((((last_number - first_number) / 10) + 0.5) +1)) 
    #*---------------------------------------------------*#
    while random_number != guessing_number :
        if guessing_number > random_number and attempts != 0:
            if guessing_number > last_number :
                print("ERROR! The number is out of the range")
                break
            else :
                attempts -= 1
                print(f"You have {attempts} attempts")
                guessing_number = int(input("Your number is larger than random number, please try again: "))
        elif guessing_number < random_number and attempts != 0 :
            if guessing_number < first_number :
                print("ERROR! The number is out of the range")
                break
            else :
                attempts -= 1
                print(f"You have {attempts} attempts")
                guessing_number = int(input("Your number is smaller than random number, please try again: "))
        if guessing_number == random_number:
            print("congratulation that's the true number")
        if attempts == 0 :
            print("Your attempts are over")
            break