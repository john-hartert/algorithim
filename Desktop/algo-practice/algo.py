a = [1, 2, 3, 4, 5]
for i in range(len(a)):
    print hex(id(a[i]))



# In arrays the numbers have to be next to eachother.
# If you try to add another number at the end of and array but that space is being taken up
# from other memory(program). So, everything has to move.

# Linked list has a head and a tail. Each node points to the next node.
# A node holds a value and a next property. Next is the node of the next value in the chain.

# Linked list is an object. Head (first node in the list) and a tail (last node in the list).
# A tree is a linked list.

# Tail continuously stays empty and points to the next list.

# To remove a number change the next.

# To access a certain value in a linked list you'll need to loop through each array,
# since the value proceeding it is the only one that know what value is next.
