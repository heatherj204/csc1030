'''
    wite a functino using the quese data structure to generate a sequnece of binary numbers from 1 to n.

    Example:
    Given n=16 the binary seguence is 1 10 11 100 101 110 111 1000 1001 1010 1011 1100 1101 1111 10000
'''

from queue_imp import Queue

def genNumbers(n=16):

    queue = Queue()

    queue.enqueue('1')

    res = []

    for _ in range(n):
        current = queue.dequeue()

        queue.enqueue(current + '0')
        queue.enqueue(current + '1')

def lifi_test(str='EAS*Y*QUE***ST***IO*N**'):

    stack = Stack()
    res = []
    for c in str:
        if c == '*':
            res.append(stack.pop())
        else:
            stack.push(c)

    return res
