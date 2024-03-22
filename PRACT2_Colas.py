

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.top = self.top.next
            self.size -= 1
            return data
        return None

    def get_top(self):
        return self.top.data if self.top else None

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if not self.front:
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.front:
            data = self.front.data
            self.front = self.front.next
            self.size -= 1
            if not self.front:
                self.rear = None
            return data
        return None

    def get_front(self):
        return self.front.data if self.front else None

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def get_nth(self, pos):
        if pos < 0 or pos >= self.size:
            return None
        current = self.front
        for _ in range(pos):
            current = current.next
        return current.data

class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print_info(self):
        print("     Customer:", self.customer)
        print("     Quantity:", self.qtty)
        print("     ------------")

class TestQueue:
    @staticmethod
    def print_info(queue):
        print("********* QUEUE DUMP *********")
        print("   Size:", queue.get_size())
        print("   ** Elements **")
        current = queue.front
        count = 1
        while current:
            print("   ** Element", count)
            current.data.print_info()
            current = current.next
            count += 1
        print("******************************")

if __name__ == "__main__":

    queue = Queue()
    order1 = Order(20, "cust1")
    order2 = Order(30, "cust2")
    order3 = Order(40, "cust3")
    queue.enqueue(order1)
    queue.enqueue(order2)
    queue.enqueue(order3)

    print("Front:")
    queue.get_front().print_info()
    print("Dequeue:")
    queue.dequeue().print_info()
    print("Front:")
    queue.get_front().print_info()

    TestQueue.print_info(queue)

    print("Nth element at position 2:", queue.get_nth(2))