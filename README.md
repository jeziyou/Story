# 📚 儿童故事集 | Children's Story Collection

一个双语儿童故事集Web应用，支持中英文切换，配有精美AI生成插图，可直接部署到Streamlit Cloud分享。

## ✨ 功能特性

- 🌐 **中英文双语切换** - 一键切换中文/英文版本
- 🎨 **AI生成插图** - 每页故事配有精美的文生图插图（离线版本，图片已预生成保存）
- 📖 **翻页阅读体验** - 直观的上一页/下一页导航
- 🔤 **字体大小调节** - 可调节阅读字体大小
- 🚀 **一键部署** - 直接部署到Streamlit Cloud，无需额外配置

## 📁 项目结构

```
├── app.py                 # Streamlit主应用
├── requirements.txt       # Python依赖
├── .streamlit/
│   └── config.toml        # Streamlit主题配置
├── images/                # 预生成的故事插图（离线版本）
│   ├── little_star_cover.png
│   ├── little_star_page1.png
│   ├── ...
└── README.md
```

## 🚀 本地运行

```bash
pip install -r requirements.txt
streamlit run app.py
```

然后在浏览器打开 http://localhost:8501

## ☁️ 部署到 Streamlit Cloud

1. 将代码推送到GitHub仓库
2. 访问 [share.streamlit.io](https://share.streamlit.io)
3. 连接你的GitHub仓库
4. 主文件选择 `app.py`
5. 点击 **Deploy!**

部署完成后即可获得公开链接分享给他人访问。

## 📖 当前故事

- **《小星星找朋友》** - 约7分钟阅读时长，温暖的友谊故事
