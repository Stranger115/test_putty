## 自动化测试putty V0.9.0 windows版

`环境准备`

> Python3.7 32bit
>
> windows10

`单元测试`

```shell
# 生成requirements.txt
pip freeze > requirements.txt
# 安装requirement.txt
pip install -r requirements.txt
cd test_putty
set PYTHONPATH=%CD%\src  # windows 
pytest -s ./tst
```

`自动化测试`

```shell
# windows 测试
cd  test_putty
pip requirment.txt
set PYTHONPATH=%CD%\src
pybot pybot puttyv0.7.0test.robot
```




