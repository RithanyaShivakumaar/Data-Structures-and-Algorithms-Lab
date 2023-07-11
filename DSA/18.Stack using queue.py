class Stack_structure:
   def __init__(self):
      self.q = Queue_structure()

   def check_empty(self):
      return self.q.check_empty()

   def push_val(self, data):
      self.q.enqueue_operation(data)

   def pop_val(self):
      for _ in range(self.q.size_calculate() - 1):
         dequeued = self.q.dequeue_operation()
         self.q.enqueue_operation(dequeued)
      return self.q.dequeue_operation()
  
   def display1(self) :
      print(list(reversed(self.q.items)))

   def display2(self) :
      print(list(reversed(self.q.items)))
      
  
class Queue_structure:
   def __init__(self):
      self.items = []
      self.size = 0

   def check_empty(self):
      return self.items == []

   def enqueue_operation(self, data):
      self.size += 1
      self.items.append(data)

   def dequeue_operation(self):
      self.size -= 1
      return self.items.pop(0)

   def size_calculate(self):
      return self.size
    
my_instance = Stack_structure()

print('Menu')
print('1.push ')
print('2.pop')
print('3.quit')

while True:
   operation = int(input('What operation number would you like to perform ? '))

   
   if operation == 1:
      ele = int(input("Enter data to be pushed : "))
      my_instance.push_val(ele)
      my_instance.display2()
   elif operation == 2:
      if my_instance.check_empty():
         print('The stack is empty.')
      else:
         print('The deleted value is : ', my_instance.pop_val())
         my_instance.display1()
   elif operation == 3:
      break