#Task 1: The function returns s string of name chosen by user, greeting and punctuation. Punctuation and greeting have a base value: "Hello","!", if theyre not specified they will return this value.
# def greet(name, greeting = "Hello", punctuation = "!"):
#     return name+","+greeting+punctuation #here we used "+" to connect the string variables, we couldve also used f"{name},{greeting}{punctuation}", which has the same result
#
# print(greet("Ada"))
# print(greet("Bob", "good morning"))
# print(greet("Bob", punctuation="."))


#Task 2: Sum to n, user inputs n>=0 and the program returns the sum of all numbers from 1 to n
# def sum (n):
#     sum = 0
#     while n > 0:
#         sum = sum + n
#         n = n-1
#     return sum
# print(sum(0))

#Task 3:
# def divide(a, b):
#     return a//b, a%b
#
# divide(17,5)


#Task 4:Counting even numbers:
# def count_even(numbers):
#     count=0
#     for n in numbers:
#         if n%2==0:
#             count+=1
#     print (count)
#     return
# count_even([])

#Task 5:Enter score and the program returns your grade. Do not use elif.
# score = int(input())
# def grade(score): #here we do NOT have to use AND, because python reads this line by line, and if one condition is fulfilled, it executes return, which returns a grade and exits the value
#     if score >= 90:
#         return 1
#     if score >=80:
#         return 2
#     if score >=70:
#         return 3
#     if score >=60:
#         return 4
#     else:
#         return 5
# print(grade(score))
#
# def grade(score): #here we HAVE to use intervals to specify, because the function grade(score) will go through every single line before it ends
#     if score >= 90:
#         print(1)
#     if score >=80 and score <90:
#         print(2)
#     if score >=70 and score <80:
#         print(3)
#     if score >=60 and score <70:
#         print(4)
#     else:
#         print(5)
#
# def grade(score):
#    grading={
#         90:1,
#         80:2,
#         70:3,
#         60:4,
#         0:5
#      }
#    for key in grading: #we are going to be iterating throught the keys (lowest score needed for each grade) of the dictionary and comparing them with our score
#          if score >= key:
#             print( grading[key]) #we only use print to check whether it works, in the test you actually only need ot use return grading[key]
#             return
# grade(0)


#Task 9:
# def distance(p1, p2):
#     x=p2[0]-p1[0]
#     y=p2[1]-p1[1]
#     distance= (x**2+y**2)**0.5
#     print(str(distance))
#     return
#
# distance((1,2),(4,6))

#Task 6:
# def count_vowels(text):
#     vowels=["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
#     count=0
#     for ch in text:
#         if ch in vowels:
#             count+=1
#     print(count)
#     return
# count_vowels("genz amish")

#other solution
# def distance(p1, p2):
#     x1, y1 = p1
#     x2, y2 = p2
#     print(((x2-x1)**2 + (y2-y1)**2)**0.5)
#     return
# distance((1,2),(4,6))

#Task 7

#Task 10: Square, sum of square
# def square(x):
#     return x**2
#
# def sum_of_squares(numbers):
#     total = 0
#     for i in numbers:
#         total = square(i) + total
#     print(total)
#     return
# sum_of_squares([1, 2, 3])

#Task 15: domain of and emai adress
# def email_domain(email):
#     i=0
#     for ch in email:
#         i=i+1
#         if ch == "@":
#             return email[i:]
#         return ""
# email_domain("fenikova.kati@gmail.com")