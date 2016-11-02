class Time(object):
    """ represents the time of day.
    attributes: hour, minute, second"""

#used the same time as before because why not
time1 = Time()
time1.hour = 7
time1.minute = 36
time1.second = 15

time2 = Time()
time2.hour = 4
time2.minute = 57
time2.second = 28


def is_after(t1, t2):
    time1_total = (time1.hour * 3600) + (time1.minute * 60) + time1.second
    # multiply by 3600 for total seconds in a day, multiply by 60 for total minutes in an hour
    time2_total = (time2.hour * 3600) + (time2.minute * 60) + time2.second
    # multiply by 3600 for total seconds in a day, multiply by 60 for total minutes in an hour
    return time1_total > time2_total

print is_after(time1, time2)
