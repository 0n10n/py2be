## env设置

- https://docs.python.org/3/tutorial/venv.html

步骤：

```
$ python -m venv env
$ source env/bin/activate
# 退出虚拟环境：
$ source env/bin/deactivate
```

创建requirements.txt文件

```
$ pip3 freeze > requirements.txt
```

使用时

```
$ pip3 install -r requirements.txt
```

