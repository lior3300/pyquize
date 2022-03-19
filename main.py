'''
    this is a quiz game
    
    part 1: creating the game
    started: 19/3/2022 15:36
    finished: 19/3/2022 17:33

    part 2
    started: 19/3/2022 20:03
    finished: 19/3/2022 XXXXXX
'''
import json

#read answers from file, convert them into a tuple and appened them into the list
answers = []
with open('answers.txt') as answers_file:
    for i in answers_file:
        answers.append(tuple(i.rstrip('\n').split(",")))

#question source https://www.mentimeter.com/blog/audience-energizers/55-free-trivia-and-fun-quiz-question-templates
with open('questions.json') as questions_json:
    questions = json.load(questions_json)

def restart_game():
    score = 0
    questionNum = 0

    for question in questions.keys():
        answer=None

        print("\n------------------------")
        print(question+"\n")
        print(*answers[questionNum],sep="\n") # * is called kwargs

        score += check_answer(answer:=input("what is your answer? ").upper(),question) # := is called walrus (working on python 3.8+)
        questionNum += 1
    
    show_score(score)
        
def check_answer(answer,question):
    if questions.get(question) == answer:
        print("\nCorrect!")
        return 1
    else:
        print("\nwrong!")
        return 0

def show_score(score):
    percent=(score/len(questions)*100)
    print("you answered {:.1f}% of the question correctly!".format(percent))

def main():
    print("in this game you'll be shown {} question and 4 possiable answers A-D for each wuestion.".format(len(questions)))
    print("choose A/B/C/D to go to the next question.\n")
    
    restart_game()
    while restart := input("\nwant try again? write any charecter for to try again, or write no to stop: ") != "no":
        restart_game()


main()


        