print ('\nGood day!\nI suggest you format the following text:\n')

with open("text.txt", encoding='utf-8') as text:
    text = text.read() 
print (text)
    
text_split = text.split()
total_amount_elem = len(list(text_split))

while True:
    input_num = input ('\nPlease enter the length of the string below.\n(Number of characters, not less than 36!!!:\n')
    if not input_num.isdigit():
        print ('Wrong input!!!\nRepeat please!')
        continue
    input_num = int(input_num)
    if input_num < 36:
        print ('Wrong input!!!\nRepeat please!')
        False
    else:
        break

ind, ind_word, word_num_index,  total_ind_finish = 0, 0, 0, 0

while total_amount_elem > total_ind_finish:
    n = input_num
                                                  
    if ind == 0:
        ind = ind
    else:
        ind = ind_word
    sum_simb = 0
    word_count = 0
    while sum_simb < n:
        n = n - 1
        sum_simb = sum_simb + (len(list(text_split[ind]))) 
        ind = ind + 1
        word_count +=1
    
    count_space = input_num - sum_simb - word_count - 1                     #       check. if there are more spaces (-1) than words

    if count_space < 0:
        word_count = word_count - 1 
        i = 0
        sum_simb = 0
                                                                            #       word counter
        while i < word_count:
            sum_simb = sum_simb + (len(list(text_split[ind_word])))
            ind_word  += 1
            i += 1

    count_space = input_num - sum_simb                                      #      total spaces
    
                                                                            #      forming a string
    if word_num_index == 0:
        word_num_index = word_num_index
    else:
        word_num_index = ind_word - i
        
    text_list =[]                         
    wni = 0
    while wni < word_count:
        text_list.append(text_split[word_num_index])
        word_num_index +=1
        wni +=1

    count_space_i = 0
    current_word = 0
    while count_space_i != count_space:
        if current_word == len(text_list) - 1:
            current_word = 0
            continue

        text_list[current_word] = text_list[current_word] + ' '
        current_word += 1
        count_space_i += 1

    text_list.append('\n')
    text_join = "".join(text_list)
    index = sum_simb + word_count
    
    with open ('finish.txt', 'a', encoding='utf-8') as funish_txt:
        funish_txt.writelines(text_join)
        funish_txt = """ "finish.txt" """

    total_ind_finish = ind_word + word_count

print (f'Dear user!\nYour new file is located in the root folder, under the name{funish_txt}\n')






    


