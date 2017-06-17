from datetime import datetime
now = datetime.now()  #获取当前世界
print (now)
print (type(now))

dt = datetime(2015,5,19,12,10)  #用指定日期时间创建datetime
print (dt)


#时间戳timestamp   1970-1-1 00:00:00 utc+0:00

#datetime和timestamp的转换
dt = datetime(2015,5,19,12,20)
print (dt.timestamp())


dt = 1432009200.0
print (datetime.fromtimestamp(dt))  #本地时间
print (datetime.utcfromtimestamp(dt))       #utc时间


#str转datetime
cday = datetime.strptime('2015-6-1 18:11:11','%Y-%m-%d %H:%M:%S')
print (cday)

#datetime转str
now = datetime.now()
print (now.strftime('%a,%b %d %H:%M'))


#datetime加减
from datetime import datetime,timedelta
now = datetime.now()
print (now)
print (now+timedelta(hours=10))
print (now-timedelta(days=1))
print (now+timedelta(days=2,hours=12))


#本地实际转换为UTC时间
from datetime import datetime,timedelta,timezone
tz_utc_8 = timezone(timedelta(hours=8)) #创建时间UTC+8:00
now = datetime.now()
dt = now.replace(tzinfo=tz_utc_8)        #强制设置为UTC+8:00
print (dt)

#时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)        #拿到UTC时间，并强制设置时区为utc+0:00
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))     #astimezone（）将转换时区为北京时间
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))      #转换为东京时间
print(tokyo_dt)
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))      #将bj_dt转换时区为东京时间
print(tokyo_dt2)



import re
from datetime import datetime,timezone,timedelta

def to_timestamp(dt_str,tz_str):
    dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    tz = re.match(r'^UTC([+|-])(0?[0-9]|1[0-2])\:00$',tz_str)
    s = int (tz.group(1)+tz.group(2))
    ts_7 = dt+timedelta(hours=s)
    ts = dt.replace(tzinfo=ts_7)
    return ts.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30','UTC+7:00')
print (t1)
