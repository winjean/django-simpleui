- 建立虚拟环境
pip install virtualenv
pip install virtualenvwrapper-win

mkvirtualenv -p <指定python安装位置> <虚拟环境目录位置>

查看虚拟环境列表
workon

进入虚拟环境
workon env_winjean

退出虚拟环境
deactivate

1、安装Django:
pip install django==3.2 

查看版本号： 
python -m django --version

查看当前安装的django版本库： 
pip show django

删除django： 
python uninstall django

2、安装Django REST Framework： 
pip install djangorestframework

3、安装Django REST Framework JWT: 
pip install djangorestframework-jwt

- 新建项目  
django-admin startproject my_site

- 创建应用  
python manage.py startapp app_name

- 运行服务  
python manage.py runserver 0.0.0.0:8000

- 生成数据库语句  
python manage.py makemigrations <model>

- 同步数据库  
python manage.py migrate


- 创建admin用户
python manage.py createsuperuser

- 在项目根目录中，打开终端执行以下命令  
- 生成 requirements.txt 文件  
pip3 freeze > requirements.txt  

- 安装依赖文件  
pip3 install -r requriements.txt 

- 安装 pipreqs  
pip3 install pipreqs

- 生成依赖文件，其中前面的路径为项目根目录路径  
- Windows 一定要在后面加上编码，否则报 UnicodeDecodeError: 'gbk' codec can't decode byte 0xae in position 81: illegal multibyte sequence  
- Linux 尚未测试  
pipreqs E:\Python_virtualenvs\for_django\Projects\FortressMachine --encoding=utf-8  

- 安装  
pip3 install -r E:\Python_virtualenvs\for_django\Projects\FortressMachine\requriements.txt  



安装xadminpip
https://www.jianshu.com/p/3a3afda82f72
pip install https://github.com/sshwsfc/xadmin/tarball/master

安装simpleui
pip install django-simpleui
