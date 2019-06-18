dat={"name":"Anandhu","number":"10"} #dict
lis=["Anandhu","10","c"] #list
li=[12,23,4,5,66,23]
#if statement with nested if
if "Anandhu" in lis:
    if lis[1]=="10":
        if lis[2]=="c":
            print("Anandhu10")
else:
    print("No name")
sum=0

#for loop
for x in li:
    sum=sum+x

print(sum)
avg=sum/len(li)

#while loop with break and continue and else clause
a=10;b=20
while a<29:
    a=a+1
    b=b+0.5
    if a!=b:
        continue
    if a==b:
        print("a is b at",a)
        break
else:
    print("not possible")