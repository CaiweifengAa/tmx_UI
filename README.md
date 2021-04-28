# ui_test: to test thingsmartix website.
# 环境搭建：
* 1、Python：3.5+，pip要升级到最新版本:
```bash
python -m pip install -U pip
```
* 2、git安装,cmd进入工作目录，将代码克隆到本地：git clone https://github.com/thingsmatrix/ui_test
* 3、在pycharm中，打开克隆到本地的项目
* 4、在pycharm中设置项目的解释器，file -> settings -> project -> python inerpreter
* 5、打开pycharm的终端terminal，执行：pip install –r requirements.txt，在执行上述命令前，先确保pip是最新版本
* 6、设置pytest为默认运行器：file -> settings -> tools -> python integrated tools -> testing选择pytest，如果是unittest选择unittest，点击OK
* 7、在pycharm终端中，安装webdriver，seleniumbase install geckodriver，或单独下载webdriver，
并在系统环境变量中设置webdriver的路径，或拷贝到[虚拟环境]\Lib\site-packages\seleniumbase\drivers
* 8、cd到examples文件夹，执行：pytest test_login.py
* 9、通过run_all_case.py或者命令行执行pytest  test_login.py --html=reportdemo.html输出测试报告；

# 配置文件
* 1、config.ini，配置测试环境地址，邮件发送人，邮件内容，和其他默认参数等信息；
* 2、test_data.yml，存放测试数据；
* ###### 4、config.xml，配置登录用户等信息，在credentials.py文件中设置，然后导入该文件获取对应值；
* 3、项目根目录下的settings.py文件为配置数据库地址和其他默认参数，在pytest.ini中自定文件路径为根目录，
    则运行测试用例需要在根目录下的run.py中运行，否则无法读取到文件；若不需要配置数据库等默认参数，可以在
    pytest.ini中将--settings_file=settings.py注释掉，避免在代码中运行找不到文件的错误；

# 分支控制
* 1、master为主分支，develop为开发分支，平时在develop分支上提交新的代码，稳定后再合并到master分支；
* 2、在提交代码前，先pull下当前分支最新代码，避免提交时可能覆盖其他人的代码；
* 3、合并代码操作（PyCharm操作为例，将develop分支合并到master分支）：
    * VCS>>Git>>Branches>>Local Branches>>选择master>>Checkout
    * VCS>>Git>>Merge Changes>>Branches to merge>>选择develop>>点击Merge
* 4、非项目运行依赖文件，不需要提交到项目代码中，通过.gitignore来控制忽略，添加文件时指定到具体文件名，
    避免使用add . 命令，把非必要的文件提交到代码中；
* 5、若不小心提交的非依赖文件，在项目下，通过git命令行工具，执行：git rm -r --cached [无关文件] 命令来删除，
    然后操作git commit和git push。
    
# 元素定位
* 1、通过jQuery方法定位：
    * 需要要修改解释器下的Lib\site-packages\seleniumbase\fixtures\constants.py文件中的MIN_JS值，将原来的值注释掉，
    添加新的MIN_JS = ("https://cdn.staticfile.org/jquery/%s/jquery.min.js" % VER),
    或者是MIN_JS = ("http://apps.bdimg.com/libs/jquery/2.0.0/jquery.min.js")
