Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import time
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'time']
>>> dir(time)
['_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'altzone', 'asctime', 'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic', 'monotonic_ns', 'perf_counter', 'perf_counter_ns', 'process_time', 'process_time_ns', 'sleep', 'strftime', 'strptime', 'struct_time', 'thread_time', 'thread_time_ns', 'time', 'time_ns', 'timezone', 'tzname']
>>> time.time()
1617696754.9921656
>>> time.sleep(10)
>>> time.gmtime()
time.struct_time(tm_year=2021, tm_mon=4, tm_mday=6, tm_hour=8, tm_min=13, tm_sec=37, tm_wday=1, tm_yday=96, tm_isdst=0)
>>> time.localtime()
time.struct_time(tm_year=2021, tm_mon=4, tm_mday=6, tm_hour=17, tm_min=13, tm_sec=43, tm_wday=1, tm_yday=96, tm_isdst=0)
>>> from datetime import *
>>> dir()
['MAXYEAR', 'MINYEAR', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
>>> d1 = date(2021,5,1)
>>> d2 = date(2021,6,20)
>>> d1
datetime.date(2021, 5, 1)
>>> d2
datetime.date(2021, 6, 20)
>>> d3 = date.today()
>>> d3
datetime.date(2021, 4, 6)
>>> d = date.today()
>>> te = timedelta(days=100)
>>> d + te
datetime.date(2021, 7, 15)
>>> 