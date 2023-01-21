import random
l=[12,10,34,78,"Ali","Mohammed",[100,200,[1000,2000,[10000,20000,30000],3000],300],5]
print(len(l))
print(l)
if 105 in l:
    print ("YES!")
else:
    print("No")
print (l[-2][-2][-2][-2])
print (l[-2][-2][-2])
print (l[-2][-2])
print (l[-2])
for item in l:
    print(item)
for i in range(len(l)):
    print(l[i])
print(l[4:5])
print(l[1:5]*5)
print(l)
ll=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15,15,15,15,15]
print(max(ll))
print(min(ll))
print(sum(ll))
print(sum(ll)/len(ll))
ll.append(16)
print(ll)
ll.reverse()
print(ll)
print(ll,ll)
ll.reverse()
ll.remove(15)
print(ll)
for i in range(len(l)):
    if 15 in ll:
        ll.remove(15)
        ll.append(16+i)
        print(ll)
        print("ll.count(15) :", ll.count(15))
if (ll.count(15)) <= 0:
    ll.insert(14, 15)
                
print(ll)