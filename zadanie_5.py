#4
for c in range(1, 255):
    nums = ''
    bin_num = bin(c)[2:]
    while len(bin_num) < 8:
        bin_num = '0' + bin_num

    for i in bin_num:
        if i == '1':
            nums += '0'
        elif i == '0':
            nums += '1'
    new_num = int(nums, 2)
    result = new_num - c
    if result == 111:
        print(c)



#6
counter = 0
new_counter = 0
result = 0
ls = []
for c in range(1, 51):
    bin_num = bin(c)[2:]
    for i in bin_num:
        if i == '1':
            counter += 1
        else:
            continue
    if counter % 2 == 0:
        bin_num += '0'
    else:
        bin_num += '1'

    for i in bin_num:
        if i == '1':
            new_counter += 1
        else:
            continue
    if new_counter % 2 == 0:
        bin_num += '0'
    else:
        bin_num += '1'

    result = int(bin_num, 2)
    if result < 50:
        ls.append(result)
    counter = 0
    new_counter =0
print(max(ls))


#2
for i in range(1, 100000):
    num = i
    bin_num = bin(num)[2:]
    bin_num = bin_num[:-1]
    if num %2 == 0:
        bin_num += '01'
    else: bin_num +='10'
    result = int(bin_num, 2)
    if result == 2018:
        print(num)


#3
for i in range(1, 100000):
    num = i
    bin_num = bin(num)[2:]
    bin_num = bin_num[:-1]
    if num %2 == 0:
        bin_num += '01'
    else: bin_num +='10'
    result = int(bin_num, 2)
    if result == 2017:
        print(num)


#5
for i in range(1, 100):
    num = i
    bin_num = bin(i)[2:]
    if bin_num.count('1')>bin_num.count('0'):
        bin_num += '1'
    elif bin_num.count('0')>=bin_num.count('1'):
        bin_num += '0'
    result = int(bin_num,2)
    if result<100:
        print(result)