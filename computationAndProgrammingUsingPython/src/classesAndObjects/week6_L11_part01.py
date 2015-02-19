class Clock(object):
  def __init__(self, time):
    self.time = time

  def print_time(self):
    time = "6:30" #assignment creates a new time variable (do not use self)
    print self.time

clock = Clock("5:30")
clock.print_time() #Result is "5:30"

class Clock1(object):
  def __init__(self, time):
    self.time = time

  def print_time(self, time):
    print time #Note print out the "argument" time (do not use self)

clock1 = Clock1("5:30")
clock1.print_time("10:30")

class Clock2(object):
  def __init__(self, time):
    self.time = time

  def print_time(self):
    print self.time #Print out the "time" instance variable

boston_clock2 = Clock2("5:30")
paris_clock2 = boston_clock2

paris_clock2.time = "10:30"
boston_clock2.print_time() #Note that boston_clock2 and paris_clock2 point to the same instance

print "Is instance of Clock2?", isinstance(paris_clock2, Clock2)
print "Type of paris_clock2 instance:", type(paris_clock2)
print "Are paris_clock2 and boston_clock2 the same instance obj?", (paris_clock2 == boston_clock2)

print "paris_clock2", paris_clock2
print "boston_clock2", boston_clock2
#if you want to override the behaviour the __str__ method must be overriden in Clock2 class


