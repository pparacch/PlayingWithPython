class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x #x not defined (do not use self) 
    def getY(self):
        return y #y do not defined (do not use self)

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8

print "X: %d, Y: %d" % (X, Y)

#q1
w1 = Weird(X, Y)
#print w1.getX() #Throws an error cause variable x do not exist
#print w1.getY() #Throws an error cause variable y do not exist

w2 = Wild(X, Y)
print "w2 = Wild(X, Y)"
print "w2.getX(): %d" % w2.getX()
print "w2.getY(): %d" % w2.getY()

w3 = Wild(17,18)
print "w3 = Wild(17,18)"
print "w3.getX(): %d" % w3.getX()
print "w3.getY(): %d" % w3.getY()

w4 = Wild(X, 18)
print "w4 = Wild(X, 18)"
print "w4.getX(): %d" % w4.getX()
print "w4.getY(): %d" % w4.getY()

X = w4.getX() + w3.getX() + w2.getX()
print "X = w4.getX() + w3.getX() + w2.getX() ->", X
print "w4.getX(): %d" % w4.getX()

Y = w4.getY() + w3.getY()
Y = Y + w2.getY()
print "Y = w4.getY() + w3.getY(); Y = Y + w2.getY() - Y: %d " % Y
print "w2.getY(): %d" % w2.getY()




