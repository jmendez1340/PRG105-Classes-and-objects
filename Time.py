class Time(object):
    """ represents the time of day.
    attributes: hour, minute, second"""

time = Time()
time.hour = 7
time.minute = 36
time.second = 15

def print_time(time):
    print "%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second)

print_time(time)