#project: P4
#submitter-netid: kurosu
#partner-netid: none

remaining = int(input("How many tries do you want for each question: "))
correct = 0
tries = 3

def askQuestion(question, youranswer, hint):
    if question == "question1":
        print('What is the type of the following? "1.0" + "2.0" \na) int \nb) float \nc) str \nd) bool \ne) NoneType') 
    if question == "question2":
        print('What is the type of the following? "1" * 2')
    if question == "question3":
        print('What does this expression evaluate to? \nTrue != (3 < 2)')
   
    global remaining
    global correct
    global tries


    localremain = remaining

    while(localremain > 0):

        

        youranswer == "c"
        youranswer == "str"
        youranswer == "True"

        hint == "hint1"
        hint == "hint2"
        hint == "hint3"

        
        answer1 = input("Your answer: ")
        answer = str.strip(answer1)
        answer = str.lower(answer)

        if answer != youranswer:
            localremain -= 1 

            if (localremain == 1):
                if hint == "hint":
                    print('Check the textbook')
                if hint == "hint2":
                    print("notice the quotes!")
                if hint == "hint3":
                    print("Calcuate the right side first. Don't forget != means not equal to.")

        if (localremain == 0):
            print('You answered ' + "'" +  str(answer1)  + "'" + '. The correct answer is ' + "'" +  str(youranswer)  + "'" + '.')



        if answer == youranswer:
            print("Congratulations! You got it right.")
            correct += 1
            break
            
        else:
            print("You have this many remaining tries:",str(localremain))
   
            


askQuestion("question1", "c", "hint")
askQuestion("question2", "str", "hint2")
askQuestion("question3", "true", "hint3")


print("You tried " + str(tries) + " questions and got " + str(correct) + " right.")
            

    

    

    

        

