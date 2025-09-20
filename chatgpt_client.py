"""
ChatGPT API連携クライアント
"""
import openai
from typing import List, Dict, Optional
from config import Config

class ChatGPTClient:
    """ChatGPT APIクライアントクラス"""
    
    def __init__(self):
        """初期化"""
        Config.validate_config()
        self.client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
        self.model = Config.OPENAI_MODEL
        self.max_tokens = Config.OPENAI_MAX_TOKENS
        self.temperature = Config.OPENAI_TEMPERATURE
    
    def chat(self, message: str, system_prompt: Optional[str] = None) -> str:
        """
        シンプルなチャット機能
        
        Args:
            message (str): ユーザーのメッセージ
            system_prompt (str, optional): システムプロンプト
            
        Returns:
            str: ChatGPTからの応答
        """
        messages = []
        
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        
        messages.append({"role": "user", "content": message})
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"エラーが発生しました: {str(e)}"
    
    def chat_with_history(self, messages: List[Dict[str, str]]) -> str:
        """
        会話履歴を含むチャット機能
        
        Args:
            messages (List[Dict[str, str]]): 会話履歴
                例: [{"role": "user", "content": "こんにちは"}, {"role": "assistant", "content": "こんにちは！"}]
            
        Returns:
            str: ChatGPTからの応答
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"エラーが発生しました: {str(e)}"
    
    def generate_text(self, prompt: str, max_tokens: Optional[int] = None) -> str:
        """
        テキスト生成機能
        
        Args:
            prompt (str): プロンプト
            max_tokens (int, optional): 最大トークン数
            
        Returns:
            str: 生成されたテキスト
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens or self.max_tokens,
                temperature=self.temperature
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"エラーが発生しました: {str(e)}"
    
    def translate_text(self, text: str, target_language: str = "Japanese") -> str:
        """
        テキスト翻訳機能
        
        Args:
            text (str): 翻訳するテキスト
            target_language (str): 翻訳先言語
            
        Returns:
            str: 翻訳されたテキスト
        """
        prompt = f"以下のテキストを{target_language}に翻訳してください:\n\n{text}"
        return self.generate_text(prompt)
    
    def summarize_text(self, text: str, max_length: int = 200) -> str:
        """
        テキスト要約機能
        
        Args:
            text (str): 要約するテキスト
            max_length (int): 最大文字数
            
        Returns:
            str: 要約されたテキスト
        """
        prompt = f"以下のテキストを{max_length}文字以内で要約してください:\n\n{text}"
        return self.generate_text(prompt)
