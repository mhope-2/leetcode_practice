def check_unique(l):
    hashmap = {}
    
    for i in l:
        hashmap[i] = 1 + hashmap.get(i, 0)
    for i in l:
        if hashmap[i] > 1:
            return False
    return True

print(check_unique([1,2,3,4,4]))
