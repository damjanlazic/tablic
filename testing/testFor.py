
combination=[1,2,3,4,5]
izvadi=3
index=0
for value in combination:
    if value == izvadi:
        combination.pop(index)
    index+=1
print("combination:", combination)
