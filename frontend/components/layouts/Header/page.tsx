import Link from 'next/link'; // Next.jsのLinkコンポーネントをインポート
import styles from "./Header.module.css";

export const Header = () => {
  return (
    <header className={styles.eikan}>
      <div className={styles.logo}>EikanEleven</div>
      <nav className={styles.nav}>
        <ul>
          <li><Link href="/players">Plyers</Link></li>
          <li><Link href="/matches">Tactics</Link></li>
          <li><Link href="/results">Matches</Link></li>
          <li><Link href="/userinfo">User</Link></li>
        </ul>
      </nav>
    </header>
  );
};