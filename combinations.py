from itertools import combinations
word,n = map(str,input("Enter the word and the range :").split())
list1 = sorted(list(combinations(word,int(n))))
print(list1)