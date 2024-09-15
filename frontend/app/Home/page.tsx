import Link from 'next/link';
import styles from '../Home/Home.module.css';

const Home = () => {
  return (
    <div className={styles.container}>
      <h1 className={styles.title}>ホームページ</h1>
      <p>ここは栄冠イレブンのホームページです。</p>
      <Link href="/players">
        <a className={styles.button}>選手一覧を見る</a>
      </Link>
    </div>
  );
};

export default Home;
