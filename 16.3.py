class Time(object):
    """ represents the time of day.
    attributes: hour, minute, second
    """

time = Time()
time.hour = 6
time.minute = 24
time.second = 30


def increment(time, seconds):
    print ("Originally the time was: %.2d:%.2d:%.2d"
          % (time.hour, time.minute, time.second))

    time.second += seconds
    if time.second >= 59:  # if the number is greater than 59 it's broken down >
        quotient, remainder = divmod(time.second, 60)  # divmod divides first argument by the second
        time.minute += quotient
        time.second = remainder
    if time.minute >= 59:   # if the number is greater than 59 it's broken down >
        quotient, remainder = divmod(time.minute, 60)  # divmod divides first argument by the second
        time.hour += quotient
        time.minute = remainder
    if time.hour >= 12:   # don't want to deal with military time so 12 will suffice >
        time.hour -= 12

    print "The time now is: %.2d:%.2d:%.2d" % (time.hour, time.minute, time.second)

increment(time, 600)
# use any increment you want
# I used 600 because 600 seconds is a guaranteed 10 minutes if not something went wrong
