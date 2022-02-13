Windows 命令行：[3. Using Python on Windows — Python 3.9.10 documentation](https://docs.python.org/3.9/using/windows.html?highlight=run library module script)

python.exe -m pip install --upgrade pip

python.exe -m pip install py

python -m site

在pip install时手工指定：
一般情况
pip install -i http://mirrors.aliyun.com/pypi/simple/ pillow  --trusted-host mirrors.aliyun.com

增加extra-index-url，及trusted-host：
pip install pillow -i http://mirrors.aliyun.com/pypi/simple/ --extra-index-url https://pypi.python.org/simple --trusted-host mirrors.aliyun.com

```
 python -m pip install requests  -i http://mirrors.aliyun.com/pypi/simple/ --extra-index-url https://pypi.python.org/simple --trusted-host mirrors.aliyun.com
```
