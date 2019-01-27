
# coding: utf-8

# In[1]:


###########################################
#   107-1 Data Structure and Programming
#   Programming Assignment #4
#   Instructor: Pei-Yuan Wu
############################################

import sys

# **********************************
# *  TODO                          *
# **********************************
'''
You need to complete this class MinBinaryHeap()
Feel free to add more functions in this class.
'''
class MinBinaryHeap():
    def __init__(self):
        self.heap = [0] # with a dummy node
        self.currentSize = 0
#------------------------------------------------------insert part        
    def upheap(self , i):
        #i 一開始對應到到的是最後一個node
        while i // 2 > 0 : 
            if self.heap[i] < self.heap[i//2] : #i(子) i//2(超) ==> i < i//2 往上轉
                temp = self.heap[i//2]
                self.heap[i//2] = self.heap[i]
                self.heap[i] = temp
            i = i // 2 #往上指一層parent
        
    def insert(self, item):
        self.heap.append(item)
        self.currentSize = self.currentSize + 1
        self.upheap(self.currentSize)
        #print(self.heap)
#----------------------------------------------------------deleteMin part
    
    def downheap(self , i):
        while (i*2) <= self.currentSize:
            min_child = self.findminc(i) #記得self
            if self.heap[i] > self.heap[min_child]:  #i: 超 
                temp = self.heap[i]
                self.heap[i] = self.heap[min_child]
                self.heap[min_child] = temp
            i = min_child
            

    def findminc(self , i):
        # i 指向操作中的node
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heap[i*2] < self.heap[i*2 + 1]:
                return i * 2
            else : 
                return i * 2 + 1
        
    
    def deleteMin(self):

        self.heap[1] = self.heap[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heap.pop()
        self.downheap(1)
        #print(self.heap)


    def findMin(self):
        
        min_ = self.heap[1]
        
        return min_
    

    def size(self):

        return self.currentSize
    
    def string(self):
        # Convert self.heap into a string
        return list2String(self.heap[1:])

def list2String(l):
    formatted_list = ['{}' for item in l ] 
    s = ','.join(formatted_list)
    return s.format(*l)


# In[2]:



if __name__ == '__main__':
    # 1. Check the command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 programming_hw4.py <input> <output>")
    
    # 2. Read the input file
    inFile = open(sys.argv[1], 'r')
    input_line_list = list(inFile.read().splitlines())
    input_cmd_list = [ line.split(' ') for line in input_line_list ]
    #print(input_cmd_list) #test
    inFile.close()

    # 3. Solve
    minPQ = MinBinaryHeap()
    findMin_list = []
    for cmd in input_cmd_list:
        if cmd[0] == 'insert':
            # print('insert {}'.format(cmd[1]))
            minPQ.insert(int(cmd[1]))
        elif cmd[0] == 'deleteMin':
            # print('deleteMin')
            if minPQ.size() > 0:
                minPQ.deleteMin()
        elif cmd[0] == 'findMin':
            # print('findMin')
            if minPQ.size() > 0:
                findMin_list.append(minPQ.findMin())
            else:
                findMin_list.append('-')
        else: # Unknown command
            assert False
        # print(minPQ.string())
    
    # 4. Output answers
    outFile = open(sys.argv[2], 'w')
    # 4.1 Output FindMin string
    outFile.write('{}\n'.format(list2String(findMin_list)))
    # 4.2 Output minPQ string
    outFile.write('{}'.format(minPQ.string()))
    outFile.close()
    #print(list2String(findMin_list))
    #print(minPQ.string())

