
age = 20
if age>=18:
    print('your age is',age)
    print('adult')

age = 3
if age>=18:
    print ('your age is',age)
    print ('adult')
else:
    print ('your age is',age)
    print ('teenager')

age = 3
if age>=18:
    print ('your age is',age)
    print ('adult')

elif age>=6:
    print ('your age is',age)
    print ('teenager')

else:
    print ('you are kid ,go back home play something')


x=1
if x:
    print('x is not zero')

birth = int(input('please enter your birth:'))
if birth<2000:
    print('蛋蛋前')
else:
    print('蛋蛋后')

#BMI测试~
m = float(input('please enter your tall(eg:1.75):'))
kg = float(input('please enter your fit(eg:76.5):'))

BMI = kg/(m*m)

if BMI>32:
    print ('你TM非常胖了')
elif BMI<=32 and BMI>28:
    print ('你有点胖伙计')
elif BMI<=28 and BMI>25:
    print ('亲你的体重有点过重哦')
elif BMI<=25 and BMI>18.5:
    print ('你TM是正常身材')
else:
    print ('你妈太对不起你了~')


if salary>=10:
    print ('我擦你个变态')
elif salary>=5:
    print ('你他妈的就是变态别想了')
else:
    print ('咋地不服啊！')
