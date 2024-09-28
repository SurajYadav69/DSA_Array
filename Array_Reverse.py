#Array Reverse 

a = [2,4,67,89,0,1,100,99]

'''#build in method 

a.reverse()
print("reverse array:", a)

'''

#without build in method
reverse = []
for i in range (len(a)-1,-1,-1):   #(start, end, step)
    reverse.append(a[i])
print(reverse)