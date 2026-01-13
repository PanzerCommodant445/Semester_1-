#-------------Methods-------------
# This method should return the largest of 3 integers
def largestOfThree(x, y, z):
    largest = x
    if y > largest:
        largest = y
    if z > largest:
        largest = z
    return largest

# This method should combine all the words in the list into a sentence with spaces between
def formSentence(wordList):
    sentence = ""
    for i in range(len(wordList)):
        sentence += wordList[i]
        if i != len(wordList) - 1:   # add a space unless it's the last word
            sentence += " "
    return sentence

# This method should combine all the words in the list in reverse into a sentence with spaces between
def reverseSentence(wordList):
    sentence = ""
    for i in range(len(wordList) - 1, -1, -1):  # loop backwards manually
        sentence += wordList[i]
        if i != 0:   # add space unless it's the first element
            sentence += " "
    return sentence

#--------------Code--------------
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter another number: "))

ans = largestOfThree(a, b, c)
print("The largest of the three numbers is " + str(ans))
print()

words = ["This", "will", "become", "the", "coolest", "sentence", "yahoo"]
sentence = formSentence(words)
print(sentence)

print()
print("The same sentence backwards!")
sentence = reverseSentence(words)
print(sentence)