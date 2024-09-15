import styles from '../results/Results.module.css';

const Matches = () => {
  const matches = [
    { id: 1, date: '2024/09/01', opponent: 'チームA', result: '2-1 勝利' },
    { id: 2, date: '2024/09/07', opponent: 'チームB', result: '1-3 敗北' },
  ];

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>試合</h1>
      <ul className={styles.unrow}>
        {matches.map((match) => (
          <li className={styles.row} key={match.id}>
            {match.date} - {match.opponent} - {match.result}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Matches;
