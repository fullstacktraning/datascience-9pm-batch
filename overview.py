# str = "Python !!!"
# print(str)

# age = 40
# print(age)

# price=10.1
# print(price)

# is_student = True
# print(is_student)

# x= "10"
# y = int(x)
# print(y*y)

# num1 = 10
# num2 = True
# print(num1 > num2)
# print(num1 > 5 and num2 < 5)
# print(num1 * num2)

# age = 18
# if age >= 18:
#     print("Eligible to vote")

# age = 16
# if age >= 18:
#     print("Major")
# else:
#     print("Minor")

# marks = 85
# if marks >= 90:
#     print("A")
# elif marks>= 75:
#     print("B")
# else:
#     print("C")

# marks = 85
# match marks:
#     case 90:
#         print("A")
#     case 85:
#         print("B")
#     case 70:
#         print("C")
#     case _:
#         print("Fail")

# def test_func():
#     print("No Parameter - No Return Type")

# test_func()

# def test_func():
#     return "No Parameter - With Return Type"

# res = test_func()
# print(res)


# def test_func(param1):
#     print(param1)

# test_func("With Parameter - No Return Type")


# def test_func(param1):
#     return param1

# res = test_func("With Parameter - With Return Type")
# print(res)


# score = {
#     90 : "A Grade",
#     80 : "B Grade",
#     70 : "C Grade",
#     60 : "Fail"
# }
# print(score)
# print(score.get(90))
# print(score.get(40,"Invalid"))


# mathematics = {
#     "+" : lambda num1,num2:num1+num2,
#     "-" : lambda num1,num2:num1-num2,
#     "*" : lambda num1,num2:num1*num2,
#     "/" : lambda num1,num2:num1/num2
# }

# print(mathematics["+"](200,100))

# numbers = [10,20,30,40,50]
# for num in numbers:
#     print(num)

# tuple = (100,200,300)
# print(tuple)
# print(tuple[0])
# print(tuple[-1])
# for tup in tuple:
#     print(tup)


a, *b = (1,2,3,4,5)
print(a)
for num in b:
    print(num)