# 一个安装的示例UI界面。

---

## 请注意
**这只是**一个UI界面，**不是**安装程序。

如果想要当成框架，那么把我在ready_installer.py的注释包围的代码删除，能使无用功删除。


## 许可证！
这个项目使用MIT许可证。
已经放到LICENSE文件中。


## 依赖
下载python（请下载python3！）

这个项目不需要任何第三方的依赖。
只需要python3的tkinter库。
如果是纯正的Linux自带的python3但是没有tkinter库，那么请安装tkinter！

## 命令如下(大部分Linux发行版)
```commandline
# 根据你的 Linux 发行版选择对应的命令（Python 3）
# 1. Debian/Ubuntu
sudo apt update && sudo apt install python3-tk

# 2. Red Hat/CentOS/Fedora
# Fedora/RHEL 8+/CentOS 8+:
sudo dnf install python3-tkinter
# CentOS 7/RHEL 7:
sudo yum install python3-tkinter

# 3. Arch Linux/Manjaro
sudo pacman -S tk python

# 4. openSUSE
sudo zypper install python3-tk

# 5. Alpine Linux
sudo apk add tk python3 py3-tkinter

# 验证安装（通用）
python3 -c "import tkinter; print('Tkinter版本:', tkinter.TkVersion)"

```

好的，接下来，运行main.py文件即可。

good luck！
