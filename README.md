#VSCleaner
##用途

脚本小工具，用于删除 Microsoft Visual Studio 产生的中间文件(夹)。比如 Debug 目录,obj,ilk 文件等。
  
##用法
* 安装 [Python2.7](http://www.python.org)
* 假设在 D:\VC_PROJECT 目录下放着本地 Visual Studio 的所有工程。那么执行
```Bash
>python clean.pyc d:\vc_project
```
    所有工程的所有中间文件全部清除。
* 清除某个工程
```Bash
>python clean.pyc d:\vc_project\project1
```

##其他

之前用的 bat 批处理。修改为 Python 是为了方便维护。一些时日后，bat 的语法真的不记得了。
较好的用法是：

* 把 clean.py 放到 d:\bin ，同时把 d:\bin 加到环境变量里。
* 在 d:\bin 下创建 clean.bat 内容如下
```Bash
@ECHO OFF
python d:\bin\clean.pyc %*
```
* 在d:\vc_project\project1中打开命令行，执行
```Bash
>clean
```
  则 project1 中间文件清除干净了。
    
##自定义
  对于不同的 VC 版本，需要删除的中间文件会略有不同，或者需要删除其他(如 eclipse)环境的中间文件，可通过 clean.py 中的全局变量来进行配置。
Enjoy!