def get_ranges(l):
    def conv(left, right, sep = ', '):
        '''возвращает интервал в виде текста, если границы совпадают - одно значение
        left, right: границы
        sep: разделитель, присоединяется в конце'''
        return '{}{}{}'.format(left, (right != left)*('-'+str(right)), sep)

    left_border = l[0]
    result_str = ''
    for i in range(len(l)-1):
        #если следующее значение в списке идет не по порядку, закрываем интервал
        if l[i+1] > l[i]+1:
            result_str += conv(left_border, l[i])
            left_border = l[i + 1]
    #закрываем интервал последним элементом списка, разделитель не нужен
    result_str += conv(left_border, l[len(l)-1], sep = '')
    return result_str

print(get_ranges([ 4, 4, 5, 6, 7, 9, 767]))

