# coding=utf-8

number=23
running=True

while running:
    guess=int(raw_input('Enter integer:'))

    if guess==number:
        print 'Congratulation you guess it.'
        running=False #this causes the while loop to stop

    elif guess<number:
        print 'No,it is a little higher than that'

    else:
        print 'No,it is a little lower than that'

else:
    print 'The while loop is over.'
    #Do anything else you want to do here

print 'Done'

#记住，在python语言中是可以在while循环中加入else语句，这点和C有很大的不同哦