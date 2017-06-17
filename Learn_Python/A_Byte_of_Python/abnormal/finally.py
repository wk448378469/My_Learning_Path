#coding=utf-8

import time

try:
    f = file('poem.txt')
    while True:
        line=f.readline()
        if len(line)==0:
            break
        time.sleep(2)
        print line,

finally:
    f.close()
    print 'Cleaning up...Close the file'
#在同一project中需要有“poem.txt”文件的存在，书中的例子是建立在同一目录下所以没有问题可以运行！