#3.1
# firstList=[]
# firstList.append("genz amish kid names skibidiah")
# secondList=["genz", "amish", "kid", "named", "skibidiah"]
# thirdList=3*["amish"]
# a = [1,2,3]
# b = 3*["xyz"]
# c=a+b
# print(c)

#3.2
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = a+b
# sortedList=sorted(c)
# print(c)
# print(sortedList)
# for i in sortedList:
#     while sortedList.count(i)>1:
#         sortedList.remove(i)
# print(sortedList)

#3.3
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list3=[]
#
# for i in range(len(list1)):
#     element=list1[i]+list2[i]
#     list3.append(element)
# print (list3)

#3.4
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# list2 = ["h", "i", "j"]
# print(list1[2][1][2][0])
# list1[2][1][2].append(list2)
# print(list1)

#3.5
# number=int(input("Enter a number: "))
# while number>1:
#     factorial=number*number-1
# print(factorial)

# 2.10
# number=int(input("Insert a number between 10 and 99"))
# while number<=10 and number>=99:
#     number = int(input("Please insert a number between 10 and 99"))
#
# for i in range(0,number):
#     if i%3>0 or i%7>0:
#         print(i)

#2.11
# string=""
# start=int(input("enter start: "))
# end=int(input("enter end: "))
# for i in range(start,end+1):
#     if i>end-1:
#         print(f"{i}*{i}", end=" ")
#     else:
#         print(f"{i}*{i}", end=" + ")
# s=0
# for i in range(start,end+1):
#     s=s+i*i
# print("=", s)

#exercise
# for i in range(1,10):
#     print("\n", end="")
#     for j in range(1,10):
#         print(f"{i}x{j}={i*j}", end="; ")

#2.7 abbreviations creator
# phrase = input("Input a phrase: ")
# words=phrase.split(" ")
# print(words)
# for i in words:
#     letter=i[0].upper()
#     print(letter, end="")

#2.8 string middle characters
# phrase=input("Input a string: ")
# if len(phrase)>7 :
#     if len(phrase)%2 > 0:
#         md_point=len(phrase)//2
#         start=md_point-1
#         end=md_point+2
#         md_characters=phrase[start:end]
#         print(f"The middle characters are {md_characters}.")
#     else:
#         print("ERROR: The string is even.")
# else:
#     print("ERROR: The string is shorter than 7.")

# 2.9 balanced words
# word = input("Enter word: ")
# first=""
# second=""
# md_point = len(word) // 2
# sum_left=0
# sum_right=0
#
# if len(word)%2>0:
#     first=word[:md_point]
#     second=word[md_point+1:]
#
# else:
#     first=word[:md_point]
#     second=word[md_point:]
#
# for i in first:
#     sum_left=sum_left+ord(i)
#
# for j in second:
#     sum_right = sum_right + ord(j)
#
# if sum_left == sum_right:
#     print(f"{word} is balanced  ({word} = {first}|{second} = {sum_left}|{sum_right} = True) ")
# else:
#     print(f"{word} is unbalanced  ({word} = {first}|{second} = {sum_left}|{sum_right} = False) ")

#2.10 looping around
# number=int(input("input a number from 10 to 99: "))
# while number>99 or number<10:
#     number = int(input("please input a number from 10 to 99: "))
# for i in range(number):
#     if i%7==0:
#         continue
#     if i%3==0:
#         continue
#
#     print(i, end=";")

#2.12 loops and strings
# word=input("Enter word: ")
# used_letters=""
# isogram=False
# used_letters = ""
#
# for i in word:
#
#     if i in used_letters or i.upper() in used_letters or i.lower() in used_letters:
#         isogram=False
#         break
#
#     else:
#         isogram=True
#
#     used_letters=used_letters+i
#
# if isogram==True:
#     print(f"The word {word} is an isogram.")
#
# else:
#     print(f"The word {word} is not an isogram.")

# 2.13 kaprekar numbers
# number=int(input("enter number: "))
# square=number**2
# square_str=str(square)
# if len(square_str)%2==0:
#     midpoint=len(square_str)//2
#     left=square_str[:midpoint]
#     right=square_str[midpoint:]
#     sum=int(left)+int(right)
#
#     if sum==number:
#         print(f"The number {number} is a Kaprekar number: {number}^2 = {square} and {left} + {right} = {sum}.")
#     else:
#         print(f"The number {number} is not a Kaprekar number.")
# else:
#     print("number invalid")

#2.14 the steinhaus cyclus
import time
sum=0
seq=""
count1=0
count145=0

number=input('enter a four digit number: ')
while len(str(number))>4 or len(str(number))<4:
    number=input('invalid number. please enter a four digit number: ')

while count1<2 and count145<2:

    for i in number:
        sum=sum+int(i)**2
    if sum == 1:
        count1 += 1
    elif sum == 145:
        count145 += 1

    seq = seq + f"{str(sum)}; "
    number = str(sum)
    sum=0

print(seq)



