# # # # collection of unique elements
# # # # unordered collection
# # # # indexing not supported
# # # # slicing not supported
# # # # mutable in nature
# # # # represented in { } with comma(,)separated values
# # # # max()
# # # # min()
# # # # sum()
# # # # type()
# # # # id()
# # # # len()
# # # s={10,20,30,'Anushka','Divyansh','Argha',10,20}
# # # print (s)
# # # print(type(s))
# # s={10,20,10,30,60,40,50}
# # print(max(s))
# # print(min(s))
# # print(sum(s))
# # print(type(s))
# # print(id(s))
# # print(len(s))  # count of elements in set
# # methods
# # # copy()
# # # clear()
# # # add()
# # # update()
# # # remove()
# # # discard()
# # # pop()
# s={10,20,10,30,60,40,50}
# s.add(80)
# print(s)
# s.update([70,90])
# print(s)
# s.remove(10)
# print(s)
# s.discard(60)
# print(s)
# s.pop()
# print(s)
# x=s.copy()
# print(id(x),id(s))
# s.clear()
# print(s)  # empty set
A={2,4,6,8}
B={1,2,3,4}
print(A.union(B)) # first elements of B than different elements of A
print(A.intersection(B)) #Same elements of A and B
print(A.difference(B)) # different elements of B than are not present in A
print(A.symmetric_difference(B))  # than ddiffernt elememts in A and B