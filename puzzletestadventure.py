"""CSC111 Project 1: Text Adventure Game

Instructions (READ THIS FIRST!)
===============================

This Python module contains the code for Project 1. Please consult
the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""

# Note: You may add in other import statements here as needed
from game_data import World, Item, Location, Player
import random
import time


# Note: You may add helper functions, classes, etc. here as needed

def intro() -> None:
    """
    Intro for the game
    """
    print('Welcome to "EXAMINATION STRESSATION"!')
    time.sleep(2)
    print('You\'ve got an important exam coming up this evening, and you\'ve been studying for weeks!')
    time.sleep(2)
    print('Last night was a particularly late night on campus.')
    time.sleep(2)
    print('You had difficulty focusing, so rather than staying in one place, you studied in various places throughout '
          'campus as the night progressed.')
    time.sleep(2)
    print('Unfortunately, when you woke up this morning, you were missing some important exam-related items.')
    time.sleep(2)
    print('You cannot find your T-card, and you\'re nervous they won\'t let you into tonight\'s exam without it!')
    time.sleep(2)
    print('Also, you seem to have misplaced your lucky exam pen -- even if they let you in, you can\'t possibly write '
          'with another pen as good as that one! ')
    time.sleep(2)
    print('Finally, your instructor for the course lets you bring a cheat sheet - a handwritten page of information '
          'in the exam.')
    time.sleep(2)
    print('Last night, you painstakingly crammed as much material onto a single page as humanly possible, but that\'s '
          'missing, too!')
    time.sleep(2)
    print('All of this stuff must be around campus somewhere! Can you find all of it before your exam starts tonight?')
    time.sleep(2)
    print('Not only are those things, maybe some coffee around campus will help too! What else will you find?')
    time.sleep(3)


class SirDaniel:
    """Class for the UC puzzle

    Instance Attributes:
        - talked_to:
            Whether or not the player has talked to them before
        - completed:
            Whether or not the player has completed the challenge
    """
    talked_to: bool
    completed: bool

    def __init__(self, talked_to: bool, completed: bool) -> None:
        """Initialize a new item.
        """
        self.talked_to = talked_to
        self.completed = completed

    def speak(self) -> None:
        """Dialogue of Sir Daniel
        """
        if not self.talked_to:
            print('You can ask: \n1. Can Whitney tell the truth better than Morrison?')
            print('\n2. Is this a correct statement: You are the truth-teller or Whitney is the flip-flopper?')
            print('\n3. If I asked you if the Whitney door leads to my key, would you answer yes?')
            print('\n4. Would your exact opposite say this door leads to my key')
            inp = input()
            if inp == 1:
                print('Yes.')
            elif inp == 2:
                print('No.')
            elif inp == 3:
                print('Yes.')
            elif inp == 4:
                print('No.')
            else:
                print('Invalid input, please try again')
                self.speak()
            self.talked_to = True


class Whitney(SirDaniel):
    """Class for the UC puzzle
    """

    def __init__(self, talked_to: bool, completed: bool) -> None:
        """Initialize a new item.
        """
        super().__init__(talked_to, completed)

    def speak(self) -> None:
        """Dialogue of Whitney
        """
        if not self.talked_to:
            print('You can ask: \n1. Can you tell the truth better than Morrison?')
            print('\n2. Is this a correct statement: You are the truth-teller or Morrison is the flip-flopper?')
            print('\n3. If I asked you if your door leads to my key, would you answer yes?')
            print('\n4. Would your exact opposite say this door leads to my key')
            inp = input()
            if inp == 1:
                print('Yes.')
            elif inp == 2:
                print('Yes.')
            elif inp == 3:
                print('Yes.')
            elif inp == 4:
                print('No.')
            else:
                print('Invalid input, please try again')
                self.speak()
            self.talked_to = True

    def chosen(self) -> None:
        """What happens if Whitneu's door is chosen"""
        print('Congratulations, you chose the right door!!')
        print('You shall be rewarded with your key!!')


class Morrison(SirDaniel):
    """Class for the UC puzzle
    """

    def __init__(self, talked_to: bool, completed: bool) -> None:
        """Initialize a new item.
        """
        super().__init__(talked_to, completed)

    def speak(self) -> None:
        """Dialogue of Morrison
        """
        if not self.talked_to:
            print('You can ask: \n1. Can Whitney tell the truth better than you?')
            print('\n2. Is this a correct statement: You are the truth-teller or Whitney is the flip-flopper?')
            print('\n3. If I asked you if the Whitney door leads to my key, would you answer yes?')
            print('\n4. Would your exact opposite say this door leads to my key')
            inp = input()
            if inp == 1:
                print('No.')
            elif inp == 2:
                print('Yes.')
            elif inp == 3:
                print('Yes.')
            elif inp == 4:
                print('No.')
            else:
                print('Invalid input, please try again')
                self.speak()
            self.talked_to = True

    def chosen(self) -> None:
        """What happens when Morrison's door is chosen"""
        print('You have chosen the wrong door HAHAHAHAHAHA we have tricked you')


# Note: You may modify the code below as needed; the following starter template are just suggestions
if __name__ == "__main__":
    w = World('map.txt', 'locations.txt', 'items.txt')
    p = Player(15)
    menu = ["LOOK", "INVENTORY", "SCORE", "QUIT"]
    visited_places = []
    moves = 0
    sd = SirDaniel(False, False)
    wh = Whitney(False, False)
    mo = Morrison(False, False)
    oh = False
    intro()
    while not p.victory:
        if moves == 100:
            print('You check your watch suddenly see that its time to take your exam!')
            time.sleep(1)
            print('You hurridly run to the exam center, oh no are you going to be late???')
            time.sleep(1)
            print('You run to the front door and it is is LOCKED! It seems that all that studying was worth nothing!')
            time.sleep(1)
            print('Better luck next time!')
            print(f'Your score is: {p.score(moves, True, set(visited_places))}, better luck next time')
            time.sleep(1)
            print('You also failed your exam :(, better luck next time!')
            time.sleep(1)
            print('Thank you for playing!')
            time.sleep(1)
            exit()
        elif moves == 85:
            print('You check your watch and its getting close to exam time!')
            time.sleep(1)
            print('You better head over soon!')
            time.sleep(1)
        location = w.get_location(p.x, p.y)
        print(location.name)
        if (p.x, p.y) not in visited_places:
            print(location.l_desc)
        else:
            print(location.s_desc)
        visited_places.append((p.x, p.y))
        print("What to do?")
        print("MENU")
        print(location.cmds)
        choice = input("\nEnter action: ")
        while choice.upper() != 'MENU' and choice.upper() not in location.cmds:
            print('\n')
            print('Sorry that is not a valid response')
            time.sleep(1)
            print("What to do? \n")
            print("MENU")
            print(location.cmds)
            choice = input("\nEnter action: ")
        if choice.upper() == "MENU":
            print("Menu Options: \n")
            for option in menu:
                print(option)
            choice = input("\nChoose action: ")
            while choice.upper() not in menu:
                print('\n')
                print('Sorry that is not a valid response')
                time.sleep(1)
                print("Menu Options: \n")
                for option in menu:
                    print(option)
                choice = input("\nChoose action: ")
        if choice.upper() == 'NORTH':
            p.move(0, -1)
        elif choice.upper() == 'EAST':
            p.move(1, 0)
        elif choice.upper() == 'SOUTH':
            p.move(0, 1)
        elif choice.upper() == 'WEST':
            p.move(-1, 0)
        elif choice.upper() == 'TEST':
            p.victory = True
            break
        elif choice.upper() == 'RETURN':
            p.x, p.y = visited_places[-1]
        elif choice.upper() == 'WALK':
            p.x = 4
            p.y = 11
        elif choice.upper() == 'ENTER':
            if location.side:
                p.move(-1, 0)
            else:
                p.move(1, 0)
        elif choice.upper() == 'LEAVE':
            if location.side:
                p.move(1, 0)
            else:
                p.move(-1, 0)
        elif choice.upper() == 'UP':
            if location.num == 18:
                if 'T-CARD' not in p.show_inventory():
                    print('Sorry you can\'t enter without your T-CARD')
                else:
                    p.move(0, -1)
            else:
                p.move(0, -1)
        elif choice.upper() == 'DOWN':
            p.move(0, 1)
        elif choice.upper() == 'SEARCH':
            if location.num == 16:
                print('You look around the silent reading room where you were sitting')
                time.sleep(1)
                print('The area is comepletly empty, not a single thing there but a table and a chair')
                time.sleep(1)
                print('You look closely and see some writing on the table')
                time.sleep(1)
                print("Traverse another floor if you're kind, and a jacket you shall find")
                time.sleep(1)
            elif location.num == 15:
                print('You walk into the big open area, its crowded with students, you head over to the light area')
                time.sleep(1)
                print('You see a few people sitting there but suddenely recognize something')
                time.sleep(1)
                print('You stare from afar as you look at that pattern, you decide to go a little closer')
                time.sleep(1)
                print('You found your lost jacket!!')
                time.sleep(1)
                w.get_item(p, 7)
            elif location.num == 21:
                print('You look around the area where the stack of printer paper is')
                time.sleep(1)
                print('There is paper all over the floor and all over the desk, it\'s quite messy')
                time.sleep(1)
                print('You see a paper with some writing on it an walk over')
                time.sleep(1)
                print('You found your cheat sheet!')
                time.sleep(1)
                w.get_item(p, 4)
            elif location.num == 25:
                print('You climb up the stairs to the second floor')
                time.sleep(1.5)
                print('You climb up the stairs to the third floor')
                time.sleep(1.5)
                print('You walk over to where you were sitting and see something blue on the floor')
                time.sleep(1)
                print('You found your TCard!!')
                time.sleep(1)
                w.get_item(p, 0)
            else:
                if 'Lucky Pen' not in p.show_inventory():
                    print('You find a whiteboard, with a sentence mysteriously written on it: ')
                    time.sleep(0.5)
                    print('If it is a pen you wish to have, then you may find such in a lab')
                else:
                    print("You search the area but only find stacks of papers")
                    time.sleep(0.5)
                    print("You get the sense you won't find anything here, your instincts tell you to leave")

        elif choice.upper() == 'ATTEND':
            if location.num == 23:
                if 'Suit and Tie' in p.show_inventory():
                    print("The Rotman people are pleased with your dapper look!")
                    time.sleep(1)
                    print('They have accepted you into their ranks')
                    time.sleep(1)
                    print('And they have a gift for you, a special golden pen!')
                    time.sleep(1)
                    w.get_item(p, 5)
                else:
                    print("The Rotman people are dissapointed that you're not dressed for the part")
            else:
                if not oh:
                    print('You walk into your room for your professor\'s office hour.')
                    time.sleep(1)
                    print('There are a bunch of people standing around your professor as they\'re speaking.')
                    time.sleep(1)
                    print('you listen along to what he says.')
                    time.sleep(1)
                    print('.', end='')
                    time.sleep(1)
                    print('.', end='')
                    time.sleep(1)
                    print('.', end='')
                    time.sleep(1)
                    print('Your professor finishes his last minute talk about the exam material and everyone claps.')
                    time.sleep(1)
                    print('You believe you gained more knowledge from it and that you\'ll do better on your test.')
                    time.sleep(1)
                    oh = True
                else:
                    print('You walk into the room your professor holds office hours in, it is completely empty.')
                    time.sleep(1)
                    print('There\'s nothing to do so you leave.')
                    time.sleep(1)
        elif choice.upper() == 'PLAY':
            print('WELCOME EVERYBODY TO TODAYS UOFT HISTORY GAME SHOW!!!!')
            time.sleep(0.5)
            print('My name is Ramsey and I will be your host for today!')
            time.sleep(1)
            name = input('Today we have a very special contest, this person who seems to be looking for something, '
                         'please tell us your name: ')
            print(f'Please everybody give a big round of applause tooooooo {name.upper()}!!!!!!')
            time.sleep(1)
            print(f'{name}, your first question is: What year was the UofT founded?')
            q1 = input('Answer: ')
            if q1 == 1827:
                print('You got the first question correct!')
                time.sleep(1)
                q1 = True
            else:
                print('INCORRECT! The correct answer is "1827"')
                q1 = False
            print('Your next question will be what is the oldest building in continous academic use at UofT?')
            q2 = input('Answer: ')
            if q2.lower() == 'odette hall' or q2.lower() == 'odette':
                print('You got the second question correct!')
                time.sleep(1)
                q2 = True
            else:
                print('INCORRECT! The correct answer is "Odette Hall"')
                q2 = False
            print('And your last question is, who was the first president of UofT?')
            q3 = input('Answer: ')
            if q3.lower == 'john strachan' or q3.lower == 'john' or q3.lower == 'strachan':
                print('You got the second question correct!')
                time.sleep(1)
            else:
                print('INCORRECT! The correct answer is "John Strachan"')
                q3 = False
            print(f'EVERYBODY GIVE {name.upper()} A HUGE ROUND OF APPLAUSE!!')
            time.sleep(1)
            if q1 and q2 and q3:
                print('They got everything correct and won a coupon to our school store worth FIFTY DOLLARS!!!!')
                w.get_item(p, 9)
            else:
                print('They tried their hardest and since they didnt get every question right, they get a hi-five!')
        elif choice.upper() == 'BUY':
            print("You're at the Sidney Smith Second Cup")
            time.sleep(0.5)
            item = input('1. Caramel Frappachino $10\n2. Decaffeinated Coffee $5\n3. Leave')
            while item != 1 or 2 or 3:
                item = input('Please enter a valid input: ')
            if item == 1 and p.money >= 10:
                p.money -= 10
                w.get_item(p, 1)
            elif item == 2 and p.money >= 5:
                p.money -= 5
                w.get_item(p, 2)
            elif item == 3:
                print('You leave without buying anything.')
            else:
                print('Sorry you don\'t have enough money for that item!')
            time.sleep(1)
        elif choice.upper() == 'RENT':
            print('You walk up to the attendant and ask them what their prices are')
            time.sleep(1)
            print('You can rent a suit if you have $10')
            time.sleep(0.5)
            i = input('Rent a suit?\n1. Yes\n2. No\n')
            while i != 1 or i != 2:
                print('That is not a valid option!')
                i = input('Rent a suit?\n' + '1. Yes\n' + '2. No\n')
            if i == 1 and p.money > 5:
                w.get_item(p, 3)
            elif i == 1:
                print('You do not have enough money')
        elif choice.upper() == 'CHALLENGE' and not sd.completed:
            if sd.talked_to:
                sd.talked_to = False
                mo.talked_to = False
                wh.talked_to = False
            print('One of the three spirits of UC has your key\n but trickery is abound...\n')
            print('One spirit always tells the truth, another always lies, and the third can lie or tell the truth\n')
            print("You don't know which spirit is which, but they do")
            print("You can pick between a group of yes/no questions for two distinct spirits")
            if location.num == 8:
                # this is the joker
                if not sd.talked_to:
                    temp = input("Enter 'yes' to talk to Sir Daniel")
                    if temp.upper() == 'YES':
                        sd.speak()
                else:
                    print('You have already talked to Sir Daniel')
                # write smth to choose between options?
            elif location.num == 6:
                # this is the one that always lies
                if not mo.talked_to:
                    temp = input("Enter 'yes' to talk to Morrison")
                    if temp.upper() == 'YES':
                        mo.speak()
                else:
                    ans = input("Enter 'yes' if you wish to choose my door, otherwise you will leave")
                    if ans.upper() == 'YES':
                        mo.chosen()
            else:
                # this is the one that always tells the truth
                if not wh.talked_to:
                    temp = input("Enter 'yes' to talk to Whitney")
                    if temp.upper() == 'YES':
                        wh.speak()
                else:
                    ans = input("Enter 'yes' if you wish to choose my door, otherwise you will leave")
                    if ans.upper() == 'YES':
                        wh.chosen()
                        sd.completed = True
                        w.get_item(p, 10)
        elif choice.upper() == 'LOOK':
            print(location.l_desc)
        elif choice.upper() == 'SCORE':
            print(f'Your current score is: {p.score(moves, False, set(visited_places))}')
            time.sleep(2)
        elif choice.upper() == 'INVENTORY':
            p.print_inventory()
            time.sleep(1)
        elif choice.upper() == 'QUIT':
            print('Thank you for playing!')
            exit()
        if location.side != w.get_location(p.x, p.y).side:
            if random.randint(0, 10) >= 3:
                g_light_phrases = ['It\'s a green light! You have to wait for the light to turn red.',
                                   'ZOOOM! A car just drove by, better wait until the cross walk is safe!',
                                   'Aw, just in time to miss the red light, now you have to wait to cross!']
                print(random.choice(g_light_phrases))
                time.sleep(1)
                print('.', end='')
                time.sleep(1)
                print('.', end='')
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('The cars all stopped and it\'s safe to cross!')
                time.sleep(1)
            else:
                print('Its a red light! You can cross the street with no worries!')
                time.sleep(1)
        elif w.get_location(p.x, p.y).num not in range(15, 27):
            actions = ['REST', 'CONTINUE']
            if random.randint(1, 20) >= 1:
                rest_num = 0
                while rest_num != 3:
                    print(
                        'You are at an intersection with a bench, it has been a long day, you can choose to either rest'
                        ' or cross and continue.')
                    print('What to do?')
                    print(actions)
                    choice = input("\nEnter action: ")
                    while choice.upper() not in actions:
                        print('That is not a valid option!')
                        time.sleep(1)
                        print('You are at an intersection with a bench, it has been a long day, you can choose to '
                              'either rest or cross and continue.')
                        print('What to do?')
                        print(actions)
                        choice = input("\nEnter action: ")
                    if choice.upper() == 'CONTINUE':
                        break
                    else:
                        print('You sit and rest for a minute')
                        time.sleep(1)
                        print('.', end='')
                        time.sleep(1)
                        print('.', end='')
                        time.sleep(1)
                        print('.')
                        time.sleep(1)
                        rest_num += 1
                if rest_num == 3:
                    print('You\'re sitting on the bench, enjoying the sounds of cars and students talking')
                    time.sleep(1)
                    print('Suddenly you see Josh, a friend of yours, show up!')
                    time.sleep(1)
                    print('Josh asks you how you are and hands you an energy drink, he bought two from a BOGO!')
                    time.sleep(1)
                    print('You have obtained an energy drink!')
                    w.get_item(p, 8)
        moves += 1
    print('Congratulations for making it to your test on time!')
    time.sleep(1)
    print('You will now take your test, good luck!')
    time.sleep(1)
    if 'T-CARD' in p.show_inventory():
        time.sleep(1)
        score = p.score(moves, False, set(visited_places))
        print(f'You final score is: {score}')
        time.sleep(1)
        if score >= 50:
            print('You passed your exam with flying colors, congratulations!!!')
        else:
            print('You barely passed your exam, even with all that studying, still congrats!!!!')
        time.sleep(1)
        print('Thank you for playing!')
        time.sleep(1)
        exit()
    else:
        print('Sorry, you don\'t have your T-CARD, we can\'t let you take the test!')
        time.sleep(1)
        print(f'Your score is: {p.score(moves, True, set(visited_places))}, better luck next time')
        time.sleep(1)
        print('You also failed your exam :(, better luck next time!')
        time.sleep(1)
        print('Thank you for playing!')
        time.sleep(1)
        exit()
