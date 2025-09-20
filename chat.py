"""
対話型ChatGPTチャット
"""
from chatgpt_client import ChatGPTClient

def main():
    """メイン関数"""
    try:
        # ChatGPTクライアントを初期化
        client = ChatGPTClient()
        
        print("🤖 ChatGPT対話型チャット")
        print("=" * 50)
        print("終了するには 'exit' または 'quit' と入力してください。")
        print("履歴をクリアするには 'clear' と入力してください。")
        print("-" * 50)
        
        messages = []
        
        while True:
            # ユーザー入力
            user_input = input("\n👤 あなた: ").strip()
            
            # 終了コマンド
            if user_input.lower() in ['exit', 'quit', '終了']:
                print("\n👋 チャットを終了します。お疲れさまでした！")
                break
            
            # 履歴クリアコマンド
            if user_input.lower() in ['clear', 'クリア']:
                messages = []
                print("\n🧹 会話履歴をクリアしました。")
                continue
            
            # 空の入力はスキップ
            if not user_input:
                continue
            
            # メッセージに追加
            messages.append({"role": "user", "content": user_input})
            
            # ChatGPTからの応答を取得
            print("\n🤖 ChatGPT: ", end="", flush=True)
            try:
                response = client.chat_with_history(messages)
                print(response)
                
                # 応答を履歴に追加
                messages.append({"role": "assistant", "content": response})
                
            except Exception as e:
                print(f"エラーが発生しました: {e}")
                # エラーが発生した場合、最後のメッセージを削除
                if messages:
                    messages.pop()
    
    except Exception as e:
        print(f"初期化エラー: {e}")
        print("\n🔧 解決方法:")
        print("1. .envファイルに正しいAPIキーが設定されているか確認してください")
        print("2. python test_config.py で設定を確認してください")
        print("3. OpenAI APIキーが有効か確認してください")

if __name__ == "__main__":
    main()
