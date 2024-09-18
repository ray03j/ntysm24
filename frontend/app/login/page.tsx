'use client'

import React, { useState } from 'react';
import axios from 'axios';
import styles from './Login.module.css';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    try {
      const response = await axios.post('http://localhost:8000/login/', {
        email: email,
        password: password,
      });
      alert('Login successful! Token: ' + response.data.access_token);
    } catch (error) {
      console.error(error);
      alert('Login failed!');
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.card}>
        <h2 className={styles.title}>ログイン</h2>

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

        <button onClick={handleLogin} className={styles.button}>
          ログイン
        </button>
      </div>
    </div>
  );
};

export default Login;
