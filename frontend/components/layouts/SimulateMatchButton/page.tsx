// components/layouts/SimulateMatchButton/page.tsx
import React, { PropsWithChildren } from 'react';
import styles from "./SimulateMatchButton.module.css";

// propsの型定義 (TypeScript)
type SimulateMatchButtonProps = PropsWithChildren<{
  strategy: string; // 戦術を受け取るためのプロップ
  onClick: (strategy: string) => void; // 戦術を引数に取るコールバック
}>;

const SimulateMatchButton: React.FC<SimulateMatchButtonProps> = ({ strategy, children, onClick }) => {
  const handleClick = () => {
    onClick(strategy); // 戦術を引数としてコールバックを呼び出す
  };

  return (
    <div>
      <button className={styles.btn} onClick={handleClick}>{children}</button>
    </div>
  );
};

export default SimulateMatchButton;
