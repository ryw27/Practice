class node:
    def __init__(self,element,lc=None,rc=None,parent=None):
        self.element = element
        self.lc = lc
        self.rc = rc
        self.parent = parent
class BTreePrinter: 
    @staticmethod
    def maxLevel(node):
        if (node == None):
            return 0
        else:
            return max(BTreePrinter.maxLevel(node.rc),BTreePrinter.maxLevel(node.lc)) + 1
    @staticmethod
    def printnode(root):
        maxlevel = BTreePrinter.maxLevel(root)
        BTreePrinter.printnodeinternal([root],1,maxlevel)
    
    @staticmethod
    def elementsnull(nodes):
        for i in range(len(nodes)):
            if (nodes[i] != None):
                return False
        return True
    @staticmethod
    def printnodeinternal(nodes,level,maxlevel):
        if len(nodes) == 0 or BTreePrinter.elementsnull(nodes):
            return
        floor = maxlevel - level
        edgelines = int(2 ** max(floor - 1,0))
        firstspaces = int(2 ** floor) - 1
        betweenspaces = int(2 ** (floor + 1)) - 1
        BTreePrinter.printwhitespaces(firstspaces)
        nextnodes = []
        for i in range(len(nodes)):
            if (nodes[i] != None):
                print(nodes[i].element,end="")
                nextnodes.append(nodes[i].lc)
                nextnodes.append(nodes[i].rc)
            else:
                nextnodes.append(None)
                nextnodes.append(None)
                print(" ",end="")
            BTreePrinter.printwhitespaces(betweenspaces)
        
        print("")
        for i in range(1,edgelines + 1):
            for j in range(len(nodes)):
                BTreePrinter.printwhitespaces(firstspaces - i)
                if (nodes[j] == None):
                    BTreePrinter.printwhitespaces(edgelines + edgelines + i + 1)
                    continue
                if nodes[j].lc != None:
                    print("/",end="")
                else:
                    (BTreePrinter.printwhitespaces(1))
                BTreePrinter.printwhitespaces(i + i - 1) 
                if nodes[j].rc:
                    print("\\",end="")
                else:
                    (BTreePrinter.printwhitespaces(1))

                BTreePrinter.printwhitespaces(edgelines + edgelines - i)
            print("")
        BTreePrinter.printnodeinternal(nextnodes,level + 1,maxlevel)
    @staticmethod
    def printwhitespaces(num):
        for i in range(num):
            print(" ",end="")
def findparents(nodes):
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if nodes[j].lc == nodes[i] or nodes[j].rc == nodes[i]:
                nodes[i].parent = nodes[j]


def preorderwalk(node):
    if (node != None):
        print(node.element)
        preorderwalk(node.lc)
        preorderwalk(node.rc)
def inorderwalk(node):
    if (node != None):

        inorderwalk(node.lc)
        print(node.element)
        inorderwalk(node.rc)
def postorderwalk(node):
    if node != None:
        postorderwalk(node.lc)
        postorderwalk(node.rc)
        print(node.element)
def treesearch(node,key):
    if (node ==  None):
        return None
    else:
        if key > node.element:
            return treesearch(node.rc,key)
        elif key < node.element:
            return treesearch(node.lc,key)
        else:
            return node.element
def min_tree(root):
    while (root!= None):
        if (root.lc == None):
            return root
        root = root.lc
def max_tree(root):
    while(root != None):
        if (root.rc == None):
            return root
        root = root.rc
def insert(newnode,root):
    x = root
    parent = None
    while (x != None):
        parent = x
        if newnode.element > x.element:
            x = x.rc
        else:
            x = x.lc

    createnode = node(newnode.element,None,None,parent)

    if createnode.element < parent.element:
        parent.lc = createnode
    else:
        parent.rc = createnode 
    return parent.element
def transplant(org,rep):
    if org.parent.lc == org:
        org.parent.lc = rep
    else:
        org.parent.rc = rep
    if (rep != None):
        rep.parent = org.parent
def delete(node):
    if node.lc == None:
        transplant(node,node.rc)
    elif node.rc == None:
        transplant(node,node.lc)
    else:
        rep = min_tree(node.rc)
        if rep != node.rc:
            transplant(rep,rep.rc)
            rep.rc = node.rc
            rep.rc.parent = rep
        transplant(node,rep)
        rep.lc = node.lc
        rep.lc.parent = rep
    
def main():
    d = node(2)
    e = node(8)
    f = node(10)
    g = node(15)
    b = node(7,d,e)
    c = node(12,f,g) 
    a = node(9,b,c)
    root = a
    findparents([a,b,c,d,e,f,g])
    #inorderwalk(root)
    #preorderwalk(root)
    #postorderwalk(root)
    print(treesearch(root,3))
    print(min_tree(root))
    print(max_tree(root))
    x = BTreePrinter()
    print(x.printnode(root))
    h = node(20)
    insert(h,root)
    findparents([a,b,c,d,e,f,g,h])
    x.printnode(root)
if __name__ == "__main__":
    main()
