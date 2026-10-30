from itertools import product

#
# L=["Stefan", 38, "lecturer"]
# stefan={"name":"Stefan","age":38, "job":"lecturer"}
# print(stefan["age"])
#
# if "hobby" in stefan.keys(): #if we use in we are checking the keys automatically
#     print(stefan["hobby"])
# else:
#     print("Stefan does not have any hobbies. ")
#
# print("lecturer" in stefan.values())
#
# print("Stefans car:", stefan.get("car", "haha take the bus")) #here if car is not defined it will return the other value
#
# products={"milk":2.0, "bread":1.5, "honey":0.7}
# shipment={"eggs":15, "bread":5}
# products.update(shipment)
# print (products)
#
#
# # mylist=[1, 2, 3 ,4, 5, 6, 7]
# # for element in mylist:
# #     print(element)
#
# pets={"Stefan":"cat", "Tom":"dog", "Max":"bird"}
# for name in pets: #for value in list means were iterating through the keys
#     print(name, "has a ", pets[name])
#
# #iterating through values
#
# # 1. use .values()
# for pet in pets.values():
#     print(pet)
#
# # 2. iterate keys, but access values
# for owner in pets: #can be used for lists as well, will be confusing
#     print(pets[owner])
#
# # 3. use .items()
# for owner, pet in pets.items(): #.items() is exclusive for dictionaries easier to understand
#     print(owner, "has a", pet)
#
# #line 14
# updated_products={}
# for prod, quantity in products.items():
#     updated_products[prod]=quantity+10
# print(updated_products)
# updated_products2={prod:quantity+10 for prod, quantity in products.items()} #what should be the key:what should be the value
# print(updated_products2)
#
# has_many_products={prod:(quantity>2) for prod, quantity in products.items()}
# print(products)
# print(has_many_products)
#
# teachers = {
#     "Stefan":"Programming",
#     "Deepak":"Programming",
#     "Lisa":"Algorithms",
#     "Tom":"Databases",
#     "Frank":"Operating systems"
# }
#
# all_classes=(teachers.values())
# print(all_classes)
# no_duplicates= list(set(all_classes))
# print(no_duplicates)
#
# #line 67
#
# updated_products={}
# for prod, quantity in products.items():
#     updated_products[prod]=quantity+10
#
# for pair in products.items():
#     updated_products[pair[0]]=pair[1]+10
#
# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")
#
# x = zip(a, b)
# print(tuple(x))

# def greeting():
#     print("Hello IMC!")
# greeting()

# prices={"milk":2, "carrot":1, "jogurt":1.5}
#
# def increase(percentage):
#     for prod, price in prices.items():
#         prices[prod]=price*((1+percentage/100))
#
# def decrease(percentage):
#     for prod, price in prices.items():
#         prices[prod]=price*(1-(percentage/100))
#
# def program():
#     while True:
#         read = input("Increase or decrease? (type inc or dec)")
#         if read == "inc":
#             percentage = float(input("Enter percentage: "))
#             #increase the prices
#             increase(percentage)
#             print(prices)
#         elif read == "dec":
#             percentage = float(input("Enter percentage: "))
#             #decrease
#             decrease(percentage)
#             print(prices)
#         else:
#             break
# program()

def power(number, exponent=2):#here we can use = to assign base case for unspecified inputs
    return number**exponent
print(power(2, 3))
print(power(4))

def statistics(numbers):
    minimum=min(numbers)
    maximum=max(numbers)
    total=sum(numbers)
    return minimum, maximum, total
result = statistics([1, 2, 3, 4, 5])
print(result[2])
smallest, largest, total = statistics([1, 2, 3, 4, 5])
print((smallest, largest, "and", total))