#MadLib.py
#Name:
#Date:
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
  name1 = input("What is your friend's name? ")
  noun1 = input("Enter a noun/object: ")
  verb1 = input("Enter a present tense, non-'ing' verb: ")
  noun2 = input("Enter an object you can hold: ")
  verb2 = input("Enter a past tense verb you can do to someone else: ")
  verb3 = input("Enter a verb that you do with someone else: ")
  #Print the story with the user supplied words.
  print(" ")
  print("Story Time! :) ")
  print(" ")
  print("I have a " + noun1 + " with my friend " + name1)
  print(name1 + " and I love to " + verb1 + " all around town!")
  print("Oh no! " + name1 + " found a " + noun2 + " that is not supposed to be there!")
  print(name1 + " " + verb2 + " the " + noun2 + " at me, I ran away!")
  print("That is why I do not " + verb3 + " with " + name1 + " anymore...")
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
