# take input from user

str_1 = input( 'Please enter a string in the given format : ' )
list_1 = str_1[:-1].split(';')
dict_1= {}

# set loop conditions

for i in range(len(list_1)):
    temp_list = list_1[i].split(':')
    key = temp_list[0]
    value = [int(x) for x in temp_list[1].split(',')]
    dict_1[key] = sum(value) / len(value)

print(dict_1)

# end
