words=["Haldimond County","Prince Edward County","Regina","Cranbrook","Mount Vernon","Amsterdam","Thiruvananthapuram","Gandhinagar","Shillong"]
hints1={"Haldimond County":"Canada","Prince Edward County":"Canada","Regina":"Canada","Cranbrook":"Canada","Mount Vernon":"USA","Amsterdam":"USA","Thiruvananthapuram":"India","Gandhinagar":"India","Shillong":"India"}
hints2={"Haldimond County":"Ontario","Prince Edward County":"Ontario","Regina":"Saskatchewan","Cranbrook":"British Columbia","Mount Vernon":"Alabama","Amsterdam":"New York","Thiruvananthapuram":"Tamilnadu","Gandhinagar":"Gujarat","Shillong":"Meghalaya"}
import random
word_random=random.choice(words)
chances=5
hints=2
already_guessed=""
word_developing=""
for wor in word_random:
    if wor.isalpha():
        word_developing=word_developing+"-"
    elif wor.isspace():
        word_developing=word_developing+" "
word_developing=word_developing.rstrip()
rules="""RULES:
You will be given 5 chances to guess the city name that is either in Canada, USA or in India.
If you type a letter which is in the word selected by the system, the number of chances left will remain the same.
You will have 2 hints to use at any point of time; the hints will reveal, first the country, then the state of the city.
If you run out of chances, you will lose.
GOOD LUCK!"""
print(rules,"\n")
print(word_developing)
while chances>0:
    choice=input("""Enter 'hint' for a hint
'rules' for rules
'guess' for guessing a letter
'ready' for guessing the word: \t""")
    if choice=="rules":
        print(rules,"\n")
    elif choice=="hint":
        if hints==2:
            print(hints1[word_random],"\n")
            hints-=1
        elif hints==1:
            print(hints2[word_random],"\n")
            hints-=1
        else:
            print("You have no hints left! \n")
    elif choice=="ready":
        word=input("Enter the word: \t")
        if word.lower()==word_random.lower():
            print("That was the correct word! You won!")
            break
        else:
            print("That was a wrong guess! You lost!")
            break
    elif choice=="guess":
        letter=input("Enter a letter that might be in the hidden word: \t")
        letter=letter.lower()
        if len(letter)>1:
            print("ENTER A LETTER I SAID! NOT A WORD! \n")
        else:
            occcount=word_random.lower().count(letter)
            if letter in already_guessed:
                print("You already have guessed this letter! Try another one! \n")
            else:
                if occcount==0:
                    chances-=1
                    already_guessed=already_guessed+letter
                    print(f"Wrong guess! You have {chances} chances left! \n")
                else:
                    index=-1
                    for positions in word_random.lower():
                        index+=1
                        if positions==letter:
                            index=word_random.lower().find(positions,index)
                            word_developing=word_developing[:index]+letter+word_developing[index+1:]
                if word_developing==word_random.lower():
                    print(word_random)
                    print("Correct guess! You won!")
                    break
                else:
                    print(word_developing,"\n")
    else:
        print("INVALID CHOICE ENTERED! \n")
else:
    print("You ran out of chances! The word was ",word_random,"!")
