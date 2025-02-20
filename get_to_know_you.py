# This function will ask the user 3 questions:
# 1. What is your name?
# 2. Where are you from?
# 3. What do you do for work?

# Then the function will give a summary of the user back to them.

def get_to_know_you():
    print("Welcome to the get to know you game, we are going to ask you questions.")
    name = input("What is your name?")
    from_home = input("Where are you from?")
    work = input("What do you do for work?")
    print("Information gathered, here are facts about you!")

    print(f"Your name is {name}")
    print(f"You are from {from_home}")
    print(f"For work you do {work}")

if __name__ == "__main__":
    get_to_know_you()