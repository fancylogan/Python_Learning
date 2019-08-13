# index: 字符串控制、列表的控制
# 0、查找字符串 string.find("a")

# 1、输出字符串时把结尾从回车变成空格：
	end=“ ”
# 2、字符串以指定格式输出
	eg:
	‘{}x{}={}’.format(1,2,3)
	‘{a},{b},{c}'.format (a=1,b=2,c=3)

# 3	 \n:回车 
	 \t:tab

# 4  直接输出字符串变量
	f-string	
	f'{a},{b}'

# 5、字符串的修改
	string = goodlan#goodlan.com.cn
	string.replace(#,@)

# 6、字符串的字母大写 Upper
# 7、字符串字母小写 lower
# 8、首字母大写  captlizse
# 9、email.zfill(30)
	'00000000000000goodlan.com.cn'
# 10,email.ljust(20,*)
	字符串左对齐，其余补齐
   email.rjust (20,*)
	字符串右对齐，其余补齐
   email.center(20，*)
	居中

    字符串查找：string.count("8")
    判断是否大小写 string.isupper()
            string.islower()
    字符串长度 len(string)


    =========================我是华丽的分隔线============================
    a='123'
    print (a.zfill(30))
    print (a.ljust(30,"*"))
    print (a.rjust(30,"*"))
    print (a.center(30,"*"))
    print (a.replace('1','5'))

    000000000000000000000000000123
    123***************************
    ***************************123
    *************123**************
    523
    =========================我是华丽的分隔线============================



# 11、字符串支持切片
	string[i] 看第i个字母是啥

	string [:4]输出前4个字母


# 12、分片
	string = hanyanlong@yeah.net
	string.split("@")
	string = ["hanyanlong","yeah.net"]

# index和find的区别
	找不到index报错
	find找不到返回-1

============================================
# list.append()
    str.join(list) 把列表里的值以字符串形式输出

