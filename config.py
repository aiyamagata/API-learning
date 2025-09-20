"""
ChatGPT API連携の設定ファイル
"""
import os
from dotenv import load_dotenv

# .envファイルを読み込み
load_dotenv()

class Config:
    """設定クラス"""
    
    # OpenAI API設定
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
    OPENAI_MAX_TOKENS = int(os.getenv('OPENAI_MAX_TOKENS', 1000))
    OPENAI_TEMPERATURE = float(os.getenv('OPENAI_TEMPERATURE', 0.7))
    
    @classmethod
    def validate_config(cls):
        """設定の検証"""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEYが設定されていません。.envファイルでAPIキーを設定してください。")
        
        return True
