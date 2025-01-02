import keyword

a = 10
print(type(a))
print(id(a))
a = "vrushali"
print(type(a))
print(id(a))

l = [10,20,30]
print(l)
l.append(40)
 
print(l)

t = (10 , 20 , 30,"vrush")
 
print(t)


s ={10,20,10,30,40,"vrush"}
print(s)
s.add(50)
s.remove(40)
f = frozenset(s)
 
print(s)
print(keyword.kwlist)
print(len(keyword.kwlist))

