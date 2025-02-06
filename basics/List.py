# # # # # # # # # # # # # # # # # what is a list
# # # # # # # # # # # # # # # # # hetrogeneous and homogeneous
# # # # # # # # # # # # # # # # # ordered collection
# # # # # # # # # # # # # # # # # index supporting
# # # # # # # # # # # # # # # # #  slicing supported
# # # # # # # # # # # # # # # # # mutable
# # # # # # # # # # # # # # # # # represents in [] with comma(,) separated elements
# # # # # # # # # # # # # # # # max()
# # # # # # # # # # # # # # # # min()
# # # # # # # # # # # # # # # # id()
# # # # # # # # # # # # # # # # sum()
# # # # # # # # # # # # # # # # type()
# # # # # # # # # # # # # # # # len()
# # # # # # # # # # # # # # # # list()
# # # # # # # # # # # # # # # # l=[10,20,30,40,'Anushka']
# # # # # # # # # # # # # # # # print(type(l))
# # # # # # # # # # # # # # l=['Anushka','Sudarshan','Joshi']
# # # # # # # # # # # # # # print(l)
# # # # # # # # # # # # # # print(max(l))
# # # # # # # # # # # # # # print(min(l))
# # # # # # # # # # # # # # print(id(l))
# # # # # # # # # # # # # # l1=[10,20,30,10.5]
# # # # # # # # # # # # # # print(l1)
# # # # # # # # # # # # # # print(sum(l1))
# # # # # # # # # # # # # # print(type(l1))
# # # # # # # # # # # # # # print(len(l1))
# # # # # # # # # # # # # # print(list(l1))
# # # # # # # # # # # # # # x=list()
# # # # # # # # # # # # # # print(x)
# # # # # # # # # # # # # # print(type(x))
# # # # # # # # # # creation commands
# # # # # # # # # # # # # l=[10,20,'Anushka',30,40]
# # # # # # # # # # # # # # append()
# # # # # # # # # # # # # l.append(105)
# # # # # # # # # # # # # print(l)
# # # # # # # # # # # # l.append([10,20,30])
# # # # # # # # # # # # print(l)
# # # # # # # # # # # # extend()
# # # # # # # # # # # l.extend([10,20,30])
# # # # # # # # # # # print(l)
# # # # # # # # # # # insert()
# # # # # # # # # # l.insert(0,'Divyansh')
# # # # # # # # # # # l.insert('Divyansh',0) #errors 
# # # # # # # # # # print(l)
# # # # # # # # # # # pop()
# # # # # # # # # l=[120,50,'Anushka',100]
# # # # # # # # # print(l.pop())
# # # # # # # # # print(l)
# # # # # # # # # remove()
# # # # # # # # l=[120,50,'Anushka',100]
# # # # # # # # l.remove(100)
# # # # # # # # print(l)
# # # # # # # l=[10,20,30,40,10]
# # # # # # # l.remove(10,2)
# # # # # # # print(l) #error
# # # # # # # clear()
# # # # # # l=[120,50,'Anushka',100]
# # # # # # l.clear()
# # # # # # print(l)
# # # # # # print(id(l))
# # # # # # del()
# # # # # l=[120,50,'Anushka',100]
# # # # # del l
# # # # # print(l) #error
# # # # # copy()
# # # # l=[120,50,'Anushka',100]
# # # # l1=l.copy()
# # # # print(l1)
# # # # print(id(l),id(l1))
# # # # count()
# # # l=[120,50,'Anushka',100,120,120]
# # # print(l.count(120))
# # # index()
# # l=[120,50,'Anushka',100,120,120]
# # print(l.index(120,1))#,1 is for the next one i.e the second one
# # reverse()
# l=[120,50,'Anushka',100,120,120]
# l.reverse()
# print(l)
# # sort()
l=[120,50,100,120,120]
# l.sort()
l.sort(reverse=True)
print(l)