l = [1,2,1,2,3]
y = []
n = 0
print(len(l))
print(l)
for i in l:
  if i in y:
    pass
  elif l.count(i) > 1:
      r = l.count(i) - 1
      y.append(i)
      n += r
print(len(l) - n)
