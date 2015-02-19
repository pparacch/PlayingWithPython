class Queue(object):

	def __init__(self):
		self.vals = []
	
	def insert(self, element):
		self.vals.append(element)

	def remove(self):
		try:
			return self.vals.pop()
		except:
			raise ValueError("Elements not found")

q = Queue()
q.insert(5)
q.insert(6)

print q.remove()

q.insert(7)
print q.remove()

print q.remove()
print q.remove()

