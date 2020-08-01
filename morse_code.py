# Importing numpy
import numpy as np

#Declaring the dictionary for all the alphanumeric characters
dictionary = {'a':'.-',
              'b':'-...',
              'c':'-.-.',
              'd':'-..',
              'e':'.',
              'f':'..-.',
              'g':'--.',
              'h':'....',
              'i':'..',
              'j':'.---',
              'k':'-.-',
              'l':'.-..',
              'm':'--',
              'n':'-.',
              'o':'---',
              'p':'.--.',
              'q':'--.-',
              'r':'.-.',
              's':'...',
              't':'-',
              'u':'..-',
              'v':'...-',
              'w':'.--',
              'x':'-..-',
              'y':'-.--',
              'z':'--..',
              '1':'.----',
              '2':'..---',
              '3':'...--',
              '4':'....-',
              '5':'.....',
              '6':'-....',
              '7':'--...',
              '8':'---..',
              '9':'----.',
              '0':'-----',
              ' ':' '}

#An example String to print in morse code
string = 'hello all this 12392 station'

#Declaring an empty string to save the morse code
morse_str = ""

#Iterating through each element of the string and converting it to morse code

for l in string:
    morse_str+=dictionary[l]+ ' '

#Finally, Printint the morse code
print(morse_str)
    
    
