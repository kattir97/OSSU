s = 'azcbobobegghakl'

count = 0

for i, x in enumerate(s):
    if i + 3 <= len(s):
        if 'bob' in s[i: i + 3]:
            count += 1
    
    
print('Number of times bob occurs is: ', count)
