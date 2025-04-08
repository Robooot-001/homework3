# AI Chatbot with Gemini

這是一個使用 Google Gemini AI 模型的聊天機器人專案，提供網頁介面和命令列介面兩種使用方式。

## 功能特點

- 使用 Google Gemini AI 模型進行對話
- 提供網頁介面（Flask）和命令列介面（CLI）
- 支援 Vercel 部署

## 安裝需求

- Python 3.8+
- Flask
- google-generativeai
- python-dotenv

## 安裝步驟

1. 克隆專案：
```bash
git clone [your-repository-url]
cd [repository-name]
```

2. 安裝依賴套件：
```bash
pip install -r requirements.txt
```

## 使用方法

### 網頁介面
```bash
python api/app.py
```
然後在瀏覽器中訪問 `http://localhost:5000`

### 命令列介面
```bash
python cli.py
```

## 部署

專案已配置好 Vercel 部署，只需將專案推送到 GitHub 並連接到 Vercel 即可。

## 環境變數

- `GEMINI_API_KEY`: Google Gemini API 金鑰
- `GEMINI_MODEL`: 使用的 Gemini 模型名稱（預設：gemini-1.5-flash）

## 授權

MIT License 