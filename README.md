# dify-plugins

#### 介绍
[dify插件介绍](https://docs.dify.ai/zh-hans/plugins/introduction)

[dify插件开发脚手架](https://github.com/langgenius/dify-plugin-daemon/releases)

```bash
# 安装
wget https://github.com/langgenius/dify-plugin-daemon/releases/download/${version}/dify-plugin-linux-amd64
sudo mv dify-plugin-linux-amd64 /usr/bin/dify
chmod +x /usr/bin/dify

dify --help
dify version

# 初始化
dify plugin init

# 打包
dify plugin package ./plugin-dir
```
