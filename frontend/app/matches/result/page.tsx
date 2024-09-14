import Link from 'next/link';
import styles from '../result/Result.module.css';
import { Header } from '@/components/layouts/Header/page';

const ResultsPage = () => {
  // 仮のデータを定義（バックエンド接続前）
  const matchResults = [
    {
      id: 1,
      date: '2024-09-01',
      opponent: 'チームA',
      score: '3-1',
      details: '前半1-0、後半で2点追加し、チームAに圧勝。',
    },
    {
      id: 2,
      date: '2024-09-08',
      opponent: 'チームB',
      score: '2-2',
      details: '後半、チームBに同点弾を許し、引き分けに終わる。',
    },
    {
      id: 3,
      date: '2024-09-15',
      opponent: 'チームC',
      score: '0-1',
      details: '終盤に失点し、惜しくも敗北。',
    },
  ];

  return (
    <div className={styles.container}>
      <Header />

      <main className={styles.main}>
        <ul className={styles.resultList}>
          {matchResults.map((match) => (
            <li key={match.id} className={styles.resultItem}>
              <h2>{match.date} vs {match.opponent}</h2>
              <p><strong>スコア: </strong>{match.score}</p>
              <p>{match.details}</p>
            </li>
          ))}
        </ul>
      </main>
    </div>
  );
};

export default ResultsPage;
