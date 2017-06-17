classmates=['ahaha','kai','xiaoming']
print (len(classmates))

print (classmates[0])
print (classmates[1])
print (classmates[2])

print (classmates[-2])
print (classmates[-3])

classmates.append('lalala')

print (classmates[-1])

classmates.insert(0,'jack')
print (classmates[:])

classmates.pop()
print (classmates[:])

classmates.pop(0)
print (classmates[:])

classmates[0]='yuhuanhuan'
print (classmates[:])


list2=['add1','add2']
classmates.append(list2)
print (classmates[:])

print (len(classmates))
print (classmates[-1][0])

classmates.pop(0)
classmates.pop(1)
classmates.pop(1)
classmates.pop(0)

print (len(classmates))



classsdu=('bob1','bob2','bob3')
i=0
while i<3:
    print(classsdu[i])
    i=i+1
    if i==3:
        break
    
nimei=(2)
print (nimei)           #只有一个元素会被认为是一个变量赋值了2
nimei=5
print (nimei)           #而不是一个元组

nimeia=(2,)
print (nimeia[0])       #这样才是一个数组

t=('asd','dsa','wds','asx',['a','b'])
print (len(t))
print (t[0:5])

t[4][0]='x'
t[4][1]='y'
print (t[0:5])

L=[

    ['apple','Google','Microsoft'],
    ['Java','Python','PHP'],
    ['wangkai','alibaba','xixi']
]
print (L[0][0])
print (L[1][1])
print (L[2][2])

i=0
j=0

while i<3 and j<3:
    if L[i][j] == ['Java']:
        print (L[i][j])
    else:
        i=i+1
        j=j+1
