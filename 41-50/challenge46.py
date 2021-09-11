"""
Write a Python program that prints a descriptive message 
indicating if each character in a string is a vowel or a consonant. 
For example: "<char> is a <consonant | vowel>"

If the character is a special character, number, or symbol, print "<char> is not a letter".

If the string is empty, print "Empty String".

"""
my_word = "Shravan@4656!_ 123-1"
word = my_word.casefold()

if not word:
    print("its empty")
else:
    for i in word:
        if i.isalpha():
            vowels = ["a", "e", "i", "o", "u"]
            if i in vowels:
                print(f"{i} is vowel")
            else:
                print(f"{i} is consonant")
        elif i.isdigit():
            print(f"{i} is a number")
        elif i == " ":
            print(f"{i} is a space")
        else:
            print(f"{i} is not a letter")
