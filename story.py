#Ask user to fill out the story details
userName = str(input("What is you name?: "))
userSchool = str(input("Where do you got to school?: "))
userParent = str(input("My father's name is: "))
userHome = str(input("Where do you stay?: "))
noun1 = str(input("I love: "))
adjective1 = str(input("Enter your favorite adjective: "))

#Create story
print(f"My name is {userName} and I got to school at {userSchool}. My father is called {userParent} and we stay in {userHome}. Our {noun1} is very {adjective1}.")