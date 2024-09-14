import styles from '../matches/Matches.module.css';

const Tactics = () => {
  return (
    <div className={styles.container}>
      <h1 className={styles.title}>戦術設定</h1>
      <p>ここでは戦術設定を行います。チームの戦術を選んでください。</p>
      <ul className={styles.unrow}>
        <li className={styles.row}>カウンターアタック</li>
        <li className={styles.row}>サイド攻撃</li>
        <li className={styles.row}>ポゼッション</li>
      </ul>
    </div>
  );
};

export default Tactics;