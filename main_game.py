import random as rand
########
# Command Line Game designed by my 7 year-old sister. Programming done by ChuckyNTG.
#
#
#######

#Add points for correctanswers, powerups for hard questions if you have enough points
#Dress up person with hats
incomplete_sentences = ['The dog ___ outside','I swam ___ dad','My dad ___ leaves outside','I went trick-or-treating with ___ ___ ___','Dad and I put up the ___ on the tree','At midnight, we opened all our ___']
solutions = ['ran','with','raked','Mom and Dad','star']
word_choices = [['ran','played','flew','fell'],['outside','away','with','above'],['used','hugged','smacked','raked'],['Ghost and Mummy','Devil and God','Neighbors','Mom and Dad'],['Strawberry','Eyeball','Cat','Star'],['Beers','rifles','wallets','presents']]

sentences = zip(incomplete_sentences, solutions, word_choices)
powerups_choose_word = [('Skip Level',9),('Give Hints',2),('Remove all but two',6)]

def check_spelling(word):
    user_written = raw_input("Enter the spelling for the word:")
    
    if user_written.lower() == word.lower():
        return True 
    else:
        return False


def play_again():
    while True:
        play_again = raw_input("Would you like to play again(Y/N)?") 
        if play_again.lower() in ['y','yes']:
            return True
        elif play_again.lower() in ['n','no']:
            print 'Goodbye, {0}'.format(name)
            return False
        else:
            print 'Your choice is invalid! Please choose again!'
            continue

def spelling_game():

    hand_coins = 10
    #Voice reading

    while True:
        if len(sentences) != 0:
            sentence = rand.choice(sentences)
            sentences.remove(sentence)
            word_list = sentence[2]
        else:
            print 'No more sentences!'
            break

        print 'Please finish this sentence by entering a number!:\n'
        print '{0}\n'.format(sentence[0])
        print '1. {0}\t\t2.{1}\n3. {2}\t\t4.{3}\n'.format(word_list[0], word_list[1], word_list[2], word_list[3])
        
        print 'Choose powerups:'
        for index, powerup in enumerate(powerups_choose_word):
            print '{0}{0}. {1}'.format(index+1,powerup[0])
        print '\n'

        while True:
            try:
                choice = int(raw_input("Enter Your Choice:"))
                print 'You chose {0}'.format(word_list[choice-1]) 
                break
               #input validation on choice
            except ValueError:
                print 'Please enter a number for your choice'
                continue 
            except IndexError:
                print 'Your choice {0} is invalid'.format(choice)
                continue

        #check if the word is the right word
        if sentence[1] == word_list[choice-1]:
            print 'You chose right! Have 10 coins!'
            hand_coins += 10
            #Ask the user to spell the word
            while True:
                print 'Please spell the word: {0}'.format(word_list[choice-1])
                if check_spelling(word_list[choice-1]):
                    print 'Nice Job! You spelled the word right!'
                    hand_coins += 20
                    break
                else:
                    print 'You spelled it wrong, please try again! You have lost 3 coins.'
                    hand_coins -= 3
                    continue
        else:
            print 'You chose wrong! You have lost 2 coins. Please try again.'
            hand_coins -= 2
            continue


        print 'You have {0} coins'.format(hand_coins)
        if play_again():
            continue
        else:
            break

if __name__ == '__main__':

    name = raw_input("Enter Your Name:")
    print 'Hello, {0}'.format(name)
    spelling_game()
    exit()
