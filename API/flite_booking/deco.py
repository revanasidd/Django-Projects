# d1={'name':'shubh','age':27,'phone':767423834}
# print(d1.fromkeys('name'))
# for i in d1.fromkeys('name'):
#     print(i)
l1=[1,2,3]
l2=['a','b','c']

for i in l1:
    d1=dict.fromkeys(l2,i)
    l1.remove(i)
    break
print(d1)