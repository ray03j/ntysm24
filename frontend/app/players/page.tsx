import styles from '../players/Players.module.css';

const Players = () => {
  const players = [
    { id: 1, name: '田中 太郎', position: 'FW' },
    { id: 2, name: '鈴木 次郎', position: 'MF' },
    { id: 3, name: '佐藤 三郎', position: 'DF' },
  ];

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>選手一覧</h1>
      <ul className={styles.unrow}>
        {players.map((player) => (
          <li className={styles.row} key={player.id}>
            {player.name} - {player.position}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Players;