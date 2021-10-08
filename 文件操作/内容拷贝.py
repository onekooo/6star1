
outputfile = open('当幸福来敲门.jpg','rb')
data = outputfile.read()

inputfile = open('b.jpg','wb')
inputfile.write(data[0:len(data)//2])

outputfile.close()
inputfile.close()