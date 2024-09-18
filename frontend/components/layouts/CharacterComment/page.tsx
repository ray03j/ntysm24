
import React from 'react';
import styles from './CharacterComment.module.css';

interface CharacterCommentProps {
  comment: string; // comment の型を string に指定
}

const CharacterComment: React.FC<CharacterCommentProps> = ({ comment }) => {
  return (
    <div className={styles.characterContainer}>
      <div className={styles.character}>
        <img src="/character.png" alt="キャラクター" />
      </div>
      <div className={styles.speechBubble}>
        <p>{comment}</p>
      </div>
    </div>
  );
};

export default CharacterComment;
