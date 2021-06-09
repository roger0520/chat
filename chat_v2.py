# 處理對話紀錄

def read_file(filename):
    lines =[]
    with open(filename, 'r', encoding='utf-8-sig') as f: #-sig 去除\ufeff
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    name = None
    allen_word_count = 0
    viki_word_count = 0
    allen_sticker_count = 0
    viki_sticker_count = 0
    allen_image_count =0
    viki_image_count =0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count +=1 
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)

    print('allen說了', allen_word_count,'個字')
    print( 'allen傳了', allen_sticker_count, '個貼圖')
    print( 'allen傳了', allen_image_count, '個圖片')
    print('viki說了', viki_word_count,'個字')
    print( 'viki傳了', viki_sticker_count, '個貼圖')
    print( 'viki傳了', viki_image_count, '個圖片')          


    #return new

def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8-sig') as f: #-sig 去除\ufeff
        for line in lines:
            f.write(line + '\n')



def main():
    filename = 'LINE-Viki.txt'
    outfile = 'output.txt'
    lines = read_file(filename)
    #print(lines)
    lines = convert(lines)
    #write_file(outfile, lines)
    #print(lines)

main()
