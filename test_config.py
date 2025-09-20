"""
設定確認用のテストスクリプト
"""
from config import Config
import os

def test_config():
    """設定をテストする"""
    print("=== 設定確認 ===")
    
    # .envファイルの存在確認
    env_path = ".env"
    if os.path.exists(env_path):
        print(f"✓ .envファイルが見つかりました: {env_path}")
    else:
        print(f"✗ .envファイルが見つかりません: {env_path}")
        return False
    
    # 環境変数の確認
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        if api_key == 'your_openai_api_key_here':
            print("✗ APIキーがデフォルト値のままです。実際のAPIキーに変更してください。")
            return False
        else:
            print(f"✓ APIキーが設定されています: {api_key[:10]}...")
    else:
        print("✗ OPENAI_API_KEYが設定されていません")
        return False
    
    # 設定の検証
    try:
        Config.validate_config()
        print("✓ 設定が正しく読み込まれています")
        print(f"  モデル: {Config.OPENAI_MODEL}")
        print(f"  最大トークン数: {Config.OPENAI_MAX_TOKENS}")
        print(f"  温度: {Config.OPENAI_TEMPERATURE}")
        return True
    except ValueError as e:
        print(f"✗ 設定エラー: {e}")
        return False

if __name__ == "__main__":
    success = test_config()
    if success:
        print("\n🎉 設定が完了しました！example_usage.pyを実行できます。")
    else:
        print("\n❌ 設定に問題があります。上記のエラーを修正してください。")
