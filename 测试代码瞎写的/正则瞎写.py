before = '我是一个网站更新，我变更了abcd，哈哈哈' #input("变更前内容：")
after = '我是一个网站更新，我变更了1234，哈哈哈' #input("变更后内容：")

# 其他测试文本

print('变更前: ',before)
print('变更后：',after)
zhengze = ""
c=0

#思路：从字符串的第一个字符开始比对，如果相同记下该字符串，如果不同，把不同的部分用正则过滤，最终输出带正则的字符串
for i in range(0,len(before)):  
   if before[i] != after[i]:    #不同的时候继续循环，直到匹配到相同
      c = 1
   if before[i] == after[i]:    # 如果该位置的字符串一样，并且c不为0，证明指针已经经过了变更的部分，输出一个正则符号，继续输出
      if c != 0:
         zhengze = zhengze +'(.*?)'+before[i]
         c = 0
      else:                      # if c == 0 ,证明指针还没发现变更的部分，继续执行输出
         zhengze = zhengze + before[i]
         c = 0
print ('用正则：',zhengze)










