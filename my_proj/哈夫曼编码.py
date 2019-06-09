def findTheFrequency(text):
    result=dict()
    with open(text,'r') as f:
        for line in f.readlines():
            line = line.lower()
            for i in line:
                if i.isalpha():
                    if i in result:
                        result[i]+=1
                    else:
                        result.update({i:1})
    return result
text="test.txt"
result=findTheFrequency(text)
class Node:
    def __init__(self):
        self.frequency=0
        self.name=None
        self.lchild=None
        self.rchild=None
        self.code=None
    def __lt__(self,other):
        return self.frequency<other.frequency

# establish the Huffman Tree
def estblishHuffmanTree(info_dict):
    #output: the base node
    node_list=[]
    for i in info_dict:
        a = Node()
        a.frequency=info_dict[i]
        a.name=i
        node_list.append(a)
    while len(node_list)>1:
        node_list.sort(reverse=True)
        node_1 = node_list.pop()
        node_2 = node_list.pop()
        new_node = Node()
        new_node.frequency=node_1.frequency+node_2.frequency
        new_node.lchild=node_1
        new_node.rchild=node_2
        node_list.append(new_node)
    return new_node
base_node = estblishHuffmanTree(result)
def encode(node, rst_dict, code):
    if node.name:
        rst_dict.update({node.name: code})
        return
    code += '0'
    encode(node.lchild, rst_dict, code)
    code = code[:-1]
    code += '1'
    encode(node.rchild, rst_dict, code)
    return rst_dict


code_dict = encode(base_node, {}, '')
code_text = "GreA3_Huffman_code.txt"


def encode_text(code_dict, text, code_text):
    string = ''
    with open(text, 'r') as f:
        for line in f.readlines():
            line = line.lower()
            for i in line:
                if i.isalpha():
                    string += code_dict[i]
                else:
                    string += '\n'
    with open(code_text, 'w') as f:
        f.write(string)


encode_text(code_dict, text, code_text)