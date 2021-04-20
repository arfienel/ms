def permutations(s):
    from itertools import product
    b = []
    for combos in product(s, repeat=len(s)):
         b.append(''.join(combos))
    for item in b:
        s2 = s
        for item2 in item:
            if item2 in s2:
                print(item,s2)
                item.replace(item2,'')
                s2.replace(item2,'')
            else:
                b.remove(item)
    return list(set(b))

d = permutations('abba')
print(d)
