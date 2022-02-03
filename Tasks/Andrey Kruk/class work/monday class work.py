string = input()

l = string.split(' ')

d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
     'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
     'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20}

for i in range(len(l)):
    if l[i] in d.keys():
        l[i] = d[l[i]]

l = list(set(l))

l.sort()

l1 = []
l2 = []
n = 0
k = 1
while True:
    if (n + 2) <= len(l):
        l1.append(l[n] * l[n + 1])
    else:
        break
    if (k + 2) <= len(l):
        l2.append(l[k] + l[k + 1])
    else:
        break
    n += 2
    k += 2

sum = 0

for i in l:
    if i % 2 != 0:
        sum += i
