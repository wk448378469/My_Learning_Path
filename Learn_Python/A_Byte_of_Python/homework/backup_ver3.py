#coding=utf-8

import os
import time

source=['C:\\Data']
target_dir= 'D:\\text\\'
today=target_dir+time.strftime('%Y%m%d')
now=time.strftime('%H%M%S')

comment=raw_input('Enter a comment:')
if len(comment)==0:
    target=today+os.sep+now+'.7z'
else:
    target=today+os.sep+now+'_'+comment.replace('','_')+'.7z'

if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory',today

zip_command = "7z a %s %s" %(target,' '.join(source))

if os.system(zip_command)==0:
    print 'Successful backup to',target
else:
    print 'Back up FAILED'

