# ChatGPT API連携プロジェクト

このプロジェクトは、Pythonを使用してOpenAIのChatGPT APIと連携するためのクライアントライブラリです。

## 機能

- 基本的なチャット機能
- システムプロンプト付きチャット
- 会話履歴を保持したチャット
- テキスト生成
- 翻訳機能
- テキスト要約機能

## セットアップ

### 1. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 2. 環境変数の設定

`.env`ファイルを作成し、以下の内容を設定してください：

```env
# OpenAI API設定
OPENAI_API_KEY=your_openai_api_key_here

# モデル設定（オプション）
OPENAI_MODEL=gpt-3.5-turbo
OPENAI_MAX_TOKENS=1000
OPENAI_TEMPERATURE=0.7
```

**重要**: `your_openai_api_key_here`を実際のOpenAI APIキーに置き換えてください。

### 3. APIキーの取得

1. [OpenAI Platform](https://platform.openai.com/)にアクセス
2. アカウントを作成またはログイン
3. API Keysセクションで新しいAPIキーを生成
4. 生成されたAPIキーを`.env`ファイルに設定

## 使用方法

### 基本的な使用例

```python
from chatgpt_client import ChatGPTClient

# クライアントを初期化
client = ChatGPTClient()

# 基本的なチャット
response = client.chat("こんにちは！")
print(response)

# システムプロンプト付きチャット
response = client.chat(
    "Pythonについて教えてください。", 
    system_prompt="あなたは親切なプログラミング講師です。"
)
print(response)
```

### 会話履歴付きチャット

```python
messages = [
    {"role": "user", "content": "Pythonのリストについて教えてください。"},
    {"role": "assistant", "content": "Pythonのリストは複数の値を順序付きで格納するデータ構造です。"},
    {"role": "user", "content": "辞書との違いは何ですか？"}
]

response = client.chat_with_history(messages)
print(response)
```

### 翻訳機能

```python
# 英語を日本語に翻訳
response = client.translate_text("Hello, how are you?", "Japanese")
print(response)
```

### 要約機能

```python
long_text = "ここに長いテキストを入力..."
summary = client.summarize_text(long_text, max_length=200)
print(summary)
```

## サンプル実行

サンプルコードを実行するには：

```bash
python example_usage.py
```

対話型チャットを開始するには、サンプル実行後にプロンプトに従ってください。

## ファイル構成

```
.
├── chatgpt_client.py      # メインのクライアントクラス
├── config.py             # 設定管理
├── example_usage.py      # 使用例とサンプルコード
├── requirements.txt      # 依存関係
├── README.md            # このファイル
└── .env                 # 環境変数（要作成）
```

## エラー対処

### APIキーエラー
- `.env`ファイルに正しいAPIキーが設定されているか確認
- APIキーに権限があるか確認

### 依存関係エラー
- `pip install -r requirements.txt`を実行して依存関係をインストール

### ネットワークエラー
- インターネット接続を確認
- ファイアウォール設定を確認

## 注意事項

- APIキーは秘密情報です。`.env`ファイルをGitにコミットしないでください
- OpenAI APIの利用には料金が発生します。使用量に注意してください
- レート制限があるため、大量のリクエストを短時間で送信しないでください

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。
