def main():
      alph = input("Enter any alphabet: ")
      alph = alph.lower()
      vowel = "aeiou"
      consonant = "bcdfghjklmnpqrstvwxyz"
      if(alph in vowel): 
       print("It is a vowel")
      elif(alph in consonant):
        print("It is a consonant")  
      else:
         print("Please enter a valid input")   



if (__name__ == "__main__"):
    main()    