#Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

max = int(input("entre maximum number:-"))

odd_no = []

for i in range(1,max):
    if i % 2 == 1:
        odd_no.append(i)
        
print("odd number:", odd_no)         