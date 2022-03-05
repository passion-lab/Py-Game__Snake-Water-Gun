import random
import time


options = ["s", "w", "g"]
full = {
    "s": "Snake",
    "w": "Water",
    "g": "Gun"
}

user_points = 0
cpu_points = 0

times = 10
attempt = 1

greetings_win = ["AWESOME", "GREAT", "MARVELOUS", "BRILLIANT", "HURRAY", "OH YEAH", "CHEERS"]
greetings_lose = ["OOPS", "SORRY", "AAW", "BAD", "OH NO", "NOOP"]


def play_formula(user_input, cpu_input):
    global user_points
    global cpu_points

    if user_input == "s" and cpu_input == "w":
        print("HURRAY, You won!")
        print("Because you chose {} and computer chose {}\n\n".format(full[user_input], full[cpu_input]))
        user_points += 1
    elif user_input == "w" and cpu_input == "s":
        print("OOPS, Computer won!")
        print("Because you chose {} and computer chose {}\n\n".format(full[user_input], full[cpu_input]))
        cpu_points += 1
    elif user_input == "w" and cpu_input == "g":
        print("HURRAY, You won!")
        print("Because you chose {} and computer chose {}\n\n".format(full[user_input], full[cpu_input]))
        user_points += 1
    elif user_input == "g" and cpu_input == "w":
        print("OOPS, Computer won!")
        print("Because you chose {} and computer chose {}\n\n".format(full[user_input], full[cpu_input]))
        cpu_points += 1
    elif user_input == "s" and cpu_input == "g":
        print("OOPS, Computer won!")
        print("Because you chose {} and computer chose {}\n\n".format(full[user_input], full[cpu_input]))
        cpu_points += 1
    elif user_input == "g" and cpu_input == "s":
        print("HURRAY, You won!")
        print("Because you chose {} and computer chose {}\n\n".format(full[user_input], full[cpu_input]))
        user_points += 1
    else:
        print("DRAW, no one won!\n")
        print("Because you chose {} and computer chose {}\n\n".format(full[user_input], full[cpu_input]))


while times >= 1:
    if times >= 4:
        print(f"Round: {attempt}\n")
    elif 3 >= times > 1:
        print(f"Round: {attempt} | {times} more times you can play.\n")
    else:
        print(f"Round: {attempt} | Final Round.\n")

    def game():
        if times % 2 == 0:
            print("Any one from the following & hit enter.\n Type, S for Snake\n       W for Water\n       G for Gun\n")
            user = input("Make your choice: ")
            if len(user) >= 2:
                print("<!> SORRY, more than one input is invalid. Only one option will be accepted.")
                time.sleep(3)
                game()
            else:
                if user.lower() in options:
                    print("Now computer is choosing...\n")
                    time.sleep(1)
                    cpu = random.choice(options)
                    play_formula(user.lower(), cpu)
                else:
                    print("<!> SORRY, you entered a wrong option. Choose the right option again.")
                    time.sleep(3)
                    game()
        else:
            print("Wait, computer is choosing...\n")
            time.sleep(1)
            cpu = random.choice(options)
            print("Any one from the following & hit enter.\n Type, S for Snake\n       W for Water\n       G for Gun")
            user = input("\nNow, it's your turn. Put yours: ")
            if len(user) >= 2:
                print("<!> SORRY, more than one input is invalid. Only one option will be accepted.")
                time.sleep(3)
                game()
            else:
                if user.lower() in options:
                    play_formula(user.lower(), cpu)
                else:
                    print("<!> SORRY, you entered a wrong option. Choose the right option again.")
                    time.sleep(3)
                    game()

    game()
    attempt += 1
    times -= 1


if user_points > cpu_points:
    print("\\\\ F I N A L  R E S U L T \\\\\\\\________________________________________________\n")
    print(f"{random.choice(greetings_win)}, You won the match by {user_points - cpu_points} points!\n")
    print("{:<20}: {} times more than Computer".format("You won", user_points - cpu_points))
    print("{:<20}: {} Points\n{:<20}: {} Points".format("You scored", user_points, "Computer scored", cpu_points))
elif user_points < cpu_points:
    print("\\\\ F I N A L  R E S U L T \\\\\\\\________________________________________________\n")
    print(f"{random.choice(greetings_lose)}, You lose the match by {cpu_points - user_points} points!\n")
    print("{:<20}: {} times more than you".format("Computer won", cpu_points - user_points))
    print("{:<20}: {} Points\n{:<20}: {} Points".format("You scored", user_points, "Computer scored", cpu_points))
else:
    print("\\\\ F I N A L  R E S U L T \\\\\\\\________________________________________________\n")
    print("DRAW! No one won the match.")
    # How make a function global?
    # global game
    # game()

