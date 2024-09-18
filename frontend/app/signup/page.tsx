'use client'

import React, { useState } from 'react';
import axios from 'axios';
import styles from './Signup.module.css';

const Signup = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');

  const handleSignup = async () => {
    try {
      const response = await axios.post('http://localhost:8000/signup/', {
        email: email,
        password: password,
        name: name,
      });
      alert('Signup successful!');
    } catch (error) {
      console.error(error);
      alert('Signup failed!');
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.card}>
        <h2 className={styles.title}>サインアップ</h2>

        <div className="mb-4">
          <label className={styles.inputLabel}>名前</label>
          <input
            type="text"
            className={styles.inputField}
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </div>

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

        <button onClick={handleSignup} className={styles.button}>
          サインアップ
        </button>
      </div>
    </div>
  );
};

export default Signup;
