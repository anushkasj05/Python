# # # # collection of key value pairs
# # # # where 'key' must be unique
# # # # value may be duplicate
# # # # no indexing support
# # # # no slicing support
# # # # mutable in mature
# # # # represented in { } with comma(,) separated elements
# # # d={'Name':'Anushka',
# # #    'Age':20,
# # #    'qual':'BCA'}
# # # print(d)
# # # print(type(d))
# # # max()
# # # min()
# # # len()
# # # type()
# # # id()
# # # dict()
# # d={'Name':'Anushka','Age':20,'Qual':'BCA'}
# # print(max(d))
# # print(min(d))
# # print(len(d))
# # print(type(d))
# # print(id(d))
# # x=dict()
# # print(x)  # empty dictionary
# # print(type(x))
# # dictionary methods()
# # copy() 
# # clear()
# # keys()
# # values()
# # items()
# # get()
# # fromkeys()
# # updated()
# # setdefault()
# # pop()
# # popitem()
# d={'Name':'Anushka','Age':20,'Qual':'BCA'}
# d.copy()  # copy of dictionary
# print(d)
# d.clear()  # clear the dictionary
# print(d)
# d.keys()  # keys of dictionary
# print(d.keys())
# d.values()  # values of dictionary
# print(d.values())
# d.items()  # items of dictionary
# print(d.items())
# d.get('Name')  # get the value of key
# print(d.get('Name'))
# # d.pop('Age')  # pop the key and return value
# # print(d)
# # d.popitem()  # pop the last item
# # print(d.popitem())
# d.setdefault('Name','divyansh')  
# print(d.setdefault('Name','divyansh'))
# d.update({'Age':21,'Qual':'BCA'})  # update the dictionary
# print(d)
# d.fromkeys({'Name':'Divyansh','Age':20})
# print(d.fromkeys({'Name':'Divyansh','Age':20}))
s='Anushka'
x=dict.fromkeys(s,50)
print(x)