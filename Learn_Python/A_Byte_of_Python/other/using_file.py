#coding=utf-8

poem='''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
    '''

f=file('poem.txt','w')           #open for 'w'riting            用写的方式打开文件
f.write(poem)                       #write text to file
f.close()                            #close the file

f=file('poem.txt')                 #if no mode is specified,'r'ead mode is assumed by default:如果没有指定模式，'r'ead模式假定默认
while True:
    line=f.readline()                 #用readline()来读取文件中的每一行，而且这样读的话会返回包含行末尾的换行符！
    if len(line)==0:                  #zero lenth in dication EOF（文件结束）
        break
    print line                 #notice commat to avoid autom atic new line added by python。
                                #在line后面加上","是为了消除自动换行
f.close()