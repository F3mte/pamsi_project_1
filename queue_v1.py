import sys
import os
import time
import random as rn
import threading

# Constants used while generating random number
min_val = 10
max_val = 20

# Flag used to switch on/off function via menu
flag = 0
peek_flag = 0
enqueue_flag = 0
dequeue_flag = 0


class Queue:
    # Constructor with parameter for maximum amount of elements in queue
    def __init__(self, amount_of_elements=1):

        self.front = 0  # Front specifies position of first element in queue
        self.rear = 0  # Rear specifies position for next element

        self.amount_of_elements = amount_of_elements  # Maximum amount of elements in queue
        self.queue_size = self.amount_of_elements + 1  # Size of queue with one empty position for rear
        self.queue = [None for _ in range(self.queue_size)]  # Empty list that works as queue

        # self.queue2 = []  # Temporary queue used while extending the full queue
        # self.queue_size2 = amount_of_elements + 1

    # Function returns amount of elements in queue
    def check_amount(self):
        return (self.queue_size + self.rear - self.front) % self.queue_size

    # Function returns 1 if queue is empty (front and rear are on the same position)
    def check_if_empty(self):
        return self.front == self.rear

    # Function returns 1 if queue is full (rear is on last position and front on 0 position)
    def check_if_full(self):
        return self.check_amount() == (self.queue_size - 1)

    # Function that multiply size of queue times 2
    # def double_size(self, value):
    #     self.queue2 = [None for __ in range(self.amount_of_elements*2-1)]
    #     for it in range(self.queue_size):
    #         self.queue2[it] = self.queue[it]
    #     self.queue_size = self.queue_size*2-1
    #     self.queue = self.queue2
    #     self.queue[self.rear] = value
    #     print("Enqueued", value)
    #     self.rear = (self.rear + 1) % self.queue_size

    # Function adds value to queue
    def enqueue(self, value):
        # If queue is full, double size
        if self.check_if_full():
            # self.double_size(value)
            print("Queue is full! Please, free up some space!")
        # If queue is not full, then add value on first available position
        # Then increment tail, but if
        else:
            self.queue[self.rear] = value
            self.rear = (self.rear + 1) % self.queue_size

    # Function return first value from queue
    def dequeue(self):
        # If queue is empty, print warning
        if self.check_if_empty():
            print("Queue is empty! Cannot dequeue!")
        # If queue is not full, then add value on first available position
        # Then increment tail, but if tail is of the size of queue, then it equals 0
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.queue_size
            return temp

    # Function return value in front of queue without deleting it
    def peek(self):
        return self.queue[self.front]


# Callback that enqueue the random value, with random time interval
def enqueue_callback(min_value, max_value):
    global enqueue_flag
    # If enqueue_flag = 0, we dequeue value in front
    while True:
        while not enqueue_flag:
            random_number = rn.randint(min_value, max_value)
            q.enqueue(random_number)
            time.sleep(rn.random()*3+1)


# Callback that dequeue value in front of queue, with random time interval
def dequeue_callback():
    global dequeue_flag
    # If dequeue_flag = 0, we dequeue value in front
    while True:
        while not dequeue_flag:
            q.dequeue()
            time.sleep(rn.random()*3+1)


# Callback that displays a menu
def display_callback():
    while True:
        os.system('cls||clear')
        print("---------Menu---------")
        print("[1] Show front value")
        print("[2] Hide front value")
        print("[3] Stop enqueuing")
        print("[4] Start enqueuing")
        print("[5] Stop dequeuing")
        print("[6] Start dequeuing")
        print("[Ctrl + C] Quit")
        print("----------------------")
        # If peek_flag = 1, then program shows value in front
        if peek_flag == 1:
            print("Value in front:", q.peek())
        print("Size of queue:", q.check_amount())
        print("----------------------")
        time.sleep(1)


# Callback with endless loop that awaits for input
def input_callback():
    global enqueue_flag
    global dequeue_flag
    global peek_flag
    global flag
    # Loop that awaits for input
    while True:
        flag = int(input())
        # Set flag for showing value in front of queue
        if flag == 1:
            peek_flag = 1
        # Reset flag for showing value in front of queue
        elif flag == 2:
            peek_flag = 0
        # Set flag that stops enqueueing
        elif flag == 3:
            enqueue_flag = 1
        # Reset flag that stops enqueueing
        elif flag == 4:
            enqueue_flag = 0
        # Set flag that stops dequeuing
        elif flag == 5:
            dequeue_flag = 1
        # Reset flag that stops dequeuing
        elif flag == 6:
            dequeue_flag = 0
        else:
            pass


# Creating an object Queue that can contain 5 elements
q = Queue(int(sys.argv[1]))

# Initializing and starting timer, with a callback in which enqueueing happens
enqueue_timer = threading.Timer(2, enqueue_callback, args=(min_val, max_val))
enqueue_timer.start()

# Initializing and starting timer, with a callback in which dequeuing happens
dequeue_timer = threading.Timer(2, dequeue_callback)
dequeue_timer.start()

# Initializing and starting timer, with a callback in which menu is displayed
display_timer = threading.Timer(1, display_callback)
display_timer.start()

# Initializing and starting timer, with a callback in which flags are set or rest with input value
input_timer = threading.Timer(1, input_callback)
input_timer.start()
