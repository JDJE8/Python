def histogram(list):
    for i in range(len(list)):
        print(list[i] * "*")

l=[]
for i in range(3):
    num=int(input("Enter three number : "))
    l.append(num)

histogram(l)
