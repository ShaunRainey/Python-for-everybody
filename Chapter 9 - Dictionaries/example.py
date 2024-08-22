counts = dict()
print('Enter a line of text:')
line = input('')
words = line.split()
print('Words:', words) 
print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print(counts)
print (f'Most common word "{max(counts)}" appears {counts[max(counts)]} times')
