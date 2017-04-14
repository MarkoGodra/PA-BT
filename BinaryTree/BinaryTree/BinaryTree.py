import sys
import random

#random list generator
def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

#class for nodes
class Node :
    def __init__(self, data) :
        self.p = None
        self.r = None
        self.l = None
        self.data1 = data   
        self.data2 = str(data)

#tree class
class Tree :
    #root is only field
    
    #constructor
    def __init__(self) :
        self.root = None

    #method for adding nodes to tree
    def add(self, val) : #same as insert method from PDF
        if(self.root == None) :
            self.root = Node(val)
        else :
            self._add(val, self.root)

    #side method for recursive adding
    def _add(self, val, node) :
        #if less add it to left side
        if(val < node.data1) :
            if(node.l != None) :
                self._add(val, node.l)
            else :
                node.l = Node(val)
                node.l.p = node
        #if val is greater add it to right side
        else :
            if(node.r != None) :
                self._add(val, node.r)
            else :
                node.r = Node(val)
                node.r.p = node

    #In-Order-Walk
    def in_order_walk(self, node) :
        if(node != None) :
            self.in_order_walk(node.l)
            print("print node data : ", node.data1, node.data2)
            self.in_order_walk(node.r)

    #Print-root
    def print_root(self) :
        print("Data in root node", self.root.data1, self.root.data2)

    #Search the tree for wanted key
    def tree_search(self, current, key) :
        if (current == None or key == current.data1) :
            return current
        if (key < current.data1) :
            return self.tree_search(current.l, key)
        else :
            return self.tree_search(current.r, key)

    #Search the tree for wanted key iterative way
    def iterative_tree_search(self, current, key) :
        while (current != None and key != current.data1) :
            if (key  < current.data1) :
                current = current.l
            else :
                current = current.r
        return current

    #Find the tree minimum
    def tree_minimum(self, node) :
        while (node.l != None) :
            node = node.l
        return node

    #Find tree maximum
    def tree_maximum(self, node) :
        while(node.r != None) :
            node = node.r
        return node

    #Print node's parent
    def print_parrent(self, node) :
        if (node.p != None) :
            print("Parent node of node ", node.data1, "is", node.p.data1)
        else :
            print("The node ", node.data1, "is root")

    #Transplant
    def transplant(self, u, v) :
        if (u.p == None) :
            self.root = v
        elif (u == u.p.l) :
            u.p.l = v
        else :
            u.p.r = v
        if (v != None) :
            v.p = u.p   

    #Deleting node
    def delete(self, node) :
        if (node.l == None) :
            self.transplant(node, node.r)
        elif (node.r == None) :
            self.transplant(node, node.l)
        else :
            y = self.tree_minimum(node.r)
            if (y.p != z) :
                self.transplant(y, y.r)
                y.r = node.r
                y.r.p = y
            self.transplant(node, y)
            y.l = node.l
            y.l.p = y

    #In-Order-Walk-With-RetVal
    def in_order_walk_with_retval(self, node) :
        global x
        if(node != None) :
            self.in_order_walk_with_retval(node.l)
            x.append(node)
            self.in_order_walk_with_retval(node.r)
        

 
x = list()

#Testing here
tree = Tree();
A = random_list(0, 20, 10)
print(A)
key = A[9]
key_i = A[6]
key_invalid = 100

for i in range(0, len(A)) :
    tree.add(A[i])

tree.print_root()

#testing in order walk
tree.in_order_walk(tree.root)

#testing tree search
f_k = tree.tree_search(tree.root, key)
if (f_k != None) : 
    print("Found the key", f_k.data1, "and we searched for ", key)
else :
    print("No key", key, "found")

f_k = tree.tree_search(tree.root, key_invalid)
if (f_k != None) : 
    print("Found the key", f_k.data1, "and we searched for ", key_invalid)
else :
    print("No key", key_invalid, "found")


#testing iterative search
f_k_i = tree.iterative_tree_search(tree.root, key_i)
if (f_k_i != None) : 
    print("Found the key", f_k_i.data1, "and we searched for ", key_i)
else :
    print("No key", key_i, "found")

#testing tree minimum
temp = tree.tree_minimum(tree.root)
print("Tree minimum", temp.data1)

#testing tree maximum
temp = tree.tree_maximum(tree.root)
print("Tree minimum", temp.data1)

#testing print parent
tree.print_parrent(temp)
tree.print_parrent(tree.root)

#Testing inserting
print("Inserting 110 and -5 to tree")
tree.add(110)
tree.add(-5)
tree.in_order_walk(tree.root)
#testing tree minimum
temp = tree.tree_minimum(tree.root)
print("Tree minimum", temp.data1)
#testing tree maximum
temp = tree.tree_maximum(tree.root)
print("Tree minimum", temp.data1)

#testing print parent
tree.print_parrent(temp)

#Trying to delete maximum
temp = tree.tree_maximum(tree.root)
tree.delete(temp)
print("Tree after deleting max")
tree.in_order_walk(tree.root)

#Trying to delete minimum
temp = tree.tree_minimum(tree.root)
tree.delete(temp)
print("Tree after deleting min")
tree.in_order_walk(tree.root)

print("########")

tree.in_order_walk_with_retval(tree.root)


for i in x :
    print(i.data1)



