
source_file = open('a.txt','r', encoding='utf-8')
dst_file = open('b.txt','a', encoding='utf-8')

while True:
    #文件如果太大，防止程序奔溃，可以分批读取和写入，直到读取不到内容。
    data = source_file.read(1024)
    if len(data) == 0:
        break
    dst_file.write(data)

source_file.close()
dst_file.close()
