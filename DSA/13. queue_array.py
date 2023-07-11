# Queue implementation in Python

class Queue:

    def __init__(self):
        self.queue = []

    def create(self) :
        size = int(input("Enter the size of Queue : "))
        for i in range(size) :
            val = int(input(f"Enter value for index {i+1} : "))
            self.enqueue(val)

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

a_queue = Queue()
a_queue.create()
while True:
    print('\n1.enqueue')
    print('2.dequeue')
    print('3.display\n4.quit')
    do = input('Enter your choice : ')
 
    if do == '1':
        val=int(input('Enter value to enqueue : '))
        a_queue.enqueue(val)
        a_queue.display()

    elif do == '2':
        dequeued = a_queue.dequeue()
        if dequeued is None:
            print('\nQueue is empty.')
        else:
            print('Dequeued element: ', int(dequeued))
            a_queue.display()
    elif do == '3':
        a_queue.display()

    elif do == '4' :
        break

    else : 
        print("Enter valid choice")