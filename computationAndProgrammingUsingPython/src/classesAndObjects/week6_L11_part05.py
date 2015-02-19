class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each integer in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def __len__(self):
		return len(self.vals)

    def intersect(self, other):
		result = intSet()
		for e in self.vals:
			if e in other.vals:
				result.insert(e)
		return result

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
        Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')



s = intSet()
print s
s.insert(3)
s.insert(4)
s.insert(9)
s.insert(5)
print s

t = intSet()
print t
t.insert(1)
t.insert(4)
t.insert(15)
t.insert(90)
print t

print t.__len__()
print len(t)

print s.intersect(t)
