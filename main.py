
def ask_questions():
    total_score = 0
    max_score = 0

    print("\nAnswer the following question by choosing one option from a,b,c,d,e")


    # Question 1

    print("\n Question 1. how do you usually make your decision?")
    print("\n a) i let others decide in my stance")
    print("\n b) i follow what i find easiest")
    print("\n c) i think a bit and choose")
    print("\n d) i compare pros and cons properly")
    print("\n e) i analyise deeply and plan accordingly")

    choice = input("enter option (a/b/c/d/e): ").lower()

    if choice == "a":
        total_score += 0
    elif choice == "b":
        total_score += 2
    elif choice == "c":
        total_score += 4
    elif choice == "d":
        total_score += 6
    elif choice == "e":
        total_score += 10
    else:
        print("\ninvalid input 0 will be added to the score")
        total_score += 0

    max_score += 10 


    # Question 2

    print("\n Question2. How do you feel about planning?")
    print("a) I don’t plan at all")
    print("b) I plan only when forced to")
    print("c) I make a rough plan sometimes")
    print("d) I usually plan my day or week")
    print("e) I love detailed long-term plans")

    choice = input("enter option (a/b/c/d/e): ").lower()

    if choice == "a":
     total_score += 0
    elif choice == "b":
     total_score += 2
    elif choice == "c":
     total_score += 4
    elif choice == "d":
     total_score += 6
    elif choice == "e":
     total_score += 10
    else:
     print("\ninvalid input 0 will be added to the score")
    total_score += 0 # This line seems redundant if it's already 0 for invalid input
    max_score += 10

    #Question 3

    print("\n Question 3. how do you prefer spending your time")
    print("a)Reading a book")
    print("b)watching tv or movies")
    print("c)excercising and playing sports")
    print("d)socializing with friends ")
    print("e)being alone")

    choice = input("enter option (a/b/c/d/e): ").lower()

    if choice == "a":
     total_score += 0
    elif choice == "b":
     total_score += 2
    elif choice == "c":
     total_score += 4
    elif choice == "d":
     total_score += 6
    elif choice == "e":
     total_score += 10
    else:
     print("\ninvalid input 0 will be added to the score")
    total_score =+ 0 # Typo: should be += 0
    max_score += 10


    #Question 4



    print("\n Question.4 what type of vacation do you enjoy the most ")
    print("a)beach")
    print("b)mountain")
    print("c)city exploration")
    print("d)cultural heritage")
    print("e)staying home")

    choice = input("enter option (a/b/c/d/e): ").lower()

    if choice == "a":
     total_score += 0
    elif choice == "b":
     total_score += 2
    elif choice == "c":
     total_score += 4
    elif choice == "d":
     total_score += 6
    elif choice == "e":
     total_score += 10
    else:
     print("\ninvalid input 0 will be added to the score")
    total_score += 0
    max_score += 10


    # Question5



    print("\n Question.5 whats your favorite type of food?")
    print("a)mexican")
    print("b)indian")
    print("c)italian")
    print("d)british")
    print("e)korean")

    choice = input("enter option (a/b/c/d/e): ").lower()

    if choice == "a":
     total_score += 0
    elif choice == "b":
     total_score += 2
    elif choice == "c":
     total_score += 4
    elif choice == "d":
     total_score += 6
    elif choice == "e":
     total_score += 10
    else:
     print("\ninvalid input 0 will be added to the score")
    total_score += 0
    max_score += 10

    #Question6

    print("\n Question.6 which pet would you prefer?")
    print("a)cat")
    print("b)dog")
    print("c)bird")
    print("d)fish")
    print("e)hamster")

    choice = input("enter option (a/b/c/d/e): ").lower()

    if choice == "a":
     total_score += 0
    elif choice == "b":
     total_score += 2
    elif choice == "c":
     total_score += 4
    elif choice == "d":
     total_score += 6
    elif choice == "e":
     total_score += 10
    else:
     print("\ninvalid input 0 will be added to the score")
    total_score += 0
    max_score += 10

    #Question7


    print("\n Question.7 how do you start your day?")
    print("a)by having a hearty breakfast")
    print("b)with working out")
    print("c)by catching up on news ")
    print("d)sleeping in as long as possible")
    print("e)going straight to work")


    choice = input("enter option (a/b/c/d/e): ").lower()

    if choice == "a":
     total_score += 0
    elif choice == "b":
     total_score += 2
    elif choice == "c":
     total_score += 4
    elif choice == "d":
     total_score += 6
    elif choice == "e":
     total_score += 10
    else:
     print("\ninvalid input 0 will be added to the score")
    total_score += 0
    max_score += 10

    #Question8


    print("\n Question.8 what is your favorite genre of music?")
    print("a)pop")
    print("b)jazz")
    print("c)R&B ")
    print("d)rock")
    print("e)classical")

    choice = input("enter option (a/b/c/d/e): ").lower() # Missing input for Q8, Q9, Q10

    if choice == "a":
     total_score += 0
    elif choice == "b":
     total_score += 2
    elif choice == "c":
     total_score += 4
    elif choice == "d":
     total_score += 6
    elif choice == "e":
     total_score += 10
    else:
     print("\ninvalid input 0 will be added to the score")
    total_score += 0
    max_score += 10


    #Question9

    print("\n Question.9 how would you describe your social life?")
    print("a)very active")
    print("b)moderately active")
    print("c)somewhat active")
    print("d)not very active")
    print("e)null active")


    choice = input("enter option (a/b/c/d/e): ").lower() # Missing input for Q9, Q10


    if choice == "a":
     total_score += 0
    elif choice == "b":
     total_score += 2
    elif choice == "c":
     total_score += 4
    elif choice == "d":
     total_score += 6
    elif choice == "e":
     total_score += 10
    else:
     print("\ninvalid input 0 will be added to the score")
    total_score += 0
    max_score += 10


    #Question10

    print("\n Question.10 what is your favorite type of movie?")
    print("a) horror")
    print("b) action")
    print("c) science fiction ")
    print("d) drama")
    print("e) fantasy")



    choice = input("enter option (a/b/c/d/e): ").lower() # Missing input for Q10


    if choice == "a":
     total_score += 0
    elif choice == "b":
     total_score += 2
    elif choice == "c":
     total_score += 4
    elif choice == "d":
     total_score += 6
    elif choice == "e":
     total_score += 10
    else:
     print("\ninvalid input 0 will be added to the score")
    total_score += 0
    max_score += 10


    return total_score, max_score



def get_personality (percentage):



     if 0 < percentage <= 15:
       personality_type = "ISTJ"
       description = "Practical, realistic, responsible and organised."

     elif 15 < percentage <= 30:
      personality_type = "ISFJ"
      description = "Friendly, responsible, considerate and caring about others."

     elif 30 < percentage <= 45:
      personality_type = "INFJ"
      description = "Insightful, idealistic, organised and focused on meaning."

     elif 45 < percentage <= 60:
      personality_type = "INTJ"
      description = "Independent, analytical, creative and sets high standards."

     elif 60 < percentage <= 75:
      personality_type = "ISTP"
      description = "Calm, independent, good at understanding how things work."

     elif 75 < percentage <= 90:
      personality_type = "ISFP"
      description = "Quiet, creative, kind, sensitive to the present moment."

     else:
      personality_type = "INFP"
      description = "Idealistic, curious, open-minded and wants to improve the world."
     
     return personality_type, description # Added return statement for get_personality


def main():
    print("welcome to the Personality Calculator!")
    name = input("enter your name: ")

    total_score, max_score = ask_questions()

    if max_score > 0:
        percentage = (total_score / max_score) * 100
    else:
        percentage = 0

    personality_type, description = get_personality(percentage)

    print("\n===RESULT ===")
    print("Name:", name)
    print("Personality Type:", personality_type)
    print("Description:", description)
    print("Score Percentage:", round(percentage, 2), "%")

    # save_result(name, personality_type, description, percentage) # save_result function is not defined


if __name__ == "__main__":
    main()




