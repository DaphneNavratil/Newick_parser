#Import libraries
import sys


# Read the file given in argument (path) and return the string corresponding to the tree in newick format
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            newick = file.read()
            while newick.endswith('\n'):
                newick = newick[:-1] 
            return newick
    except FileNotFoundError:
        print(f"File {file_path} unfound.\n")
        return ""
    except Exception as exception:
        print(f"Error, can't read the file: {exception}\n")
        return ""

# A tree is made of nodes
class Node:
    def __init__(self, name):
        self.name = name # label of the node
        self.leftChild = None 
        self.rightChild = None

# Create the tree from the Newick format (string) and return the root of the tree
def newick_to_tree(newick_list):

    current_node = None 
    memory = [] 
    left = True 
    
    if len(newick_list)<=3: # The tree is a leaf or the Newick format is wrong
        return None

    for i in newick_list[:-1]:
        if i == "(" :
            if current_node == None :
                current_node = Node("")
                root = current_node
               
            elif left:
                current_node.leftChild = Node("")
                current_node = current_node.leftChild
            else :
                current_node.rightChild = Node("")
                current_node = current_node.rightChild
                
            memory.append(current_node)
            left = True

        elif i == ")" :
            current_node = memory[-2] 
            memory.pop() 

        elif i == "," :
            left = False

        elif i!=";" :
            if left: 
                if current_node.leftChild == None :
                    current_node.leftChild = Node(i) 
                    
                else :
                    current_node.leftChild.name += i 
            else : 
                if current_node.rightChild == None :
                    current_node.rightChild = Node(i)            
                else :
                    current_node.rightChild.name += i
    return root
