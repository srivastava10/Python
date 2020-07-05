s = ''
word = str(input())
a = word[0].upper()
word = list(word)
word[0]=a
finalWord = s.join(word)
print(finalWord)