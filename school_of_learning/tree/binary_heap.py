# -*- encoding: utf-8 -*-
########################################
#
#   Author: Md. Mehedi Hasan
#   Email: git.mehedi@gmail.com
#
#   Binary Heap Algorithm Process and Main Functionality
#   Main Function:
#   ---------------
#   1. Insert into Heap
#   2. Delete from Heap
#   3. Build Heap
#   4. Percolating Heap Down and Up
#
########################################


class BinaryHeap(object):

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize+1
        self.percolate_up(self.currentSize)

    def percolate_up(self, i):
        while i // 2 >0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def print_list(self):
        print self.heapList

b = BinaryHeap()

for i in [12,10,11,14,15,2,6]:
    b.insert(i)

b.print_list()
