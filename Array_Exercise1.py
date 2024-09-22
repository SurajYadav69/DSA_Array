''' Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,'''

array = [2200, 2350, 2600, 2130, 2190]

print('In Feb, how many dollars you spent extra compare to January?', array[1] - array[0])

print('Find out your total expense in first quarter (first three months) of the year', array[0]+array[1]+array[2])

print('Find out if you spent exactly 2000 dollars in any month', 2000 in array) #false

print('June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list', array.append(1980))
print(array)

array[3] -= 200
print('You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list', array)


