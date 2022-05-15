# Question 1

# take input from the user

str_1 = input( 'Please enter the country name followed by several resturant bills (separated by commas) : ' )

list_1 = str_1.split(', ')
list_2 = []
total_tip = 0

# set loop conditions to calculate tip if country is Bangladesh

if list_1[0].lower() == 'bangladesh':
    for i in list_1[1:]:
        bill = int(i)
        if 50 <= bill <= 300:
            tip = bill * (15/100)
        else:
            tip = 0
        list_2.append( bill + tip )
        total_tip += tip

# set loop conditions to calculate tip if country is not Bangladesh

else:
    for i in list_1[1:]:
        bill = int(i)
        if 50 <= bill <= 300:
            tip = bill * (20/100)
        else:
            tip = 0
        list_2.append( bill + tip )
        total_tip += tip

# print the total expense list and the total tip

print(list_2)
print('Total tip:', total_tip)

# end

#------------------------------------------------------------------------------------------------------------------------------------------

# Question 2

# take a given dictionary

dict1 = {1: ("Leo", "Kim", "Joe", "Brad"), 2:(12, 15, 10, 14), 3: ("Joey", "Tim", "Jen", "Jack"), 4:(19, 13, 17, 11)}

name_list = []
value_list = []
dict2 = {}

# set loop conditions to add names and values to different lists

for i in dict1:
    if i%2 != 0:
        for j in dict1[i]:
            name_list.append(j)
    else :
        for j in dict1[i]:
            value_list.append(j)

# sort the name list with respect to total asci values 

for i in range(len(name_list)-1):
        for j in range (len(name_list)-1-i):
            k1 = 0
            k2 = 0
            for k in name_list[j]:
                k1 += ord(k)
            for k in name_list[j+1]:
                k2 += ord(k)
            if k1 < k2:
                name_list[j], name_list[j+1] = name_list[j+1], name_list[j]

# sort the value list

value_list.sort()

# set loop conditions to add all values to dictionary 

for i in range(len(name_list)):
    asci_value = 0
    for j in name_list[i]:
        asci_value += ord(j)
    dict2[name_list[i]] = asci_value + value_list[i]

# print the final dictionary

print(dict2)

# end

#------------------------------------------------------------------------------------------------------------------------------------------

# Question 3

# define function to calculate final quiz marks

def calc_mark(marks_string):
    list_1 = marks_string.split(',')
    
    # set loop conditions to add all quiz marks in a list

    list_2 = []
    for i in list_1:
        list_2.append(int(i.strip()))

    print('Given marks:',list_2)
    
    # sort the marks list in descending order
    
    list_2.sort(reverse=True)

    # calculate final marks when 3 or less quizes are given

    if len(list_2) <= 3:
        total = 0
        for i in list_2[:-1]:
            total += i
        average = total / ( len(list_2) - 1 )
    
    # calculate final marks when more than 3 quizes are given

    else:
        total = 0
        for i in list_2[0:-2]:
            total += i
        average = total / ( len(list_2) - 2 )

    return average


# take input from the user

str_1 = input('Please enter the quiz marks in a string separated by a comma & multiple spaces : ')

# call function and print the final marks

print( calc_mark(str_1) )

# end
