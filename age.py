def age():
    # This function will ask a user for their name and age.
    # Then the function will return it to the user.

    # 1. ask for the user's name and age
    name = input("What is your name?")
    age = input ("What is your age?")
    # 2. print it back to the user
    print(f"Hello, {name}. It looks like you are {age}.")
    

if __name__ == "__main__":
    age()