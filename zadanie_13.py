from ipaddress import *
#1
# в net первое значение это ip адрес, второе значение из цикла это макси, ноль в net просто нужно ставить
for mask in range(33):
    net = ip_network(f'93.138.70.47/{mask}', 0)
    print(net)

#2 найти количество ip адресов с четным количеством 1
# первое значение в s это ip сети, второе это маска сети
counter = 0
net = ip_network('192.168.32.160/255.255.255.240')
for ip in net:
    s = f'{ip:b}'
    if s.count('1') % 2 == 0:
        counter +=1
print(counter)

#3 найти количество ip адресов с равным количеством 1 и 0
# первое значение в s это ip сети, второе это маска сети  
counter = 0
net = ip_network('192.168.248.176/255.255.255.240')
for ip in net:
    s = f'{ip:b}'
    if s.count('1') == s.count('0'):
        counter += 1
print(counter)

#4 найти количество ip адресов с большим количеством 1 чем 0
counter = 0
net = ip_network('192.168.248.176/255.255.255.240')
for ip in net:
    s = f'{ip:b}'
    if s.count('1') > s.count('0'):
        counter += 1
print(counter)