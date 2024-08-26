from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from sklearn.datasets import load_iris

# FastAPIのインスタンスを作成
app = FastAPI()

# 学習済みのモデルをロード
model = joblib.load("iris_model.pkl")

# リクエストボディのデータ構造を定義
class PredictionRequest(BaseModel):
    features: list

# 予測エンドポイントを作成
@app.post("/predict/")
async def predict(request: PredictionRequest):
    # リクエストの特徴量をNumPy配列に変換
    features = np.array(request.features).reshape(1, -1)
    
    # モデルを使って予測を実行
    prediction = model.predict(features)
    predicted_class = int(prediction[0])
    
    # Irisデータセットのターゲット名を取得
    class_name = load_iris().target_names[predicted_class]
    
    # 予測結果を返す
    return {"prediction": predicted_class, "class_name": class_name}

# サーバーの起動（ローカル実行時）
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
