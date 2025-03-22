# x => for creating a file 
# w => for writing in the file as well as creating
# r => for reading the file (file should already exist in your system)
# a => for appending

# Yes -Y and No-N
# mode | create-file | readable | writable | cursor position
# x    |     Y       |    N     |     Y    |       0
# w    |     Y       |    N     |     Y    |       0
# r    |     N       |    Y     |     N    |       0
# a    |     Y       |    N     |     Y    |  last contant/element/object position     
# x+   |     Y       |    Y     |     N    |  
# r+   |     N       |    Y     |     Y    |  
# w+   |     Y       |    Y     |     Y    |  
# a+   |     Y       |    Y     |     Y    |  

# f=open('n2.py','x')
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.closed)

# f=open('p2.py','w')
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.closed)

# f=open('p2.py','r')
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.closed)

# f=open('d2.py','a')
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.closed)

# f=open('n2.py','x+')
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.closed)

# f=open('p2.py','w+')
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.closed)

# f=open('p2.py','r+')
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.closed)

# f=open('d2.py','a+')
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.closed)

# operation
    # write()
    # read()
# write()
    # write()->single_line
    #writeline()->multiple line
# read()
    # read()
    # read(n)->n is the character
    # readline()
    # readlines()

# always use append mode as the cursor postion is the last element
# f=open('d1.py','a')
# f.write('hello,this is file_handing class')
# f.close()

# f=open('d1.py','a')
# data=['Hi\n','Hello\n','Welcome\n']
# f.writelines(data)
# f.close()

# f=open('d1.py','r')
# data=f.read(5)
# print(data)
# data=f.read(5)
# print(data)
# data=f.read()
# print(data)
# data=f.read()
# print(data)

f=open('d1.py','r')
data=f.readline()
print(data)
data=f.readlines()
print(data)