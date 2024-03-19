
#Input
digitWords = input("Please enter a digit and two words:")

#Level 3
digit = int(digitWords[0])
words = str(digitWords[2:])
noSpaces = words.replace(" ", "")

#Level 4
wordTimes = digit*2
space0 = words.find(" ")
lastLetter0 = words[space0 - 1]
lastLetter1 = words[-1]

#Level 4+
word1 = words[:space0]
word1Len = len(word1)
word2 = words[space0 + 1:]
word2Len = len(word2)
fullWordLen = word1Len + word2Len
letter1 = word1[0]
letter2 = word2[-1]

#Outputs
print(digit*noSpaces)
print(wordTimes*(lastLetter0 + lastLetter1))
print(fullWordLen*(letter1 + letter2))