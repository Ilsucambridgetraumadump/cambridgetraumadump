#Task # 38 : Input characters and stop when a full stop is entered. Print the number of vowels and 
#consonants entered. Do not accept any non-characters and give an error if entered. Accept both lower 
#case and upper case alphabets.

ch = ""
vowels = 0
consonants = 0

while ch != ".":
    ch = input("input a letter ")
    while len(ch) > 1 or not ch.isalpha():            #could do ch.isalpha = 1, ch.isaplha = true, not ch.isalpha = 0...... etc
        print("please enter a single letter ")
        ch = input("input a letter ")
    if ch in "AEIOUaeiou":                          #could also do if ch.lower in "aeiou" or if ch.upper in "AEIOU"
        vowels = vowels + 1
    else:
        consonants = consonants + 1

print("vowels = ", vowels, "\nconsonants = ", consonants)
