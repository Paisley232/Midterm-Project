susNames = ["Alayna", "Josh", "Maya", "Hannah", "Nathan", "Ben", "Reethika", "Jamin", "Chase"]
dob = ["02/14/2004" , "05/21/1982" , "07/26/2001" , "03/11/2002" , "08/03/2008" , "05/21/1982" , "04/01/2001" , "12/22/2006" , "10/02/1981"]
clockedIn = [8 , 8 , 8 , 10 , 10 , 8]


def intro():
    print("Welcome Detective! We are so grateful to have you on this case. \nWe have found a body at the Wyland Inc. office today on 10/06/2026. Here's what we know.\n\nVictim is female and apparently an office worker. We haven't identified the body yet. \nShe was found in the women's bathroom at 9:45 am and we now know that \nShe was killed around 9:00 am it looks like from fatal bowel movement.. \nShe had an empty coffee cup so we suppose she was poisoned through that.\nThe Scranton police department is low on staff so we really need you. \n\nI am captain Kirk. I will be assisting you on this case.")

def firstRoom():
    #user sees the info on the id including the person's birthday and user has to 
    #calculate the victims age then they type it out as an integer
    # output would be saying if they are a suspect or not (eliminate 5- 6 left)

    print("According to the owner of the company, this morning was shipment day. \nAll those who were working in the warehouse and were accounted for during the killing are 22 and younger. \nBut she could have gone up to the office to use the restroom. So we really just need to figure out her age.\n\nDetective, can you please check if she has a wallet with an ID? \n\nBROOKLYN COMACHO-------------------------------DOB: 04/18/2000\n Ok now we know she is over 22 and was working in the office that morning. \nLet's see who else would have been in the office. Could you check the worker's birthdays for me?")
    i = 0
    susNamesCopy = susNames.copy()

    for name in susNames:
        print(name + "-------------------------------DOB:" + dob[i])

        year = dob[i].split("/")[2]
        age = 2026 - int(year)
        suspectAge = input("How old is the suspect? ")

        while(suspectAge != str(age)):
            print("That is not correct try again. ")
            suspectAge = input("How old is the suspect? ")
            age = 2026 - int(year)
        i = i+1

        if int(suspectAge) <= 22:
            susNamesCopy.remove(name)
            print("They are NOT a SUSPECT")
        else:
            print("They are A SUSPECT")

    print("The suspects are Josh, Maya, Hannah, Ben, Reethika, Chase")
    return susNamesCopy

def secondRoom(susNames):
    #shows the user the time stamps of the office and asks the user one by one who was in the office 
    # at 9:00 am that day
    #output would say correct or incorrect for each person (eliminate 2- 4 left)

    print("\nGreat work detective! That sure narrows it down. Now we need to see who was clocked into the office \nwhen the murder was committed. Here is the clock in times of each \nsuspect from this morning. They aren't able to get into the building without \nclocking in with their ID card. Let me know what you come up with.")
    i = 0

    for name in susNames:
        time = clockedIn[i]
        print(name + ": " + str(time))

        if time < 9:
            print("They are A SUSPECT\n")
        else:
            print("They are NOT A SUSPECT\n")

        i = i + 1
    print("The suspects are Josh, Maya, Hannah, Chase")


def thirdRoom(): 
    #user types a name from the remaining suspects
    #output lists the items in each locker as they ask about each person
    #user has to put in the one suspenct that can be eliminated (eliminate 1- 3 left)

    print("We've got a permit to search the building. Can you start with the suspect's lockers? \nLook for anything suspicious. Whose should we check first? \n(Type Done when finished investigating)")

    name = ""
    name = input("Who should we first ask? ").upper()

    while name != "DONE":
        if name == "JOSH":
            print("coke zero\nbasketball\nsneakers")
        elif name == "MAYA":
            print("hairbrush\nempty of laxatives\npurse")
        elif name == "HANNAH":
            print("stuffed animal\nhair oil\nsingular super long wavy brown hair")
        elif name == "CHASE":
            print("Earbuds\nbook\nbinoculars")
        else:
            print("They are not a suspect")
        name = input("Who should we ask next? Type Done if finished investigating. ").upper()

    suspect = input("Okay, now you have some clues. Analyze it and ask yourself : Who is no longer a suspect? ").upper()
    while suspect != "JOSH":
        suspect = input("INCORRECT! Who is no longer a suspect? ").upper()


def fourthRoom():
    #user gets a list of the remaining suspects and a list of 3 questions for each suspect that is numbered
    #user only gets to ask each suspect 1 question 
    #user types integers of the number for each question they want to ask
    #user then types a string for the usspect they want to eliminate (eliminate 1- 2 left)
    #output is the answers of the suspects

    print("Nice work detective. But we're running out of hours in the day. \nI think all that is left to do today is conduct some interviews. \n\nHere is a list of questions I suggest you ask them try to stick with them. \nWe're running out of time. I'll give you one question per person. \n\nHere are the questions: \n1)What is your relation to Brooklyn?\n2)Where were you at 9 AM this morning?\n3)What is Brooklyn's favorite morning drink?  \n\nBe sure to ask the right questions or this could cost us the case.")

    count = 0 
    oldName = []

    while count < 3:
        name = input("Who do you want to talk to? ").upper()
        while (name in oldName):
            name = input("Choose a different person. Who do you want to talk to? ") .upper()
        oldName.append(name.upper())

        if name == "MAYA":
            num = input("Ok, now type the number of the question you want to ask.")
            if num == "1":
                print("I didn't know her very well but she seemed very nice. She was a very good worker.")
            elif num == "2":
                print("I was in the bathroom I think. Someone was definitely blowing it up though...")
            elif num == "3":
                print("I think maybe orange juice?")
            else:
                print("That is not a valid number. Choose a number 1-3.")
            count = count + 1

        elif name == "HANNAH":
            num = input("Ok, now type the number of the question you want to ask.")
            if num == "1":
                print("Uhh oh yeah we were best friends! I am going to miss her sooo much!!")
            elif num == "2":
                print("I was talking to Chase at his cubicle. I had soooo many questions about his vacation! \nHe loves all my questions.")
            elif num == "3":
                print("Coffee.")
            else:
                print("That is not a valid number. Choose a number 1-3.")
            count = count + 1

        elif name == "CHASE":
            num = input("Ok, now type the number of the question you want to ask.")
            if num == "1":
                print("I have always had a bit of a crush on her but I don't know how she felt about me. ")
            elif num == "2":
                print("I was at my cubicle quietly doing my work.")
            elif num == "3":
                print("Most people drink coffee right?")
            else:
                print("That is not a valid number. Choose a number 1-3.")
            count = count + 1

        else:
            print("That is not a suspect. ")

    suspect = input("Good job detective! You have enough clues to eliminate someone. Who is no longer a suspect?").upper()

    while suspect != "CHASE":
        suspect = input("INCORRECT! Who is no longer a suspect?").upper()

def fifthRoom():
    #user gets a written note that says "go to my desk I am innocent I know who did it though, 
    # I wrote the letters around in red to stay anonymous.
    #user writes in string the person of the desk to go to
    #output either shows the red letters and the user has to put in the correct string to scramble 
    # the words into the killer's name or if the user chose the killer's desk
    #output shows that the user dies

    print("Wait detective!! What is that under the chair suspect?? Can you go check that out for me?\n Thank you. Let's look at what it says.\n \nI am innocent but i know who the killer is \nand i think they are framing me. I couldn't tell you \nhere because i think they would kill me. Go \nto my desk and look for the red letters. \nThere you will find the answer. \n \nYou can go check this out, right detective? \nI'll stay here at the station and uhh look at more of this evidence.. \n\nBe careful! The lights are usually automatically off this time at night in the office. ")

    name = input("There are two suspects remaining, who's cubicle do you want to go to Maya or Hannah? This is a life or death decision!").upper()

    if name == "MAYA":
        print("A\nA\nH\n Congratulations, you are safe! The killer is Hannah!!")
    else:
        print("OH NO!! Someone just poisoned you! \nYou did not choose the innocent person's desk... \nIt was Hannah the whole time!! She liked Chase but he liked Brooklyn!! \n12 So she poisoned her with laxatives and framed Maya by putting the empty bottle in her locker.\n\n\n You fall to the ground and die.")






def main():
    intro()
    secondRoom(firstRoom())
    thirdRoom()
    fourthRoom()
    fifthRoom()

if __name__ ==  "__main__":
    main()