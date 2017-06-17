

number=23
guess=int(raw_input('Enter an integer:'))

if guess==number:
    print 'Congratulation,you guessed it'#New block startshere
    print "(but you do not win any prizes!)"# NeW block endeshere
elif guess<number:
    print 'No,it is a little higher than that'#Anythor block
    #You can do whatever you want in a block...
else:
    print 'No,it is a little lower than that'
    #You must have guess>number to reach here

print 'Done'
#This last state ent is always executed ,after the if statem ent is executed