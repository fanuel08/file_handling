'''## Create a program that asks for the user’s name and favorite color, then prints a personalized greeting like: “Hello, [Name]! Your favorite color, [Color], is awesome!”
# Greeting
def get_name():
    name = input(f"What is your name:")
    return name

## calling the function and storing the returned value
user_name = get_name()
print(f"Your name is {user_name}")
print(" ")

# Favorite color
def get_color():
    color = input(f"What is your favorite color: ")
    return color

# calling the function and storing the returned value
color = get_color()
print(f"Your favorite color {color} is awesome! ")

    
''2. Simple Quiz Game 🎮
Create a multiple-choice quiz with questions about Python, movies, or any fun topic! Display scores at the end and allow the user to play again. 🏆 ''

# a simple quiz
quiz_1 = input(f'Is python an object oriented language? "yes/no": ')
quiz_1 = quiz_1.upper()

if quiz_1 == "YES":
    print(f"You are correct, AWesome! ")
    print(f"+1")
    
elif quiz_1 == "NO":
    print(f"You're almost there, just try again ")
    print(f"0")'''
    
    
 # List of questions, options ad correct answers   
questions = [
              {
            "question" : "Who was the first Kenyan Pesident: ",
         "options" : ["A)Kasongo", "B)Uhunye", "C)Mai", "D)Matamu"],
         "correct" : "C"
         },
        {
           "question" : "Who is the football goat: ",
         "options" : ["A)Kasongo", "B)Uhunye", "C) Ranaldo", "D) M#ssi"], 
         "correct" : "D"
         } 
        ]
def game_quiz(questions):   
    # Initialize the score 
 score = 0

# Loop through each question
for q in questions:
    print(q["question"])
    
for option in options:
    print(["options"])    
    
   # Get users answers and convert to uppercase
answer = input("Input your answer: A, B, C, D ").strip().upper() 
   
   # Check if answer is correct
if answer == q["answers"]:
    print("✅ Correct!")
    count +=1
    
else:
    print(f"❌ Wrong! The correct answer was {q['answer']}")
    
 # Display final score
    print(f"\n🎉 You got {score} out of {len(questions)} correct!")

# Main program loop
while True:
    quiz_game()
    # Ask if user wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye! 👋")
        break   