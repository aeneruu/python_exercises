opening_brackets=["{", "[", "("]
closing_brackets=["}", "]", ")"]
curly_brackets=["{", "}"]
box_brackets=["[", "]"]
round_brackets=["(", ")"]
brackets_stack=[]

expression=input("Please enter your expression: ")

for i in range(int(len(expression))):
