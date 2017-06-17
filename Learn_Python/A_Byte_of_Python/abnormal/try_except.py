#coding=utf-8

import sys

try:
    s=raw_input('Enter something->')
except EOFError:
    print '\n Why did you do an EOF on me?'
    sys.exit()

except:
    print '\n Some error/exception occurred'

print 'Done'

#把错误的语句放到try中，然后在except中处理所有的错误和异常
