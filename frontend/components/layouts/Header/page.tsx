import Link from 'next/link'; // Next.jsのLinkコンポーネントをインポート
import styles from "./Header.module.css";

export const Header = () => {
  return (
    <header className={styles.eikan}>
      <div className={styles.logo}>栄冠イレブン</div>
      <nav className={styles.nav}>
        <ul>
          <li><Link href="/">ホーム</Link></li>
          <li><Link href="/players">選手一覧</Link></li>
          <li><Link href="/matches">戦術設定</Link></li>
          <li><Link href="/results">試合</Link></li>
        </ul>
      </nav>
    </header>
  );
};