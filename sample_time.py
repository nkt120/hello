import datetime

dt1 = datetime.datetime(2020,1,1,9,0,0)
dt2 = datetime.datetime(2020,1,1,9,30,0)
bet_time = dt2 - dt1
print(bet_time.total_seconds()/60)
dt1 += datetime.timedelta(minutes = 30)
print(dt1.hour,dt1.minute)
print(dt1.time())