"use client"; // 先頭に追加
import { Header } from '@/components/layouts/Header/page';
import CharacterComment from '@/components/layouts/CharacterComment/page'; // キャラクターコメントをインポート
import SimulateMatchButton from '@/components/layouts/SimulateMatchButton/page'; // シミュレートボタンをインポート
import styles from '../matches/Matches.module.css';
import axios from 'axios';
import { useRouter } from 'next/navigation'; // 正しいインポートを使用

const Tactics: React.FC = () => {
  const router = useRouter(); // Next.jsのルーターを取得

  // ボタンをクリックしたときにPOSTリクエストを送信
  const handleSimulateMatch = async (strategy: string) => {
    const requestData = {
      my_team_id: '5654d8f5-dbff-4012-954f-f6b451be612b', // 実際のUUIDを入れてください
      opponent_team_id: 'c079eed5-f33e-4acf-bb1e-6854666120e5', // 実際のUUIDを入れてください
      strategy: strategy // 引数として受け取った戦術
    };

    try {
      const response = await axios.post('http://localhost:8000/match/simulate_match/', requestData, {
        headers: {
          'Content-Type': 'application/json',
        }
      });

      // 試合結果を取得し、リダイレクトとデータを渡す
      const matchResult = response.data;

      // クエリ文字列を作成
      const queryString = new URLSearchParams({
        matchResult: JSON.stringify(matchResult)
      }).toString();

      // 結果ページにリダイレクト
      router.push(`/matches/result?${queryString}`);

    } catch (error) {
      console.error('エラーが発生しました:', error);
    }
  };
  
  return (
    <div>
      <Header />
      <div className={styles.container}>
        <h1 className={styles.title}>Tactics</h1>
        <p>ここでは戦術設定を行います。チームの戦術を選んでください。</p>
        
        <ul className={styles.unrow}>
          <SimulateMatchButton onClick={handleSimulateMatch} strategy='short_counter'>Short Counter</SimulateMatchButton>
          <SimulateMatchButton onClick={handleSimulateMatch} strategy='side_attack'>Side Attack</SimulateMatchButton>
          <SimulateMatchButton onClick={handleSimulateMatch} strategy='posession'>Posession</SimulateMatchButton>
          <SimulateMatchButton onClick={handleSimulateMatch} strategy='long_counter'>Long Counter</SimulateMatchButton>
        </ul>

        {/* キャラクターコメントを追加 */}
        <CharacterComment  />

      </div>
    </div>
  );
};

export default Tactics;
