
'''
HW1
'''

######### (100 points) ###########

'''write a function that gets a sentence (as a str) and outputs the length of the last word and the count of the characters in the sentence. 
   1) 
   
   e.g.: input_sentence = 'Hello World!' --> output = [ 5 , 12 ]       
   e.g.: input_sentence = 'This is a sentence.' --> output = [ 8 , 19]
   

'''
def find_length(x):
    words = x.split()

    if not len(words):
        return 'sentence cannot be empty!'
    return [len([i for i in words[-1] if ord('A') <= ord(i) <= ord('Z') or ord('a') <= ord(i) <= ord('z')]),
            len(x)]


print(find_length('How Are You!?'))
print(find_length('Iam doing good!!'))

'''
    2)  write a function that gets two lists of numbers and merges them and outputs the sorted merged list.
   
   e.g.: input_list1 = [0,1,2,8,-1, 9] , input_list2 = [-11,9]--> output = [-11, -1, 0, 1, 2, 8, 9, 9]
   
'''
 def sorted_merged_list(l1,l2):
    return ((sorted(l1 + l2)))

l1 = [9,4,2,-1,-2,-4]
l2 = [8,11,-8]
print(sorted_merged_list(l1,l2))

'''
    3)  write a function that get a list of numbers and outputs the second largest number in it.
   
   e.g.: input_list = [0,1,2,8,-1] --> output = 2
   e.g.: input_list = [-11, 1.2, 9.9,9] --> output = 9
'''
def second_largest_number(list1):
    list1.sort()
    return list1[len(list1)-2]

input_list1 = [81,76,108,95,2]
print(second_largest_number(input_list1))


'''
    4)  write a function that get a string as an input and outputs the reverse of that (only letters!)
   
   e.g.: input_str = 'hel-lo,wo.rld' --> output = 'dlr-ow,ol.leh'
   e.g.: input_str = '12311!hm' --> output = '12311!mh'
'''
def reverseString(text):
    index = -1

    for i in range(len(text) - 1, int(len(text) / 2), -1):

        if text[i].isalpha():
            temp = text[i]
            while True:
                index += 1
                if text[index].isalpha():
                    text[i] = text[index]
                    text[index] = temp
                    break
    return text


string = "123vouty*@as"
print("Input string: ", string)
string = reverseString(list(string))
print("Output string: ", "".join(string))

'''
    5)  write a function that gets a sentence (as a str) and outputs the reverse of that.
   
   e.g.: input_sentence = 'Hello World' --> output = 'World Hello'
   e.g.: input_sentence = 'this is a sentence' --> output = 'sentence a is this'
'''
def reversed_sentence(Sentence):
    Sentence = Sentence.split()
    Sentence.reverse()
    return ' '.join(Sentence)


print(reversed_sentence('Too much noise'))
print(reversed_sentence('Monday is a weekday'))

'''
    6)  write a function that gets two numbers as strings and outputs the sum of them. 
   
   e.g.: str1 = '96' , sr2 = '21'--> output = 117
   e.g.: str1 = '28' , sr2 = '2'--> output = 30
'''
def sum_method(first, second):
    return int(first) + int(second)
str1 = '100'
str2 = '200'
print(sum_method(str1, str2))
str1 = '300'
str2 = '400'
print(sum_method(str1, str2))

'''
    7)  write a function that gets two binary numbers from the user and outputs the sum of them in binary. 
   
   e.g.: input1 = 101 , input2 = 10 --> output = 111
   e.g.: input1 = 11 , input2 = 1 --> output = 100
'''
def two_binary_numbers(input1, input2):
    try:
        result = int(input1, 2) + int(input2, 2)
        return bin(result)[2:]
    except Exception as e:
        return e

input1 = input('Enter the number in binary format A: ')
input2 = input('Enter the number in binary format B: ')

print(two_binary_numbers(input1, input2))

'''
    8)  write a function:
    
        5-1) thats gets a list of numbers and counts the occurrences of all items in it. 
              e.g.: list1 = [9,9,1,0,1,9] --> output = [(9,3) , (1,2), (0,1)]
              
        5-2) that gets two lists and outputs their common elements. 
             e.g.: list1 = [66,23,1,0,1,9] , list2 = [5,55,1,12] --> output = [1] 
'''
from collections import Counter

def counts_the_occurences(list1):
    return list(Counter(list1).items())

print(counts_the_occurences([5, 5, 7, 8, 8, 10, 11]))

a=[2,3,4,5]
b=[3,5,7,9]
def common(a,b):
    c = [value for value in a if value in b]
    return c
d=common(a,b)
print(d) 

'''      

    9)  write a function that gets a string from the user and returns the most frequent character in it. 
   
   e.g.: str1 = 'hello world'--> output = 'l'
   e.g.: str1 = 'cs_comp478'--> output = 'c'
'''
# YOUR CODE GOES HERE

def most_frequent_character(str1):
  max_count = 0
  max_char = ''
  for char in str1:
      count = str1.count(char)
      if count > max_count:
          max_count = count
          max_char = char
  print(str(max_char))
most_frequent_character('abcdefabcc')

'''
    10) write a function that gets a list of numbers and returns the compnents of the list that are perfect square numbers. 
   
   e.g.: input1 = [1, 5, 8, 9] --> output = [1,9]
   e.g.: input1 = [3, 7, 5, 55 ]--> output = []

'''

# YOUR CODE GOES HERE

from math import sqrt

def perfect_square(list1):
    return [i for i in list1 if int(sqrt(i))**2 == i]

print(perfect_square([4, 36, 77, 91]))
print(perfect_square([2, 8, 11, 12]))

'''


    

