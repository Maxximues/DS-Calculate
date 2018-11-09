#2018.11.06
#singly_linked_list
 
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class link_list:
	def __init__(self):
		# initialize linklist
		self.head = None 

	def insert_head(self, data):
		newnode = Node(data)
		if self.head != None:
			newnode.next = self.head
		self.head = newnode

	def insert_tail(self, data):
		if self.head is None :self.insert_head(data)
		else:
			temp = self.head
			while temp.next != None:
				temp = temp.next
			temp.next = Node(data)

	def printlist(self):
		tamp = self.head
		if tamp is None:
			print("list is Empty")
		while tamp is not None:
			print(tamp.data)
			tamp = tamp.next

	def delete_tail(self):
		tamp = self.head
		if self.head != None:
			if self.head.next is None:
				self.head = None
			else:
				while tamp.next.next is not None:
					tamp = tamp.next
				tamp.next, tamp = None, tamp.next
		return tamp

	def isEnmpty(self):
		self.head = None


def main():
	A = link_list()
	for i in range(3):
		print("Inserting num at head")
		A.insert_head(int(input()))
	print("Inserting num at tail")
	A.insert_tail(int(input()))
	print("Print list")
	A.printlist()
	print("Delete tail")
	A.delete_tail()
	A.printlist()
	print("Empty list")
	A.isEnmpty()
	A.printlist()


if __name__ == '__main__':
	main()
