import { Header } from '@/components/layouts/Header/page';
import CharacterComment from '@/components/layouts/CharacterComment/page'; // キャラクターコメントをインポート
import styles from '../matches/Matches.module.css';

const Tactics = () => {
  return (
    <div>
      <Header />
      <div className={styles.container}>
        <h1 className={styles.title}>Tactics</h1>
        <p>ここでは戦術設定を行います。チームの戦術を選んでください。</p>
        
        <ul className={styles.unrow}>
          <li className={styles.row}>カウンターアタック</li>
          <li className={styles.row}>サイド攻撃</li>
          <li className={styles.row}>ポゼッション</li>
        </ul>

        {/* キャラクターコメントを追加 */}
        <CharacterComment comment="野球と違ってたくさんの戦術があるよ" />
      </div>
    </div>
  );
};

export default Tactics;
