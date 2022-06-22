
n1 = 1
n2 = 2
n3 = n1 + n2
sum = 0

while n3 <= 4000000:
    n3 = n1+n2
    if n3 >= 4000000:
        break
    if n3%2==0:
        sum = sum+n3
    n1 = n2
    n2 = n3
print("ans: ",sum+2 )
        


    

         


