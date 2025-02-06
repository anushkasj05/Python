# # collection of unique elements
# # freeze any collection(list,set,tuple,string)
# # unordered collection
# # indexing not allowed
# # slicing not supported
# # immutable nature
# s='Anushka'
# fs=frozenset(s)
# print(fs)
# print(type(fs))
# copy()
# difference()
# intersection()
# union()
# issuperset()
# issubset()
# symmetric_difference()
# isdisjoin()
s={10,20,30,40}
x=frozenset(s)
l=[2,4,6,10,20]
y=frozenset(l)
print(x)
print(y)
print(x.union(y))
print(x.intersection(y))
print(x.difference(y))
print(x.symmetric_difference(y))
print(x.issubset(y))
print(x.issuperset(y))
print(x.isdisjoint(y))  #returns true if both sets are disjoint else false