"use client";
import { Header } from '@/components/layouts/Header/page';
import CharacterComment from '@/components/layouts/CharacterComment/page'; // キャラクターコメントをインポート
import SimulateMatchButton from '@/components/layouts/SimulateMatchButton/page'; // シミュレートボタンをインポート
import styles from '../matches/Matches.module.css';

const Tactics = () => {
  return (
    <div>
      <Header />
      <div className={styles.container}>
        <h1 className={styles.title}>Tactics</h1>
        <p>ここでは戦術設定を行います。チームの戦術を選んでください。</p>
        
        <ul className={styles.unrow}>
          <li className={styles.row}>Short Counter</li>
          <li className={styles.row}>Side Attack</li>
          <li className={styles.row}>Posession</li>
          <li className={styles.row}>Long Counter</li>
        </ul>

        {/* キャラクターコメントを追加 */}
        <CharacterComment  />

        {/* 試合シミュレーションボタンを追加 */}
        <SimulateMatchButton />
      </div>
    </div>
  );
};

export default Tactics;
