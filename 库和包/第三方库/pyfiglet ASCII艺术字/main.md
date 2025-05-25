# pyfiglet - Python ASCII 艺术字生成库

`pyfiglet` 是一个将普通文本转换为 ASCII 艺术字的 Python 库，支持 300+ 种字体风格。

## 安装

```bash
pip install pyfiglet
```

## 基础用法

### 1. 快速生成艺术字

```python
import pyfiglet

text = pyfiglet.figlet_format("Hello World!")
print(text)
```

### 2. 指定字体

```python
result = pyfiglet.figlet_format("Python", font="slant")
print(result)
```

输出：

```
  _____       __    __             
 / ___/__  __/ /_  / /  ___  _____ 
 \__ \/ / / / __ \/ /  / _ \/ ___/ 
 ___/ / /_/ / / / / /__/  __/ /    
/____/\__, /_/ /_/____/\___/_/     
     /____/                        
```

### 3. 列出所有可用字体

```python
print(pyfiglet.FigletFont.getFonts())  # 输出 300+ 字体列表
```

## 进阶功能

### 控制宽度和对齐

```python
text = pyfiglet.figlet_format(
    "Center",
    font="block",
    width=80,  # 控制总宽度
    justify="center"  # 对齐方式(left/center/right)
)
```

### 从文件加载自定义字体

```python
custom_font = pyfiglet.Figlet(font='path/to/myfont.flf')
print(custom_font.renderText('Custom'))
```

### 彩色输出（需搭配 `termcolor`）

```bash
pip install termcolor
```

```python
from termcolor import colored

art = pyfiglet.figlet_format("Color!", font="starwars")
print(colored(art, "red", "on_yellow"))
```

## 命令行直接使用

```bash
# 查看帮助
python -m pyfiglet -h

# 快速生成
python -m pyfiglet -f slant "CLI Mode"

# 列出所有字体
python -m pyfiglet -l
```

## 常见应用场景

1. 命令行工具欢迎界面
2. 日志警告醒目提示
3. 生成复古风格文字海报
4. 游戏中的标题文字
5. 黑客风终端效果

## 资源

- [PyPI 主页](https://pypi.org/project/pyfiglet/)
- [GitHub 源码](https://github.com/pwaller/pyfiglet)
- [在线字体预览](https://patorjk.com/software/taag/)

## 示例字体效果

| 字体名       | 效果预览                        |
|-----------|-----------------------------|
| `block`   | ██████  ██  ██████  ██   ██ |
| `script`  | 𝒮𝒸𝓇𝒾�𝓉  𝓈𝓉𝓎𝓁𝑒     |
| `bubble`  | Ⓑⓤⓑⓑⓛⓔ ⓕⓞⓝⓣ                 |
| `digital` | █▀▀ █── █▀▀ █─█ █▀▀ █▀▀ █── |

> 提示：运行 `python -m pyfiglet -l` 查看完整字体列表