"use client";
import { useState } from 'react';
import styles from '../players/Players.module.css';
import { Header } from '@/components/layouts/Header/page';
import CharacterComment from '@/components/layouts/CharacterComment/page'; // 追加

const TeamPage = () => {
  const [activeTab, setActiveTab] = useState('starting11');

  const starting11 = [
    { name: '佐藤栄松', position: 'GK', stats: 'Saves: 20' },
    { name: 'Player 2', position: 'DF', stats: 'Tackles: 30' },
    { name: 'Player 3', position: 'DF', stats: 'Clearances: 25' },
    { name: 'Player 4', position: 'DF', stats: 'Interceptions: 15' },
    { name: 'Player 5', position: 'DF', stats: 'Tackles: 40' },
    { name: 'Player 6', position: 'MF', stats: 'Assists: 10' },
    { name: 'Player 7', position: 'MF', stats: 'Passes: 100' },
    { name: 'Player 8', position: 'MF', stats: 'Dribbles: 20' },
    { name: 'Player 9', position: 'FW', stats: 'Goals: 15' },
    { name: 'Player 10', position: 'FW', stats: 'Shots: 50' },
    { name: 'Player 11', position: 'FW', stats: 'Goals: 10' }
  ];

  const bench7 = [
    { name: 'Player 12', position: 'GK', stats: 'Saves: 10' },
    { name: 'Player 13', position: 'DF', stats: 'Tackles: 15' },
    { name: 'Player 14', position: 'MF', stats: 'Assists: 8' },
    { name: 'Player 15', position: 'FW', stats: 'Goals: 5' },
    { name: 'Player 16', position: 'MF', stats: 'Passes: 80' },
    { name: 'Player 17', position: 'DF', stats: 'Clearances: 10' },
    { name: 'Player 18', position: 'FW', stats: 'Shots: 30' }
  ];

  const outsideBench = [
    { name: 'Player 19', position: 'MF', stats: 'Dribbles: 10' },
    { name: 'Player 20', position: 'DF', stats: 'Tackles: 20' },
    { name: 'Player 21', position: 'FW', stats: 'Goals: 3' },
    { name: 'Player 22', position: 'GK', stats: 'Saves: 5' }
  ];

  return (
    <div>
      <Header />
      <div className={styles.container}>
        <h1 className={styles.sutamen}>My Team</h1>

        {/* キャラクターコメントを追加 */}
        <CharacterComment comment="今日はベンチに入れない選手が多いなあ..." />

        {/* タブの切り替え */}
        <div className={styles.tabs}>
          <button
            className={activeTab === 'starting11' ? styles.active : ''}
            onClick={() => setActiveTab('starting11')}
          >
            Starting Members
          </button>
          <button
            className={activeTab === 'bench7' ? styles.active : ''}
            onClick={() => setActiveTab('bench7')}
          >
            Subs
          </button>
          <button
            className={activeTab === 'outsideBench' ? styles.active : ''}
            onClick={() => setActiveTab('outsideBench')}
          >
            Members
          </button>
        </div>

        {/* 選手リストの表示 */}
        <div className={styles.playerList}>
          {activeTab === 'starting11' && (
            <div className={styles.cardGrid}>
              {starting11.map((player, index) => (
                <div key={index} className={styles.playerCard}>
                  <h3>{player.name}</h3>
                  <p>{player.position}</p>
                  <p>{player.stats}</p>
                </div>
              ))}
            </div>
          )}

          {activeTab === 'bench7' && (
            <div className={styles.cardGrid}>
              {bench7.map((player, index) => (
                <div key={index} className={styles.playerCard}>
                  <h3>{player.name}</h3>
                  <p>{player.position}</p>
                  <p>{player.stats}</p>
                </div>
              ))}
            </div>
          )}

          {activeTab === 'outsideBench' && (
            <div className={styles.cardGrid}>
              {outsideBench.map((player, index) => (
                <div key={index} className={styles.playerCard}>
                  <h3>{player.name}</h3>
                  <p>{player.position}</p>
                  <p>{player.stats}</p>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default TeamPage;
