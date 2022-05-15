# Question 1

# take input from user

num_1 = int(input( 'Please enter a number : '))
cntr = 0
total = 0
while total + cntr + 1 <= num_1 :
    cntr += 1
    total += cntr

for i in range(1,cntr+1) :
    print('#' * i)

rmn_brk = num_1 - total

print( 'Remaining bricks:', rmn_brk )

# end

#------------------------------------------------------------------------------------------------------------------------------------------

# Question 2

# take input from user 

list_1 = input(' Please enter a string where multiple numbers separated by commas : ')
list_1 = [int(x) for x in list_1.split(', ')]

list_1.sort()
print( 'Sorted list:', list_1 )

list_2 = []

for i in range(len(list_1)) :
    if i == 0 :
        if list_1[i+1] - list_1[i] <= 20 :
            list_2.append(list_1[i])
        else :
            list_2.append(list_1[i+1])
    elif list_1[i] - list_1[i-1] <= 20 :
        list_2.append(list_1[i])

print( 'Criteria pass:', list_2 )

total = 0

for i in list_2 :
    total += i

avg = total / len(list_2)

print( 'Average:', avg )

# end
