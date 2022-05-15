# start

word_1 = input( 'Please enter a string : ' )
word_2 = ''
vwls = 'aeiouAEIOU'

# set loop condition

for i in range (len(word_1)) :
    if word_1[i] in vwls:
        if i<(len(word_1)-2) and word_1[i+1] in vwls and word_1[i+2] in vwls :
                word_2 += '#'
        elif i<(len(word_1)-1) and word_1[i+1] in vwls and word_1[i-1] in vwls :
                word_2 += '#'
        elif word_1[i-2] in vwls and word_1[i-1] in vwls :
                word_2 += '#'
        else:
            word_2 += word_1[i]    
    else :
        word_2 += word_1[i]

print(word_2)

# end
