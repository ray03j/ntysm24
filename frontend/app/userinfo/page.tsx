"use client";
import { useState } from 'react';
import styles from '../userinfo/userinfo.module.css';
import { Header } from '@/components/layouts/Header/page';

const SettingsPage = () => {
  // 仮のユーザーデータを保存するステート
  const [userData, setUserData] = useState({
    username: '山田 太郎',
    email: 'taro.yamada@example.com',
    notificationsEnabled: true, // 通知設定
  });

  

  // 通知設定の変更処理
  const handleNotificationsToggle = () => {
    setUserData({
      ...userData,
      notificationsEnabled: !userData.notificationsEnabled,
    });
  };

  return (
    <div>
        <Header />
        <div className={styles.container}>
            <h1>ユーザー情報</h1>


        <div className={styles.infoSection}>
            <label>名前</label>
            <p>{userData.username}</p>
        </div>

         <div className={styles.infoSection}>
            <label>メールアドレス</label>
            <p>{userData.email}</p>
         </div>


        <div className={styles.infoSection}>
            <label>通知設定</label>
            <button onClick={handleNotificationsToggle} className={styles.toggleButton}>
            {userData.notificationsEnabled ? '通知を無効にする' : '通知を有効にする'}
            </button>
        </div>
        </div>
    </div>
  );
};

export default SettingsPage;
