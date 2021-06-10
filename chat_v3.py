
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ')
    time = s[0][:5]   #代表s[0]那個字串的前五個字  清單分割法 ,在python中清單的切割可以使用在字串上
    name = s[0][5:]   #取第五個字到最後
    print(name)