# take a given list

list_1 = [10, 4, 23, 49, 36]

# define function to transform a list of integer values using normalization

def normalize( number_list ) :
    mxmm = number_list[0]
    mnmm = number_list[0]
    for i in number_list :
        if i > mxmm :
            mxmm = i
        elif i < mnmm :
            mnmm = i
    for i in range(len(number_list)) :
        number_list[i] = (number_list[i] - mnmm) / (mxmm - mnmm)
    return number_list


# call the function

print(normalize( list_1 ))

# end
