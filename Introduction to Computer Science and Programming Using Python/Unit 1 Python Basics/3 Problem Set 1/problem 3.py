s = 'jnmltbaip'
longest = ''
temp = ''


for x in s:
    if not temp or x >= temp[-1]:
        temp += x
    else:
        if len(temp) > len(longest):
            longest = temp
        temp = x
        

if len(temp) > len(longest):
    longest = temp

print("Longest substring in alphabetical order is: ", longest)
        

                    

