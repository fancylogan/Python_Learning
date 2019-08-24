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

## 方法中的self是怎么回事

    - 实例本身
    - 放到第一个参数，区别于普通函数
    - 通用名为self 

    假如你有一个类成为a和这个类的一个实例b。当你调用这个对象的方法b.method(arg1, arg2) ——的时候，这会由python自动转为a.method(arg1, arg2) ——这就是self的原理

    class Computer:
    def play(self, game = ‘qq game’)
    print(‘play,’ game)

    pc1 = Computer()
    pc1.play()

    pc2 = Computer()
    # Computer.play(pc2, game = ‘wechat game’) 与下面那句说的一样
    pc2.play


## 7-4 特殊方法

    __init__: 把各种属性绑定到self
    __slots__: 会限制实例的动态属性，减少内存消耗，tuple类型
    __str__: 对象的说明文字
    __eq__: 比较对象是否相等

    classmethod 
    staticmethod

    class Computer:
    def __init__(self, name, mem, cpu)
    self._name = name
    self.men = men
    self.cpu = cpu
    pc1 = Computer(selina, 16G, 8)
    pc1.disk = ‘ssd’
    # 只有PC1有


    class Computer:
    __slots__ = (‘_name’, ‘mem’, ‘cpu’)

    不能加更多的比如pc2.disk = ‘ssd’就不能加在slots里

    class Computer:
    def __str__(self):
    return f ‘{self.name}:{self.men}-{self.cpu}’
    def __eq__(self, other):
    return self.cpu == other.cpu

    @classmethod  # 通过新的方法构造实例，区别于默认的__init__，类似其他语言重载
    def new_pc(cls, info):
    “从字符串直接产生新的实例”
    name, men, cpu = info.split(‘-’)
    return cls(name, mem, cpu)

    @staticmethod # 不需要生成类的实例，就可以实现的方法
    def calc(a, b, oper)
    if oper == +:
    return a + b





## 面向对象的三大特征
### 封装、继承、多态

    # 继承，在继承里补充或者修改一些方法 
    class Tesla(Car):     # 儿子类（父类） child(father/super)
    def __init__(self, brand = ‘Tesla’, price = 10000, wheels = ‘4’, power = ‘electric’):
    super().__init__(brand, price, wheels, power)
    def run(self, action):
    print(f ‘{self.brand} is running with {self.power}’)

    t = Tesla()
    t.price = 999
    t.price 

    如果t是子类的实例，那他也是父类的实例

    # 多态 先调用自己的方法，如果自己没有，再调父类。




    7-6 元编程
    我是谁？
    我从哪儿来？
    我到哪儿去？

    #运行时动态创建类和函数
    # metaclass -> class -> object
    # __new__

    class Game:
    pass

    Game.__class__
    #class的类型是type


    Type是一个metaclass
    通过type创建一个新的metaclass

    class SelinaMeta(type):
    pass
    class Selina(metaclass = SelinaMeta):
    pass 

    Selina 是 SelinaMeta 的一个实例

    Selina.__new__   # 创建并且返回一个新的object



    class SelinaMeta(type):
    def __new__(cls, name, bases, my_dict):      #classmethod 不需要在上面写@那个，											# 比较特殊
    print (f ‘{name} 使用__new__创建’)
    Selina_class = super().__new__(cls, name, bases, my_dict)   # 返回了新的类，
    # super()的含义是子类去调用父类的方法
    return Selina_class 

    class Selina(metaclass = SelinaMeta): 
    pass
