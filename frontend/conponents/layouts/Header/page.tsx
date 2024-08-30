import styles from "./Header.module.css";

export const Header =()=> {
return (
    <header className={styles.eikan}>
      <div className={styles.logo}>栄冠イレブン</div>
      <nav className={styles.nav}>
        <ul>
          <li><a href="/">ホーム</a></li>
          <li><a href="/players">選手一覧</a></li>
          <li><a href="/tactics">戦術設定</a></li>
          <li><a href="/matches">試合結果</a></li>
        </ul>
      </nav>
    </header>
    )
    
}

