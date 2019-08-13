"""


"""

print("进制转换".center(28,"="))
print('1. 二进制到十进制')
print('2. 十进制到二进制')
print('3. 十六进制到十进制')
print('4. 十进制到十六进制')
a='1. 二进制到十进制'
# b='2. 十进制到二进制'
# c='3. 十六进制到十进制'
# d='4. 十进制到十六进制'
choice = input('大胆说出你的选择：')
if choice == "1":
    num = input('你的选择是 '+a+'，'+'告诉我你要换算的数字：')
    weishu = len(num)
    ten = 0
    i = 1 
    for i in range(weishu):
       ten = ten + 2**i * int(num[-i])
    print (ten)
    
        

# if choice == "2":
#     num = input('你的选择是 '+b +'，'+'告诉我你要换算的数字：')
# if choice == "3":
#     num = input('你的选择是 '+c +'，'+'告诉我你要换算的数字：')
# if choice == "4":
#     num = input('你的选择是 '+d +'，'+'告诉我你要换算的数字：')
# else:
#     print("你输入的啥啊")




