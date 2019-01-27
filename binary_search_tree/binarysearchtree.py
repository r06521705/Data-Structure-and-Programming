#############################################
#   107-1 Data Structure and Programming
#   Programming Assignment #3
#   Instructor: Pei-Yuan Wu
############################################

# Do not import any other library
import sys

# **********************************
# *  TODO                          *
# **********************************


# You may need this node class for implementation of tree.
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def binary_insert(root , node ):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                binary_insert(root.left , node)
        else:
            if root.right is None:
                root.right = node
            else:
                binary_insert(root.right , node)


def preorder_print(root):
    temp = []
    if root is not None:
        temp.append(root.data)
        temp.extend(preorder_print(root.left))
        temp.extend(preorder_print(root.right))
    return temp

def postorder_print(root):
    temp = []
    if root is not None:
        temp.extend(postorder_print(root.left))
        temp.extend(postorder_print(root.right))
        temp.append(root.data)
    return temp
    
def preorder_check(input_string):
#先用input(順)建一棵樹，在和原input做比較，如不同則return '-' , 依樣後再做後續另外一種order
    temp = input_string.split(",")
    b = list(map(int , temp))
    #------bulid the tree
    for i in range(len(b)):
        if i == 0 :
            r = Node(b[i])
        else:
            binary_insert(r,Node(b[i]))
    temp2 = preorder_print(r)
    if b != temp2:
        return '-'
    else:
        ans = postorder_print(r)
        ans = list(map(str , ans))
        ans_str = ','.join(ans)
        return ans_str
    

# This function is for checking if a sequence can be a postorder of BST or not.
# if yes, return the preorder traversal of the BST.
# if not, return '-'.
def postorder_check(input_string):
#先用input(反)建一棵樹，在和原input做比較，如不同則return '-' , 依樣後再做後續另外一種order
    temp = input_string.split(",")
    b = list(map(int , temp))
    b_or = b.copy()
    b.reverse()
    #------bulid the tree
    for i in range(len(b)):
        if i == 0 :
            r = Node(b[i])
        else:
            binary_insert(r,Node(b[i]))
    temp2 = postorder_print(r)
    if b_or != temp2:
        return '-'
    else:
        ans = preorder_print(r)
        ans = list(map(str , ans))
        ans_str = ','.join(ans)
        return ans_str

# **********************************
# *  Do NOT modify the code below  *
# **********************************
if __name__ == '__main__':
    # 1. Check the command line arguments
    if len(sys.argv) != 4:
        sys.exit("Usage: python3 programming_hw3.py <-pre | -post> <input> <output>")
    
    # 2. Read the input file
    inFile = open(sys.argv[2], 'r')
    input_list = list(inFile.read().splitlines())
    inFile.close()
    # print(input_list)

    # 3. Solve
    if sys.argv[1] == '-pre':
        answer_list = [ preorder_check(s) for s in input_list ]
    elif sys.argv[1] == '-post':
        answer_list = [ postorder_check(s) for s in input_list ] 
    # print(answer_list)

    # 4. Output answers
    outFile = open(sys.argv[3], 'w')
    for ans in answer_list:
        outFile.write('{}\n'.format(ans))
    outFile.close()
