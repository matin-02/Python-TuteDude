# filter(function, sequence)

seq = [1, 2, 3, 4, 5]
fo = filter(lambda x: True if x % 2 != 0 else False, seq)
print(list(fo))

mo = list(map(lambda x: True if x % 2 != 0 else False, seq))
print(mo)
