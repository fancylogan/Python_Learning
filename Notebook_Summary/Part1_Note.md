# Anaconda 

## 安装Anaconda
	配置环境变量
	设置源国内源
		conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
		conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
		conda config --set show_channel_urls yes

		测试 conda install 
	
### 可能有的问题：
		安装找不到源
			.condarc以点开头，一般表示 conda 应用程序的配置文件，在用户的家目录（windows：C:\\users\\username\\，linux：/home/username/）。
			但对于.condarc配置文件，是一种可选的（optional）运行期配置文件，其默认情况下是不存在的，但当用户第一次运行 conda config命令时，
			将会在用户的家目录创建该文件。
		解决方法：

		conda config –append channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
		conda config –append channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
		conda config --set show_channel_urls yes

## PS：常用conda命令

	conda install AppName==Version （eg. Django==2.2.1）
	conda remove appname
	conda list 查看安装的包
	


    cl = 查看conda evn list
    cc + NAME = 新建conda虚拟环境
        （conda create --prefix=D:\python36\py36 python=3.6）（新建虚拟环境到指定位置）
    cr + NAME = 删除conda环境
    coa + NAME = 激活指定虚拟环境（进）
    cod    = 退出 指定虚拟环境（退）




    打开VScode  
        code .

# Jupyter
## 运行：jupyter  notebook

更改根目录：
	jupyter notebook --generate-config
	运行生成的文件
	
	更改下面这个目录c''
		c.notebookapp.notebook_dir：u'D:\\123\\123'


	Jupyter 新建项目
