import zipfile
import string
import itertools
myzipfile = 'zipsecretfile.zip'
def uncompress(zipfilename,password):
    try:
        zfile = zipfile.ZipFile(zipfilename)
        zfile.extractall('./',pwd=password.encode('utf-8'))
        return True
    except:
        return False

chars = string.ascii_lowercase+string.digits
print('正在解压......')
for c in itertools.permutations(chars,4):
    password = ''.join(c)
    res = uncompress(myzipfile,password)
    if res:
        print('解压成功',password)
        break