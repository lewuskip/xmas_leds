
class WindowElement:
	def __init__(self, lednum_start, len):
		self.lednum_start = lednum_start
		self.len = len
		
		self.front_refs = []
		self.back_refs = []
		
class WindowsLayout:
	def __init__(self):

		self.elements = []
		
		for x in range(12):
			self.elements.append(WindowElement(0+x*26,  26))
	
		self.elements[0].front_refs.append(self.elements[1])
		self.elements[0].back_refs.append(self.elements[5])
		
		self.elements[1].front_refs.append(self.elements[2])
		self.elements[1].back_refs.append(self.elements[0])
		
		self.elements[2].front_refs.append(self.elements[3])
		self.elements[2].front_refs.append(self.elements[8])
		self.elements[2].back_refs.append(self.elements[1])

		self.elements[3].front_refs.append(self.elements[4])
		self.elements[3].back_refs.append(self.elements[2])

		self.elements[4].front_refs.append(self.elements[5])
		self.elements[4].front_refs.append(self.elements[11])
		self.elements[4].back_refs.append(self.elements[3])

		self.elements[5].front_refs.append(self.elements[0])
		self.elements[5].back_refs.append(self.elements[4])
		self.elements[5].back_refs.append(self.elements[11])

if __name__ == "__main__":
	print "Start"
	import pdb
	pdb.set_trace()
	windows = WindowsLayout()
	print windows
	
	