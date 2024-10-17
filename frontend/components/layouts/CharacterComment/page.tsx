"use client";
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import styles from './CharacterComment.module.css';

// 型定義 (以前作成したもの)
// TypeScript型定義

interface DifyChatRequest {
  inputs: Record<string, any>;  // 任意のキーと値を持つオブジェクト
  query: string;                // 質問内容
  response_mode?: string;        // 応答モード（オプション）
  user: string;                 // ユーザーID
}

type ResponseData = {
  status: string;  // "success" や "error" などのステータス
  answer:string
     // FastAPIで処理されたデータ
};
const CharacterComment: React.FC = () => {
  const [apiComment, setApiComment] = useState<string>(''); // APIのレスポンス用の状態を追加
  const [error, setError] = useState<string | null>(null); // エラーメッセージ用の状態を追加

  // データ (リクエストボディ用)
  const requestPayload: DifyChatRequest = {
    "inputs": {},
    "query": "ギラヴァンツ北九州",
    "response_mode": "blocking",
    "user": "9be0a4ae-9b70-4c18-909b-64a924779d3b"
  };

  // API を呼び出してコメントを取得する useEffect フック
  useEffect(() => {
    const fetchWeatherComment = async ()=> {
      try {
        const response = await axios.post<ResponseData>("http://localhost:8000/rag/generate", requestPayload, {
          headers: {
            "Content-Type": "application/json",
          }
        }); 
        console.log(response)
        // サーバーからのレスポンスを状態に保存
        const answer :string =JSON.stringify(response.data.answer)
        const formattedAnswer = answer
        .trim()                     // 先頭と末尾の空白を削除
        .replace(/"/g, '')           // " を削除
        .replace(/\n+$/, '');        // 最後の改行のみを削除
        
        setApiComment(formattedAnswer); // `result`キーにアクセスする必要があるか確認
        setError(null); // エラーがない場合はエラーメッセージをクリア
        console.log('レスポンス:', response.data);

      } catch (error: any) {
        if (error.response) {
          // サーバーがエラーを返した場合
          setError(`サーバーエラー: ${error.response.data.detail}`);
        } else if (error.request) {
          // リクエストが送信されたが応答がなかった場合
          setError('サーバーからの応答がありません');
        } else {
          // その他のエラー
          setError(`予期しないエラーが発生しました: ${error.message}`);
        }
        console.error('APIの呼び出し中にエラーが発生しました', error);
        setApiComment('APIエラーが発生しました'); // エラーメッセージをセット
      }
    };

    fetchWeatherComment(); // useEffect内でAPI呼び出し
  }, []); // 空の配列を渡すことで、コンポーネントの初回レンダリング時にのみ実行される
  return (
    <div className={styles.characterContainer}>
      <div className={styles.character}>
        <img src="/character.png" alt="キャラクター" />
      </div>
      <div className={styles.speechBubble}>
        <p>{apiComment}</p> {/* APIから取得したコメントを表示 */}
        {error && <p className={styles.error}>{error}</p>} {/* エラーメッセージを表示 */}
      </div>
    </div>
  );
};

export default CharacterComment;