****
Time
****

Times and dates are not built in types in python, but they're important enough
to mention here while we discuss other types.

*NOTE: Test these on your system, as there can be differences between
unixlike and windows, and there can be differences depending on what is
considered localtime, time due to daylight savings, etc.*


::

   import time
   
   # to get "now" in seconds since the epoch
   >>> time.time()
   1314852408.951319
   # to convert "now" into a human readable time
   >>> time.ctime(time.time())
   'Wed Aug 31 21:47:01 2011'
   # to see the effect of your timezone, call ctime with a value of 1
   >>> time.ctime(1)
   'Wed Dec 31 16:00:01 1969'
   
   
   # Others
   # Are we in daylight savings? (1 for yes, 0 for no)
   >>> time.daylight
   1
   # To figure out our timezone (timezone is number of seconds west from utc)
   >>> -1 * (time.timezone / (60*60)) 
   # Pause the execution of an application for x number of seconds
   >>> time.sleep(5)
   

Dates
=====

::

   >>> import datetime
   >>> d = datetime.datetime(2010, 7, 4, 12, 15, 58)
   >>> '{0:%Y-%m-%d %H:%M:%S}'.format(d)
   '2010-07-04 12:15:58'
   
   ### Date arithmetic with timedelta
   # assuming datetime has been imported as a full module
   >>> now = datetime.datetime.today()
   # See the date represented as today
   >>> now
   datetime.datetime(2011, 11, 24, 12, 40, 57, 433000)
   # Add thirty days to today
   >>> now += datetime.timedelta(days=30)
   # View the new date
   >>> now
   datetime.datetime(2011, 12, 24, 12, 40, 57, 433000)