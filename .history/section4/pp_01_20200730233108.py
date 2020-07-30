s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s[0])

s[0] = 'X'
print(s[2:5])

s[2:5] = ['C', 'D', 'E']
print(s)

s[2:5] = []
print(s)

s[:] = []
print(s)

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n.append(100)

n.insert(0, 200)
print(n)

n.pop()
print(n)

n.pop(0)
print(n)

del n[0]
print(n)

m = [1, 2, 3, 4, 5]
m.remove(2)
m.remove(2)
m.remove(2)

print(m)