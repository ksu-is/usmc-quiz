""" following code is a program Quiz-Game in python.
    it contains 4 categories with 5 questions each.
    programmer: Jarvis Sturdivant
    github: jsturdi3
    email : jsturdi3@students.kenneaw.edu
    ************************* Jarvis Sturdivant ********************************
    Scores will be recorded, make every option Count ...
        ENJOY :)
#
"""

print("*** Yo! Welcome to the most USMC quiz by Jarvis Sturdivant***")
name = input(' WHATS YOUR NAME ? \n:')
print('WELCOME,', name)
ans = input('Are you ready?  (y/n): ')
score = 0
total_q = 5

if ans.lower() == 'y':
    print('On which topic would you like to test your brain? ')
    ans = input('a. Important Marines \nb. Important Battle \nc. Base Locations   \nd. Rank Structure \n(a/b/c/d): \n')

    if ans.lower() == 'a':
        print('** Welcome To The USMC-quiz** \n Their are 5 questions, Try to score max ')

        # 1
        print('1. Who was the first female Marine? ')
        ans = input('a. Opha May Johnson b. Carolyn White  c. Lauren Robinson d. Jade Sturdivant  \n')
        if ans.lower() == 'a':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is Opha May Johnson')

        print('2. Who was the first air pilot in the USMC  ?')
        ans = input('a. Jim Mathis b. K Kulack c. A.A Cunningham d. J Lash \n')
        if ans.lower() == 'c':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is A.A Cunningham')

        print('3. Who was the first Marine Corps Commandant?')
        ans = input('a. Chris Rock b. 4.Chesty Puller c. Anrold Archbad d.4.Samuel Nicholas \n')
        if ans.lower() == 'd':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is Samuel Nicholas')

        print('4. Who earn a medal of honor  ?')
        ans = input('a. Kyle Carpenter b. Chesty Puller c. Sean Combs d. Jim Mad Dog Mattis \n')
        if ans.lower() == 'a':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is Kyle Carpenter')

        print('5. Who was a general in the USMC and named as the Sectary of Defense ?')
        ans = input('a. Steve Smith b.Smearly Bulter  c. Jim Mad Dog Mattis d. Jim Kulekla \n')
        if ans.lower() == 'c':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is Jim Mad Dog Mattis')

        print('Thank you for playing, you got ', score, " questions correct.")
        Marks = (score / total_q) * 100

        print("Marks: ", Marks)
        if Marks > 70:
            print(" You are the next Commandant of the Marine Corp !!! ")
        elif Marks > 50:
            print("You Played Well NCO")
        elif Marks < 30:
            print("You Know Nothing PVT:(")
        print("Goodbye", name, ". It was nice having you :)")

    # 2
    elif ans.lower() == 'b':
        print('** Welcome To The Battle-quiz ** \n Their are 5 questions, Try to score max ')

        print('1. What  was name of the bar that the Marine Corp was created?')
        ans = input('a. Tun Tarvan b. Sempri Fi bar and grill c. Devil Dog  d. Rah rah \n')
        if ans.lower() == 'a':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is Tun Tarvan')

        print('2. What battle where the US marines were called devil dogs ?')
        ans = input('a. Iwa Jima b. Korea 10 c. Belleau Wood d. Gualdacanal \n')
        if ans.lower() == 'c':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is Belleau Wood')

        print('3. What was the name of the campaign in the pacfic?')
        ans = input('a. Ship to Shore campagin b. Hawaii Campagin c.Show of force Campagin d. Island hopping campagin \n')
        if ans.lower() == 'd':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is Island Hopping Campagin')

        print('4. What was the name of the battle that was called ambush alley?')
        ans = input('a. Bagdad b. Nasiriyah c. Ramadi d. Barsaha \n')
        if ans.lower() == 'b':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is Nasiriyah')

        print('5. The average person has over how many DREAMS a year ?')
        ans = input('a. 2,567 b. 1,460 c. 2,141 d. 9,999 \n')
        if ans.lower() == 'b':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is 1,460')

        print('Thank you for playing, you got ', score, " questions correct.")
        Marks = (score / total_q) * 100

        print("Marks: ", Marks)
        if Marks > 70:
            print(" You are the next Commandant !!! ")
        elif Marks > 50:
            print("You Played Well NCO")
        elif Marks < 30:
            print("You Know Nothing PVT :(")
        print("Goodbye", name, ". It was nice having you :)")

    # 3
    elif ans.lower() == 'c':
        print('** Welcome To The Base Location-quiz ** \n Their are 5 questions, Try to score max ')

        print('1. What is the base named in N.C that is located in Jacksonville ?')
        ans = input('a. Camp Fox b. Parris Island c. Camp Legune d. Fort Jackson \n')
        if ans.lower() == 'c':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is Camp Leguene')

        print('2. What base is located in Oceanside Ca ?')
        ans = input('a. Miramar b. Camp Pendelton c. 29 Palms d. Corridor \n')
        if ans.lower() == 'b':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is Camp Pendelton')

        print('3. what base is located in the Mohve Desert ?')
        ans = input('a. 29 Palms b Yuma MCAS c. EL Torro d. Tripler \n')
        if ans.lower() == 'a':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is 29 Palms')

        print('4. Kanehoe Bay is located in what state?')
        ans = input('a. Ca b. Japan c. HI d. Fl \n')
        if ans.lower() == 'c':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is HI')

        print('5. Camp Bulter is located where ?')
        ans = input('a. Germany b. Korea c. Thaliand d. Japan  \n')
        if ans.lower() == 'd':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is Japan')

        print('Thank you for playing, you got ', score, " questions correct.")
        Marks = (score / total_q) * 100

        print("Marks: ", Marks)
        if Marks > 70:
            print(" You are the next Commandant !!! ")
        elif Marks > 50:
            print("You Played Well")
        elif Marks < 30:
            print("You Know Nothing PVT :(")
        print("Goodbye", name, ". It was nice having you :)")

    # 4
    elif ans.lower() == 'd':
        print('** Welcome To The History-quiz ** \n Their are 5 questions, Try to score max ')

        print('1. Where did Marines first serve at ?')
        ans = input('a. Tanks b. Ships c. Infantry d. cars \n')
        if ans.lower() == 'b':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is Ships')

        print('2. How many years Leonardo Da Vinci took to paint MONA LISA ?')
        ans = input('a. 18 b.15 c. 10 d. 2 \n')
        if ans.lower() == 'c':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is 10')

        print('3. The Eagle Globe and anchor was adopted ?')
        ans = input('a. 1868 b. 1821 c. 1762 d. 1811 \n')
        if ans.lower() == 'a':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is 1868')

        print('4. What department is shared with the Marine Corps ?')
        ans = input('a. Army b. Air force c. Costal Guard d. Navy \n')
        if ans.lower() == 'd':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is Navy')

        print('5. Marines say what slogan  ?')
        ans = input('a. yahyah b. whoyah c. Rahrah d. Urah \n')
        if ans.lower() == 'd':
            score += 1
            print('Correct :)')
        else:
            print('Incorrect :(')
            print('Correct answer is Urah')

        print('Thank you for playing, you got ', score, " questions correct.")
        Marks = (score / total_q) * 100

        print("Marks: ", Marks)
        if Marks > 70:
            print(" You are the next Commandant !!! ")
        elif Marks > 50:
            print("You Played Well NCO")
        elif Marks < 30:
            print("You Know Nothing PVT :(")
            print("Goodbye", name, ". It was nice having you :)")

if ans.lower() == 'n':
    print("Sad to see you leave :(")
