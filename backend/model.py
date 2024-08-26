from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import joblib

# Irisデータセットをロード
data = load_iris()
X, y = data.data, data.target

# RandomForestClassifierでモデルをトレーニング
model = RandomForestClassifier()
model.fit(X, y)

# 学習済みモデルを保存
joblib.dump(model, 'iris_model.pkl')
