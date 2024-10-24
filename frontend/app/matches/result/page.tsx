"use client"; // 追加: クライアントコンポーネントを示す
import { useEffect, useState } from 'react';
import { useSearchParams } from 'next/navigation'; // useSearchParamsをインポート
import styles from '../result/Result.module.css'; // CSSモジュールをインポート
import { Header } from '@/components/layouts/Header/page';

const ResultsPage = () => {
  const searchParams = useSearchParams(); // クエリパラメータを取得
  const [result, setResult] = useState<any>(null); // スコアを格納するためのステート

  useEffect(() => {
    const matchResult = searchParams.get('matchResult'); // クエリからmatchResultを取得

    if (matchResult) {
      // 受け取ったJSONをパースしてstateに保存
      setResult(JSON.parse(matchResult));
    }
  }, [searchParams]); // searchParamsを依存配列に追加

  // 結果がまだない場合のローディング表示
  if (!result) {
    return <div className={styles.loading}>Loading...</div>;
  }

  return (
    <div className={styles.container}>
      <Header />
      <main className={styles.main}>
        <h2>試合結果</h2>
        <div className={styles.resultItem}>
          <p><strong>私のチームスコア: </strong>{result.my_team_score}</p>
          <p><strong>相手チームスコア: </strong>{result.opponent_team_score}</p>
        </div>
      </main>
    </div>
  );
};

export default ResultsPage;
