'''
    this is a quiz game
    started: 19/3/2021 15:36
    finished: :( TODO
'''

#question source https://www.mentimeter.com/blog/audience-energizers/55-free-trivia-and-fun-quiz-question-templates
questions = {
"What country has the highest life expectancy?":"B",
"Where would you be if you were standing on the Spanish Steps?":"A",
"Which language has the more native speakers: English, Portuguese, Spanish or Mandarin?":"D",
"What is the most common surname in the United States?":"D",
"What disease commonly spread on pirate ships?":"B",
"Who was the Ancient Greek God of the Sun? ":"C",
"What was the name of the crime boss who was head of the feared Chicago Outfit?":"A",
"What year was the United Nations established?":"B",
"Who has won the most total Academy Awards?":"B",
"What artist has the most streams on Spotify?":"C",
} #TODO: move questions to json file

answers = [
("A)Russia","B)Hong Kong","C)Australia","D)Taiwan"),
("A)Rome","B)Greece","C)Madrid","D)Morocco"),
("A)Mandarin","B)German","C)Portuguese","D)Spanish"),
("A)White","B)Mcgregor","C)Kohen","D)Smith"),
("A)Chickenpox","B)Scurvy","C)Influenza","D)Covid-19"),
("A)Zeus","B)Poseidon","C)Apollo","D)Artemis"),
("A)Al Capone","B)Bugsy Siegel","C)Lucky Luciano","D)Tony Accardo"),
("A)1939","B)1945","C)1918","D)1948"),
("A)Ethan Coen","B)Walt Disney","C)Robert Amram","D)Peter Farrelly"),
("A)Taylor Swift","B)The Weeknd","C)Drake","D)Beyonce")
] #TODO: move to a file

def restart_game():
    score = 0
    questionNum = 0

    for i in questions.keys():
        answer=None

        print("\n------------------------")
        print(i+"\n")
        print(*answers[questionNum],sep="\n") # * is called kwargs

        score += check_answer(answer:=input("what is your answer? ").upper(),i) # := is called walrus (working on python 3.8+)
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
    pass

def main():
    print("in this game you'll be shown {} question and 4 possiable answers A-D for each wuestion.".format(len(questions)))
    print("choose A/B/C/D to go to the next question.\n")
    
    restart_game()
    while restart := input("\nwant try again? write any charecter for to try again, or write no to stop: ") != "no":
        restart_game()


main()