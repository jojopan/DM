# coding=utf-8


name = input("输入你的名字：")
age = input("输入你的年龄：")
height = input("输入你的身高：")
question = input("你是不是特别黑：")

# print(name)
# print(age)
# print(height)
# print(question)


if question == "0" or question == "1":
    print("wobuxin")

msg = '''
-----------Personal Info----------
Name   : %s
Age    : %d
Height : %s
Answer : %s
----------End---------------------
''' % (name,age,height,question)


# print(msg)