from pydantic import BaseModel
from typing import Dict, Optional

class DifyChatRequest(BaseModel):
    inputs: Dict = {}  # `inputs`は辞書型として定義（空辞書がデフォルト）
    query: str  # 質問文 (例: "アインクラッドとは？")
    response_mode: Optional[str] = "blocking"  # レスポンスモード、デフォルトは "blocking"
    user: str  # ユーザーID