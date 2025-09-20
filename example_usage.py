"""
ChatGPT API連携の使用例
"""
from chatgpt_client import ChatGPTClient

def main():
    """メイン関数"""
    # ChatGPTクライアントを初期化
    client = ChatGPTClient()
    
    print("=== ChatGPT API連携テスト ===\n")
    
    # 1. 基本的なチャット
    print("1. 基本的なチャット:")
    response = client.chat("こんにちは！Pythonについて教えてください。")
    print(f"応答: {response}\n")
    
    # 2. システムプロンプト付きチャット
    print("2. システムプロンプト付きチャット:")
    system_prompt = "あなたは親切なプログラミング講師です。"
    response = client.chat("for文の使い方を教えてください。", system_prompt)
    print(f"応答: {response}\n")
    
    # 3. 会話履歴付きチャット
    print("3. 会話履歴付きチャット:")
    messages = [
        {"role": "user", "content": "Pythonのリストについて教えてください。"},
        {"role": "assistant", "content": "Pythonのリストは複数の値を順序付きで格納するデータ構造です。"},
        {"role": "user", "content": "辞書との違いは何ですか？"}
    ]
    response = client.chat_with_history(messages)
    print(f"応答: {response}\n")
    
    # 4. テキスト生成
    print("4. テキスト生成:")
    response = client.generate_text("人工知能の将来について100文字以内で説明してください。")
    print(f"応答: {response}\n")
    
    # 5. 翻訳機能
    print("5. 翻訳機能:")
    response = client.translate_text("Hello, how are you today?", "Japanese")
    print(f"応答: {response}\n")
    
    # 6. 要約機能
    print("6. 要約機能:")
    long_text = """
    人工知能（AI）は、コンピュータシステムが人間の知能を模倣する技術です。
    機械学習、深層学習、自然言語処理などの分野で急速に発展しています。
    AIは医療、金融、自動車、教育など様々な分野で活用されており、
    将来的には人間の生活を大きく変える可能性があります。
    しかし、倫理的な問題や雇用への影響など、慎重に検討すべき課題も存在します。
    """
    response = client.summarize_text(long_text, 100)
    print(f"応答: {response}\n")

def interactive_chat():
    """対話型チャット"""
    client = ChatGPTClient()
    
    print("=== 対話型チャット ===")
    print("終了するには 'exit' と入力してください。\n")
    
    messages = []
    
    while True:
        user_input = input("あなた: ")
        
        if user_input.lower() == 'exit':
            print("チャットを終了します。")
            break
        
        messages.append({"role": "user", "content": user_input})
        
        response = client.chat_with_history(messages)
        print(f"ChatGPT: {response}\n")
        
        messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    try:
        main()
        
        # 対話型チャットを実行するかどうか確認
        choice = input("\n対話型チャットを開始しますか？ (y/n): ")
        if choice.lower() == 'y':
            interactive_chat()
            
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        print("APIキーが正しく設定されているか確認してください。")
