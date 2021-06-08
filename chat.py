# 處理對話紀錄

def read_file(filename):
    lines =[]
    with open(filename, 'r', encoding='utf-8-sig') as f: #-sig 去除\ufeff
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue 
        if person:
            new.append(person + ': ' + line)
    return new

def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8-sig') as f: #-sig 去除\ufeff
        for line in lines:
            f.write(line + '\n')



def main():
    filename = 'input.txt'
    outfile = 'output.txt'
    lines = read_file(filename)
    #print(lines)
    lines = convert(lines)
    write_file(outfile, lines)
    print(lines)

main()
