import { Header } from '@/components/layouts/Header/page';
import styles from '../results/Results.module.css';
import CharacterComment from '@/components/layouts/CharacterComment/page'; // キャラクターコメントをインポート

const Matches = () => {
  const matches = [
    { id: 1, date: '2024/09/01', opponent: 'チームA', result: '2-1 win' },
    { id: 2, date: '2024/09/07', opponent: 'チームB', result: '1-3 loss' },
  ];

  return (
    <div>
      <Header />
    <div className={styles.container}>
      <h1 className={styles.title}>Results</h1>
      <ul className={styles.unrow}>
        {matches.map((match) => (
          <li className={styles.row} key={match.id}>
            {match.date} - {match.opponent} - {match.result}
          </li>
        ))}
      </ul>

      {/* キャラクターコメントを追加 */}
      <CharacterComment comment="ポンポン点が決まらないから熱中して見れるね" />
    </div>
    </div>
  );
};

export default Matches;

