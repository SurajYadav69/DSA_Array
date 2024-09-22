print('You have a list of your favourite marvel super heros.')

heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

print('Length of the list:', len(heros))

# Add Black Panther at the end of the list
heros.append('black panther')
print('Add black panther at the end of this list:', heros)

# Remove Black Panther and insert it after Hulk
heros.remove('black panther')  # Corrected: Removed extra space
heros.insert(3, 'black panther')
print('You realize that you need to add black panther after hulk:', heros)

# Replace Thor and Hulk with Doctor Strange
heros[1:3] = ['doctor strange']  # Fixed: Assignment outside of print
print('Now you don\'t like thor and hulk because they get angry easily:', heros)

# Sort the heros list in alphabetical order
heros.sort()  # Corrected: Added parentheses to call sort
print('Sort the heros list in alphabetical order:', heros)
