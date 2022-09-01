import datetime
import time
from calendar import Calendar

def last_month():
    first_day = datetime.date(datetime.date.today().year,datetime.date.today().month-1,1)
    last_day = datetime.date(datetime.date.today().year,datetime.date.today().month,1)-datetime.timedelta(1)


    first_day_stamp=int(time.mktime(time.strptime(str(first_day),'%Y-%m-%d')))*1000
    #end_day_stamp = int(time.mktime(time.strptime(str(last_day), '%Y-%m-%d')))*1000+86399000
    end_day_stamp = (int(time.mktime(time.strptime(str(last_day), '%Y-%m-%d'))) +86400-1)*1000

    return(first_day_stamp,end_day_stamp)

def stamp(start,end):
    start_day_stamp = int(time.mktime(time.strptime(str(start),'%Y-%m-%d')))*1000
    end_day_stamp = int(time.mktime(time.strptime(str(end), '%Y-%m-%d')))*1000+86399999
    print(start_day_stamp,end_day_stamp)
    return start_day_stamp,end_day_stamp


if __name__=="__main__":
    #last_month()
    stamp('2022-08-10','2022-08-16')



