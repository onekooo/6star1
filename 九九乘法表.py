import time
for i in range(1,10):
    for j in range(1,i+1):
        # print(str(j)+'x'+str(i)+'='+str(i*j),end=' ' )
        print('{}x{}={:<2s}'.format(str(j),str(i),str(i*j)), end=' ')
        time.sleep(0.5)
    print()
    time.sleep(0.5)

# for i in range(0,5):
#     for j in range(0,5):
#         print('* ',end='')
#     print()
#
# for i in range(1,6):
#     print('*' * i, end='')
#     print()