from datetime import datetime, timedelta

t1 = 'Sun 10 May 2015 13:54:36 -0700'
t2 = 'Sun 10 May 2015 13:54:36 -0000'

def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    t1_dt = datetime.strptime(t1, fmt)
    t2_dt = datetime.strptime(t2, fmt)
    return str(abs(int((t2_dt - t1_dt).total_seconds())))

print(time_delta(t1, t2))