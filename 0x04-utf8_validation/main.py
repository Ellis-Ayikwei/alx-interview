from datetime import datetime, timedelta
from pytz import timezone
import pytz

utc = pytz.utc
print(utc.zone)
eastern = timezone('US/Eastern')
print(eastern.zone)
amsterdam = timezone('Europe/Amsterdam')
print(amsterdam.zone)
fmt = '%Y-%m-%d %H:%M:%S %Z%z'

lod_dt = eastern.localize(datetime(2002, 10, 27, 6,0,0))
print(lod_dt.strftime(fmt))

utc_dt = datetime(2002, 10, 27, 6,0,0, tzinfo=utc)
loc_dt = utc_dt.astimezone(eastern)
loc_dt.strftime(fmt)
print(loc_dt.strftime(fmt))

before = loc_dt - timedelta(minutes=10)
print(before.strftime(fmt))

print(eastern.normalize(before).strftime(fmt))

after = loc_dt + timedelta(minutes=10)

utc_dt = datetime.fromtimestamp(1143408899, tz=utc)
print(utc_dt.strftime(fmt))

now = datetime.now()
timedt = now - timedelta(days=10)
print(timedt.strftime(fmt))