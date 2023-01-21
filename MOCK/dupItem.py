a = [10,20,30,20,10,50,60,40,80,50,40]
dup_items = []
uniq_items = []
for x in a:
    if x not in uniq_items:
        uniq_items.append(x)
    else:
        dup_items.append(x)
print(uniq_items)
print(dup_items)