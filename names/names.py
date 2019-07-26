import time
# from binary_search_tree import BinarySearchTree


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                # recursive to keep going until we find an empty spot
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        # base case no value or value is the root

        if self.value == target:
            return True
        
        elif self.value < target:
            if self.right:
                return self.right.contains(target)
            
        else:
            if self.left:
                return self.left.contains(target)
        

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# runtime: 9.06782841682434 seconds


bst = BinarySearchTree("")
# put all the names from the first list into a search tree
for name in names_1:
    bst.insert(name)
# for each name in the second list, check to see if it is contained in the first list now in the tree
for name in names_2:

    if bst.contains(name):
        # if the name is a duplicate, insert it into the duplicate list
        duplicates.append(name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
