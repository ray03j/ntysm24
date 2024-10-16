from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import requests
import os
from schemas.rag import DifyChatRequest
import json

# .envファイルを読み込む
load_dotenv()

# 環境変数からAPI情報を取得
DIFY_API_URL = os.getenv("DIFY_API_URL")
API_KEY = os.getenv("API_KEY")

router = APIRouter()

@router.post("/generate")
async def chat_with_dify(request: DifyChatRequest):
    try:
        print("get request body")
        # リクエストのボディを取得
        
        payload = request.dict()

        print("post Dify request")
        print(type(DIFY_API_URL))
        print(DIFY_API_URL)
        print(type(API_KEY))
        print(payload)
        print(DIFY_API_URL+'/chat-messages')
        print( f"Bearer {API_KEY}")
        # DifyにPOSTリクエストを送信

        # requestsをつかったリクエスト
        res = requests.post(DIFY_API_URL+'/chat-messages', json=payload, headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        })

        print(res)

            # ステータスコードの確認
        if res.status_code != 200:
            print(res.text)
            raise HTTPException(status_code=res.status_code, detail="Error in Dify API request")

        if res.status_code == 200:
            print(res.text)
            return json.loads(res.text)

        # レスポンスの内容を確認する
        res_text = await res.text()  # JSONでなくても確認できるようにtext()を使う
        print("Dify API Response:", res_text)  # デバッグ用にレスポンス内容をログに出力

        # レスポンスが空でないか確認する
        if not res_text:
            raise HTTPException(status_code=500, detail="Received empty response from Dify API")

        # レスポンスがJSONとしてパース可能か確認
        try:
            res_json = res.json()  # `response.json`を参照することで問題が発生する可能性あり
            if callable(res_json):  # もし`response.json()`が関数なら
                return res_json()  # 実際にJSONを返す
            else:
                raise ValueError("response.json is not callable")
        except ValueError:
            raise HTTPException(status_code=500, detail="Received invalid JSON from Dify API")


    except Exception as err:
        # その他のエラー
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {err}")