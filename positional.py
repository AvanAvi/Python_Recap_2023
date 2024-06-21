def result(maths, english, science, history,french):
    total = maths + english + science + history + french
    average = total / 5
    percentage = (total*100)/500
    print (total)
    print(average)
    print (percentage)

result(english=100,maths=64,history=67,french=84,science=99)




def add2(num1,num2=7):
    print(num1+num2)

add2(12)    