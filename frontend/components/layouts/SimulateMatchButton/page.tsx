import React from 'react';
import axios from 'axios';

const SimulateMatchButton: React.FC = () => {
  // シミュレートするためのデータ
  const requestData = {
    my_team_id: 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', // 実際のUUIDを入れてください
    opponent_team_id: 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', // 実際のUUIDを入れてください
    strategy: 'aggressive' // 戦術の種類
  };

  // ボタンをクリックしたときにPOSTリクエストを送信
  const handleSimulateMatch = async () => {
    try {
      const response = await axios.post('http://localhost:8000/match/simulate_match/', requestData, {
        headers: {
          'Content-Type': 'application/json',
        }
      });

      // サーバーからのレスポンス
      console.log('レスポンス:', response.data);
    } catch (error) {
      console.error('エラーが発生しました:', error);
    }
  };

  return (
    <div>
      <button onClick={handleSimulateMatch}>Simulate</button>
    </div>
  );
};

export default SimulateMatchButton;
