# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secr_w1=set(secret_word)
    secr_w2=set(secret_word)
    letters=set(letters_guessed)
    if letters.intersection(secr_w1)==secr_w2:
      return True
    else:
      return False





def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    str1=set(secret_word)
    lttrs=str1.difference(set(letters_guessed))
    str2=secret_word
    for l in lttrs:
      str2=str2.replace(l,"_ ")
    return(str2)
    




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    x=string.ascii_lowercase
    lttrs=list(letters_guessed)
    for l in lttrs:
      x=x.replace(l,"")
    return x

    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('Welcome to the game Hangman!')
    print("I am thinking of a word that is ",len(secret_word)," letters long.")
    guess=6
    warnings=3
    print('You have',warnings, ' warnings left.')
    print(f'{"-"*15}')

    holosni=['a', 'i', 'e', 'o', 'u']
    letters_guessed=[]
    end=False
    while end!=True:
      print('You have ',guess, ' guesses left.')
      print('Available letters: ',get_available_letters(letters_guessed))
     

      ltrs=str.lower(input('Please guess a letter: ').replace(' ',''))
      if ltrs.isalpha() :
        if len(ltrs)==1:
          
          if ltrs in secret_word and ltrs not in letters_guessed:
            letters_guessed.append(ltrs)
            print('Good guess:', get_guessed_word(secret_word, letters_guessed))
            print(f'{"-"*15}')
            if is_word_guessed(secret_word, letters_guessed)==True:
              print('Congratulations! You won! Your word: ', secret_word)
              print('Your total score: ', guess * len((list(set(secret_word)))))          
              end=True
          elif ltrs not in secret_word:
            if ltrs in holosni:

              if ltrs not in letters_guessed:
                letters_guessed.append(ltrs)
                print('Oops! That letter is not in my word:',get_guessed_word(secret_word, letters_guessed))
                guess-=2
                
                print(f'{"-"*15}')
                if guess<=0:
                    print('Sorry, you lost, your word: ', secret_word)
                    end = True
              
              elif ltrs in letters_guessed:
                warnings-=1
                if warnings>0 and warnings<3:
                  print("Oops! You've already guessed that letter. You now have", warnings, "warnings: ",get_guessed_word(secret_word, letters_guessed))
                  print(f'{"-"*15}')
            else:
              if ltrs not in letters_guessed:
                letters_guessed.append(ltrs)
                print('Oops! That letter is not in my word:',get_guessed_word(secret_word, letters_guessed))
                guess-=1
                
                print(f'{"-"*15}')
                if guess<=0:
                    print('Sorry, you lost, your word: ', secret_word)
                    end = True
              
              elif ltrs in letters_guessed:
                warnings-=1
                if warnings>0 and warnings<3:
                  print("Oops! You've already guessed that letter. You now have", warnings, "warnings: ",get_guessed_word(secret_word, letters_guessed))
                  print(f'{"-"*15}')


                
              elif warnings <=0:
                print('No more warnings has left: ',get_guessed_word(secret_word, letters_guessed))
                print(f'{"-"*15}')
                guess-=1
                
                
                if guess<=0:
                    print('Sorry, you lost, your word: ', secret_word)
                    end = True



             

          elif ltrs in letters_guessed:
              warnings-=1
              if warnings>0 and warnings<3:
                print('Oops! That is not a valid letter. You have' ,warnings, 'warnings left:',get_guessed_word(secret_word, letters_guessed))
                print(f'{"-"*15}')

                
              elif warnings <=0:
                print('No more warnings has left: ',get_guessed_word(secret_word, letters_guessed))
                print(f'{"-"*15}')
                guess-=1
              
                
                if guess<=0:
                    print('Sorry, you lost, your word: ', secret_word)
                    end = True
                  
               
        else:
          warnings-=1
          if warnings>0 and warnings<3:
            print('Oops! That is not a valid letter. You have' ,warnings, 'warnings left:',get_guessed_word(secret_word, letters_guessed))
            print(f'{"-"*15}')
          elif warnings <=0:
            print('No more warnings has left: ',get_guessed_word(secret_word, letters_guessed))
            print(f'{"-"*15}')
            guess-=1
            
            
            if guess<=0:
                print('Sorry, you lost, your word: ', secret_word)
                end = True
      else:
        warnings-=1
        if warnings>0 and warnings<3:
          print('Oops! That is not a valid letter. You have' ,warnings, 'warnings left:',get_guessed_word(secret_word, letters_guessed))
          print(f'{"-"*15}')
        elif warnings <=0:
          print('No more warnings has left:',get_guessed_word(secret_word, letters_guessed))
          print(f'{"-"*15}')
          guess-=1
          
          
          if guess<=0:
              print('Sorry, you lost, your word: ', secret_word)
              end = True

        

            
            
            
        












# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
  

    my_word = my_word.replace(" ", '')
    if len(my_word) != len(other_word):
       return False
    list_ltrs = []
    index = 0
    for i in my_word:
        
        if i!="_":
            list_ltrs.append(other_word[index])
        else:
            list_ltrs.append("_")
        index+=1
    a="".join(list_ltrs)
    if my_word == a:
       return True
    else: 
      return False


    
def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Possible matches are: ")
    for other_word2 in wordlist:
            word = match_with_gaps(my_word, other_word2)
            if word is True:
              print(other_word2, end = " ")

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('Welcome to the game Hangman!')
    print("I am thinking of a word that is ",len(secret_word)," letters long.")
    guess=6
    warnings=3
    print('You have',warnings, ' warnings left.')
    print(f'{"-"*15}')

    holosni=['a', 'i', 'e', 'o', 'u']
    letters_guessed=[]
    end=False
    while end!=True:
      print('You have ',guess, ' guesses left.')
      print('Available letters: ',get_available_letters(letters_guessed))
     

      ltrs=str.lower(input('Please guess a letter: ').replace(' ',''))
      if ltrs.isalpha() :
        if len(ltrs)==1:
          
          if ltrs in secret_word and ltrs not in letters_guessed:
            letters_guessed.append(ltrs)
            print('Good guess:', get_guessed_word(secret_word, letters_guessed))
            print(f'{"-"*15}')
            if is_word_guessed(secret_word, letters_guessed)==True:
              print('Congratulations! You won! Your word: ', secret_word)
              print('Your total score: ', guess * len((list(set(secret_word)))))          
              end=True
          elif ltrs in secret_word and ltrs in letters_guessed:
            warnings-=1
            if warnings>0 and warnings<3:
              print("Oops! You've already guessed that letter. You now have", warnings, "warnings: ",get_guessed_word(secret_word, letters_guessed))
              print(f'{"-"*15}')
            else:                 
                warnings <=0
                print('No more warnings has left: ',get_guessed_word(secret_word, letters_guessed))
                print(f'{"-"*15}')
                guess-=1

          elif ltrs not in secret_word:
            letters_guessed.append(ltrs)
            if ltrs in holosni:

              if letters_guessed.count(ltrs)==1 :
                
                print('Oops! That letter is not in my word:',get_guessed_word(secret_word, letters_guessed))
                guess-=2
                
                print(f'{"-"*15}')
                if guess<=0:
                    print('Sorry, you lost, your word: ', secret_word)
                    end = True
              
              elif letters_guessed.count(ltrs)>1:
                warnings-=1
                if warnings>0 and warnings<3:
                  print("Oops! You've already guessed that letter. You now have", warnings, "warnings: ",get_guessed_word(secret_word, letters_guessed))
                  print(f'{"-"*15}')
                else:                 
                    warnings <=0
                    print('No more warnings has left: ',get_guessed_word(secret_word, letters_guessed))
                    print(f'{"-"*15}')
                    guess-=1
            else:
              if letters_guessed.count(ltrs)==1:
                
                print('Oops! That letter is not in my word:',get_guessed_word(secret_word, letters_guessed))
                guess-=1
                
                print(f'{"-"*15}')
                if guess<=0:
                    print('Sorry, you lost, your word: ', secret_word)
                    end = True
              
              elif letters_guessed.count(ltrs)>1:
                warnings-=1
                if warnings>0 and warnings<3:
                  print("Oops! You've already guessed that letter. You now have", warnings, "warnings: ",get_guessed_word(secret_word, letters_guessed))
                  print(f'{"-"*15}')              
                elif warnings <=0:
                    print('No more warnings has left: ',get_guessed_word(secret_word, letters_guessed))
                    print(f'{"-"*15}')
                    guess-=1                
                    if guess<=0:
                        print('Sorry, you lost, your word: ', secret_word)
                        end = True



             

        
                  
               
        else:
          warnings-=1
          if warnings>0 and warnings<3:
            print('Oops! That is not a valid letter. You have' ,warnings, 'warnings left:',get_guessed_word(secret_word, letters_guessed))
            print(f'{"-"*15}')
          elif warnings <=0:
            print('No more warnings has left: ',get_guessed_word(secret_word, letters_guessed))
            print(f'{"-"*15}')
            guess-=1
            
            
            if guess<=0:
                print('Sorry, you lost, your word: ', secret_word)
                end = True
      elif ltrs=='*':
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        print('')
      elif ltrs.isalpha()==False:
        warnings-=1
        if warnings>0 and warnings<3:
          print('Oops! That is not a valid letter. You have' ,warnings, 'warnings left:',get_guessed_word(secret_word, letters_guessed))
          print(f'{"-"*15}')
        elif warnings <=0:
          print('No more warnings has left:',get_guessed_word(secret_word, letters_guessed))
          print(f'{"-"*15}')
          guess-=1
          
          
          if guess<=0:
              print('Sorry, you lost, your word: ', secret_word)
              end = True


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
  secret_word = choose_word(wordlist)
  hangman_with_hints(secret_word)
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    