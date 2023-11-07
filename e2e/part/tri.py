from part.extract_file_2_list import extract_file_2_list

class TrieNode:
    def __init__(self):
        self.children = []
        self.context = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_new(self, extract_list):
        #self.checklist
        root = self.root
        if len(root.children) == 0:
            root.context.append("THIS IS ROOT\n")
            root.children.append(TrieNode())
            self.insert(root.children[0],extract_list)
            return True
        else:
            for c in root.children:
                ok=self.insert(c,extract_list)
                if ok:
                    return True
            newNode=TrieNode()
            self.insert(newNode,extract_list)
            root.children.append(newNode)
            return True

    def insert(self,node,ls):
        this_node_len=len(node.context)
        if this_node_len == 0:
            node.context=ls
            return True
        if self.compare_line(node.context[0],ls[0]) is False:
            return False
        # totally same=0  partial same=1  left < right=2  left > right=3
        (rst,first_unsame_index)=self.compare_lists(node.context,ls)
        if rst==0:
            return True
        elif rst==1:
            lnode=TrieNode()
            lnode.context=node.context[first_unsame_index:]
            lnode.children=node.children
            rnode=TrieNode()
            self.insert(rnode,ls[first_unsame_index:])
            #same part
            node.context=node.context[:first_unsame_index]
            node.children=[]
            node.children.append(lnode)
            node.children.append(rnode)
            return True
        elif rst==2:
            #need to compare children
            if len(node.children) == 0:
                node.children.append(TrieNode())
                self.insert(node.children[0],ls[len:])
                return True
            else:
                for c in node.children:
                    ok=self.insert(c,ls[len:])
                    if ok:
                        return True
                newNode=TrieNode()
                self.insert(newNode,ls[len:])
                node.children.append(newNode)
                return True
        elif rst==3:
            #temporally I consider it reducdent
            return True
        else:
            assert 0
            
            
    def construct_trie_from_files(self, filenames):
        for filename in filenames:
            with open(filename, 'r') as file:
                for line in file:
                    for word in line.split():
                        self.insert(word)
    
    def insert_extract_file(self, test_file_name):
        extract_list=extract_file_2_list(test_file_name)
        self.insert_new(extract_list)

    def compare_line(self,line1,line2):
        assert line1.strip() != ""
        assert line2.strip() != ""
        if line1==line2:
            return True
        return False

    def compare_lists(self,ls1,ls2):
        #unexpected
        if self.compare_line(ls1[0],ls2[0]) is False:
            return -1
        len1=len(ls1)
        len2=len(ls2)
        mlen=min(len1,len2)
        for i in range(mlen):
            if self.compare_line(ls1[i],ls2[i]) is False:
                return (1,mlen-1)
        if len1==len2:
            return (0,-1)
        elif len1<len2:
            return (2,-1)
        else:
            return (3,-1)

    def print_tree(self):
        print("# This is auto-generated execution code")
        root=self.root
        assert len(root.children) != 0
        for c in root:
            if len(c.context) == 0:
                continue
            else:
                print(c.context)
                if len(c.children) == 0:
                    print("This brance over")
                    #goto duplicate page
                else:
                    do_next()





        
    

trie = Trie()
filenames = ['test_1236.py', 'test_1246.py']
trie.insert_extract_file('test_1236.py')
trie.insert_extract_file('test_1246.py')
trie.print_tree()