class Queue_structure:
    def __init__(self):
      self.in_val = Stack_structure()
      self.out_val = Stack_structure()

    def check_empty(self):
      return (self.in_val.check_empty() and self.out_val.check_empty())

    def enqueue_operation(self, data):
      self.in_val.push_operation(data)

    def dequeue_operation(self):
      if self.out_val.check_empty():
         while not self.in_val.check_empty():
            deleted_val = self.in_val.pop_operation()
            self.out_val.push_operation(deleted_val)
      return self.out_val.pop_operation()
  
    def display1(self) :
        self.out_val.items.reverse()
        print(self.out_val.items)

    def display2(self) :
        print(self.in_val.items)

class Stack_structure:
   def __init__(self):
      self.items = []

   def check_empty(self):
      return self.items == []

   def push_operation(self, data):
      self.items.append(data)

   def pop_operation(self):
      return self.items.pop()

my_instance = Queue_structure()

while True:
   print('1.enqueue')
   print('2.dequeue')
   print('3.quit')
   operation = int(input('What operation would you like to perform ? : '))

   
   if operation == 1:
       ele = int(input("Enter data to be pushed : "))
       my_instance.enqueue_operation(ele)
       my_instance.display2()
   elif operation == 2:
      if my_instance.check_empty():
         print('The queue is empty')
      else:
         deleted_elem = my_instance.dequeue_operation()
         print('The deleted element is : ', int(deleted_elem))
         my_instance.display1()
   elif operation == 3:
      break