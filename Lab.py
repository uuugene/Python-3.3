"""def three(num):
    if num % 2 == 1 or num % 3 == 0:
        print("Yes!")
    else:
        print("No!")


ent_num = input("Enter an integer: ")
eval_ent_num = eval(ent_num)
three(eval_ent_num)"""

def greetings1(name,msg):
    print('Hello' + name + " " + msg)

greetings1("Mr. Atibila" , "goodmorning")

def greetings2(name,msg="What dey happen"):
    print("hello " + name + " " + msg)


greetings2("Abu", "Dasba")
greetings2("Abu")
#greetings2(msg='Maakye','Abu')