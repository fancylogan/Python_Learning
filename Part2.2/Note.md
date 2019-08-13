# index: try  base64 pyperclip re class

# base64算法
    import base64

    s =input()
    ss = base64.b64encode(s.encode("utf-8"))
    ss.decode("utf-8")

## eg：
    def encode():
        upwd = input("Input your password: ")
        return base64.b64encode(upwd.encode("utf-8"))#.decode("utf-8")

    def decode():
        cpwd = input("Input your password: ")
        return (base64.b64decode(cpwd.encode("utf-8"))).decode("utf-8")

# pyperclip
    pip install pyperclip

    import pyperclip  #做复制粘贴操作
    pyperclip.copy

# RE
## 两个对象
    - re对象：regex  正则表达式对象
    - match对象： match对象

## 模块内容：
    - 函数：
    re.complie(pattern, flags=0)   --regex         编译生成一个正则表达式对象 regex.???
    re.search(pattern, srting, flags=0)    --match     找到第一个匹配的位置 match.????
    re.match(pattern, srting, flags=0)    --match      从头匹配，第0位开始（能匹配到就匹配到）
    re.fullmatch(pattern, srting, flags=0)    --match
    re.split(pattern, srting, maxsplit=0, flags=0)   --list
    re.findall(pattern, srting, flags=0)    --list
    re.finditer(pattern, srting, flags=0)   --iterator
    re.sub(pattern, repl, srting, count=0, flags=0)    --str    替换的
    re.subn(pattern, repl, srting, count=0, flags=0)    --tuple
    re.escape(patten)             --characters
    re.purge()     清除
    
    - 常量：是flag的值？
    增强操作
    re.A/re.ASCII     让\w \W \b \B \d \D \s 和\S 仅执行ASCII匹配
    re.DEBUG        展示debug信息
    re.I/IGNORE             忽略大小写
    re.L/LOCALE        标识特殊字符集\w \W \b \B \s \S 依赖于当前环境
    re.M/MUTILINE        多行模式
    re.S/DOTALL        即为‘.’并且包括换行符在内的任意字符（‘.’不包括换行符）
    re.X/VERBOSE        为了增强可读性，忽略空格和‘#’后面的注释

# 两个对象
两个对象
    - re对象regex
    regex.search(string[, pos[, endpos]])
    regex.match(string[, pos[, endpos]])
    regex.fullmatch(string[, pos[, endpos]])
    regex.split(string, maxsplit=0)
    regex.findall(string[, pos[, endpos]])
    regex.finditer(string[, pos[, endpos]])
    regex.sub(repl, string,count=0)
    regex.subn(repl, string,count=0)
    regex.flags
    regex.groups
    regex.groupindex
    regex.pattern

    - match对象
    match.expand(template)
    match.group([group1, ...])
    match.group([group1, ...]) / [0],[1]...
    match.groups(default = None)
    match.groupdict(default = None)
    match.start([group])
    match.end([group])
    match.span([group])

# eg. ：
    1. import re  导入
    2. re.complie()  正则对象，#主要推荐哦
    regex = re,compile(pattern)
    result = regex.match(string)
    ==
    match = re.match(pattern, string)
    3. 使用regex查找一个字符串，返回被匹配的对象
    4. 调用匹配对象的group方法，返回实际匹配的文本
    [] 表示字符集
    | 或者，只匹配其中一个表达式

# 常用 
    ()     括号分组
    |      管道分组
    ?      取0次或1次
    re.X    换行，注释


### findall 
    - 有分组，返回元组列表
    - 无分组，返回字符串列表
### split 
    - 返回正则分割后的列表

    re.match 只从第一个开始取
    re.search 只匹配第一个
    
    eg:
    regex = re.compile("re")

    match = regex.match(“string")   

### 替换
    re_sub = re.compile(r"(3)sef(2)sdf(1)")
	re_sub.sub (r"\1 \2 \3",string)
	
	re_sub = re.compile(r'(?P<name1>,\d+)\.(?P<name2>\d+)')
	re_sub.sub (r'\g<name1>月\g<name2>日',text)

	re_sub = re.compile(r '\s+') #\s space
	re_sub.sub = ("",s) 
    
### 匹配中文：
	\u4e00-u9fa5



# Class

    class Name:
        def __init__(self, a1, a2 ,a3 ,a4):  #初始函数 ，第一个必须是self
            self._a1 = nnnnnnn  #内部变量，在本class里有效
            self.a2 = mmmm  
            self.__a3 = iiiiiiii        #两个下划线，私有变量，只在本def有效
        def function（）：   #普通函数


        @property   #放在def上面，


        @brand.setter #放在def上面
        def brand （self，brand):
            raise TypeError('字符串“0)