'use client'

import React, { useState } from 'react';
import styles from './Signin.module.css';

const Signin = () => {
  const [isLogin, setIsLogin] = useState(true);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    // login logic
  };

  const handleSignup = () => {
    // signup logic
  };

  return (
    <div className={styles.container}>
      <div className={styles.card}>
        <h2 className={styles.title}>
          {isLogin ? 'ログイン' : 'サインアップ'}
        </h2>

        <div className="mb-4">
          <label className={styles.inputLabel}>メールアドレス</label>
          <input
            type="email"
            className={styles.inputField}
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>

        <div className="mb-4">
          <label className={styles.inputLabel}>パスワード</label>
          <input
            type="password"
            className={styles.inputField}
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>

        <button
          onClick={isLogin ? handleLogin : handleSignup}
          className={styles.button}
        >
          {isLogin ? 'ログイン' : 'サインアップ'}
        </button>

        <p className={styles.switchText}>
          {isLogin ? 'アカウントをお持ちでないですか？' : '既にアカウントをお持ちですか？'}
          <button
            onClick={() => setIsLogin(!isLogin)}
            className={styles.link}
          >
            {isLogin ? 'サインアップ' : 'ログイン'}
          </button>
        </p>
      </div>
    </div>
  );
};

export default Signin;
