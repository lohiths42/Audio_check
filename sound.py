import os
import winsound
import time

duration = 500

#the scoring variable is responsible for keeping track of the score.
score = 0

# frequencies that are to be tested can be appended into the below list. The program will abutomatically make
# changes wherever necessary
frequency = [400,500,800,1000,2000,4000,6000,8000]

for i in frequency:

    # The following two lines are responsible for generating a particular frequency
    print("Playing the frequency: "+str(i))
    winsound.Beep(i, duration)

    # We are taking the user response as input here and if the user presses y or Y, we update the score
    # varibale by 1.
    user_response = input("Did you hear the sound? Press Y or N: ")
    if user_response == "y" or user_response == "Y":
        score += 1

    # giving gap between successive frequencies
    print("Get ready for the next frequency")
    time.sleep(3)

print(" ")
print("Your total score is: "+str(score))

# calulating the efficiency. The denominator in the equation is declared as float so that "hearing_efficiency"
# becomes a float.
hearing_efficiency = (score/float(len(frequency)))*100

print("Your hearing efficieny is: "+str(hearing_efficiency)+"%")
