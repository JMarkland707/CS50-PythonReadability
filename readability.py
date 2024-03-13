
# Ask the user for text input
userText = input("Text: ")
# Count the number of letters and store in variable L
LETTERS = 0
for letter in userText:
    if letter.isalpha():
        LETTERS += 1
# Count the number of words
WORDS = 1
for word in userText:
    if word == (" " or "\n"):
        WORDS += 1
# Count the number of sentences and store in variable S
SENTENCES = 0
puncList = ".", "!", "?"
for i in userText:
    if i in puncList:
        SENTENCES += 1

# Perform Coleman-Liau formula
L = (LETTERS / WORDS) * 100
S = (SENTENCES / WORDS) * 100
formulaScore = round(0.0588 * L - 0.296 * S - 15.8)

if formulaScore >= 16:
    print("Grade 16+")
elif formulaScore < 1:
    print("Before Grade 1")
else:
    print(f"Grade: {formulaScore}")
