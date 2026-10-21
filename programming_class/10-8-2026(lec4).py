# l1=[12, 34, 56, 34, 2, 3, 45 ,8 ,6]
# l2=["a", "b", "c"]
# l3 = [l1, l2]
# lz=l1
# lz[0]="Apple"
# print(l1)
#
# l4=[1, 2, 3]
# l5=[1, 2, 3]
# print(l4 is l5) #will return True or False depending on whether the value is stored in the same direction
# print(l4 == l5) #will return True or False depending on whether the value is the same
#
#
# #fruits
# fruits=["Dragonfruit", "Cantaloupe", "Banana", "Apple"]
# long_index=0
# current_index=0
#
# for fpair in enumerate(fruits):
#     if len(fpair[1]) > len(fruits[long_index]): #what
#         long_index=index
#     current_index+=1
# print(f"in index {long_index}, we have {fruits[long_index]}")
#
# fruits[1]="Mango"
# f="Mango"
#
# fruits2=list(fruits) #we have created a copy of fruits in a different direction
# # other ways:
# #fruits2 = fruits[:]
# #fruits2 = fruits.copy()
# #fruits2   = [] + fruits
# fruits2[2]="Guava"
#
# print(fruits)
# print(fruits2)

#x=sorted(list1) and list1.sort, similar y=reversed(list1), list1.reverse()

# table= [
#     ["Joe", 26],
#     ["Kim", 19],
#     ["Sue", 25]
# ]
# table[2][0]="Max"
#
# print(table)
#
#
# list1=[3, 4, 5, 6, 7, 8]
# result = [num*num for num in list1]
# print(result)
#
# #for num in list1:
# #   result.append(num*num)
# #print(result)
#
#
# emails=["skibidy.genz@kid.named", "skibidiah.genz@amish.kid", "kid.named@skibidiah.genz"]
# result=[email[0:email.index("@")] for email in emails]
# print(result)

#task 3.5 factorial digit su
# num=int(input("Enter your number to be factorized and added: "))
# factorial=1
# sum=0
#
# for i in range(1,num):
#     factorial=factorial*num
#     num=num-1
# print(factorial)
#
# factorial_str=str(factorial)
# for j in factorial_str:
#     sum=sum+int(j)
# print(sum)

#task 3.6
# game_input_validity=False
# while game_input_validity==False:
#     game = input("Enter finished game in lowercase, substitute empty spaces with \"_\": ")
#     if len(game) == 9:
#         game_input_validity = True
#
# o_win="ooo"
# x_win="xxx"
#
# if game[0:3] == x_win or game[3:6] == x_win or game[6:]==x_win:
#     print("x won game horizontally.")
#
# elif game[0:3] == o_win or game[3:6] == o_win or game[6:]==o_win:
#     print("o won game horizontally.")
#
# elif game[::3]==x_win or game[1::3]==x_win or game[2::3]==x_win:
#     print("x won game vertically.")
#
# elif game[::3]==o_win or game[1::3]==o_win or game[2::3]==o_win:
#     print("o won game vertically.")
#
# elif game[0::4]==x_win or game[2:7:2]==x_win:
#     print("x won game diagonally.")
#
# elif game[0::4]==o_win or game[2:7:2]==o_win:
#     print("o won game diagonally.")
#
# else:
#     print("Game ended in draw.")

squares=[]
lines=[]
print(type(lines))
game_input_validity=False
while game_input_validity==False:
    game = input("Enter finished game in lowercase: ")
    if len(game) == 81:
        game_input_validity = True

for n in range(9):
    line=game[n*9:9+n*9]
    print(line)
    lines.append(line)
print(lines)

for n in range(9):
    square=game[0:9:]
    print(line)
    lines.append(line)
print(lines)






# 859612437723854169164379528986147352375268914241593786432981675617425893598736241












