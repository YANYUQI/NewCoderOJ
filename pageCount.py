
# 暴力，超时
# def pageCount ():
#     n = input()
#     count = [ 0 for i in range(10)]
#     n = int(n)
#
#
#     for i in range(1,n+1):
#         curpage = i
#         while(curpage > 0):
#             curnum = curpage % 10
#             curpage = curpage // 10
#             count[curnum] += 1
#
#     for i in range(0, 9):
#         print(count[i], end = ' ')
#     print(count[9])
#
# pageCount()




def pageCount():
    n = input()
    n = int(n)
    count = [0 for i in range(10)]

    for i in range(0,10):
        page = n
        p = 0 #代表当前数字tmp右边还有几个数字
        t = 0 #统计出现次数
        while(page // (10**(p)) > 0):
            tmp = ( page % ( 10 ** (p+1)) ) // (10 ** p)
            left = page // ( 10 ** (p+1))
            right =  page % ( 10 ** (p))
            #print(left,tmp,right)

            if( i == 0 ):
                left -= 1

            if (i > tmp):
                t += left*(10**p)
            elif (i < tmp):
                t += (left+1)*(10**p)
            else:
                t += ( left*(10**p) + right + 1 )

            p += 1
        count[i] = t

    for i in range(0, 9):
         print(count[i], end = ' ')
    print(count[9])

pageCount()
