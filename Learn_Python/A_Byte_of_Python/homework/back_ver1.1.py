import os
import time
source = ['C:\\Data']
target_dir = 'D:\\text\\'
target = target_dir+time.strftime('%Y%m%d%H%M%S')+'.7z'
zip_command = "7z a %s %s" %(target,' '.join(source))
if os.system(zip_command)==0:
    print 'Successful backup to',target
else:
    print 'Backup failed'