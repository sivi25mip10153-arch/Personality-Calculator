# # Personality-Calculator using python code

## about the problem :-
As we all know, people around the world have various personality types, and many are curious to learn more about them, including their kindness, understanding, logic, and intelligence. However, comprehensive personality tests can often be lengthy and complicated.

This is why we need a simple personality calculator that can ask a few questions and categorize individuals into specific personality types.Now, full personality tests are sometimes lengthy and complicated.

**goal:** To design a personlity calculator using python code that will:

1. Asks ud multiple choice questions
2. scores each answer
3. add up your score for every question you answer
4. gives you one of the *7 personalities* according to your score
5. gives a brief description about your personalities
   

**personality types: used in this project** 

1. ISTJ: practical, realistic, responsible, enjoys creating an orderly life
   
2  ISFJ: friendly, thorough, responsible, considerate, concerned about other

3  INFJ: insightful, organized, seeks connection through ideas and material possessions

4  INTJ: independent thinkers, creative, analytical, high standards for themselves and others

5  ISTP: tolerant, highly independent, quiet observers, interested in cause/effect and values efficiency

6  ISFP: quiet, creative, friendly, kind, very connected to the present moment, tends to avoid conflicts

7  INFP: idealistic, curious, flexible, accepting, wants to improve the world



## algorithm:-
1.Start

2.user enter there name

3.initialize score = 0

4.display first question with option a,b,c,d,e and get input

5.add score based on selected options

6.repeat the process for all questions

7.calculate score percentage = (received score/maximum score)*100

8.compare percentage with redefined ranges 

9. display personality type and description

10 End


## overview of the project:-
1. it's an mcq based personality test/calculator
2. it calculates score
3. show's people their personality type
4. saves result in a file


## pseudocode for the problem:-

start

read username
set total_score = 0

function ask questions():-
set score = 0
for each question from 1 to n
display questions and options
read userchoice 
add marks based on user_choice to the score
return score

total_score = call ask question()

max_score = n*highest_option_marks
percentage = (total_score/max_score)*100

function find personality (percentage) :-
if 0 < percentage <= 15 than
return "ISTJ"

else if 15 < percentage <= 30 than
return "ISFJ"

else if 30 < percentage <= 45 than 
return "INFJ"

else if 45 < percentage <= 60 than
return "INTJ"

else if 60 < percentage <= 75 than
return "ISTP"

else if 70 < percentage <= 90 than
return "ISFP"

else
return "INFP"

personality type = call findpersonality(percentage)


display user_name
display personality_type
display brief description
display percentage



end


## testing:-

Once the program is applied testing is going to be done by:-

1. running the quiz by inserting different answer choices to verify if the percentage is increasing correctly
2. checking wheather the correct personality type is being shown in results according to there percentage.
3. making sure that users file "result.test" is being created and showing username, personality and description

   screenshots will be added after testing in "/screenshots" folder after testing are completed.

   






   




































