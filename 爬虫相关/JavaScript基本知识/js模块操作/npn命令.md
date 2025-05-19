# 介绍

npm相当于python的pip命令，都是下载第三方库的命令，只不过下载的文件会到当前文件夹下

# 临时使用国内源安装包

```shell
npm install <package-name> --registry=https://registry.npmmirror.com
```

# 全局切换为国内镜像源(切换全局镜像源)

阿里巴巴以前提供过 npm 镜像（https://registry.npm.taobao.org），但目前该地址已停止维护，并重定向到 npmmirror.com（由淘宝团队维护，等同于原淘宝源）。

```shell
# 淘宝源
npm config set registry https://registry.npmmirror.com
```

# 查看当前使用的源

```shell
npm config get registry
```

# 恢复默认官方源

```shell
npm config set registry https://registry.npmjs.org
```

# 下载模块

和python类似,crypto-js替换为你的模块名

下载的模块尽量放在项目目录下面，这样不管是js单独运行还是python调用执行都不会导致模块无法读取，也方便维护

```shell
npm install crypto-js
```