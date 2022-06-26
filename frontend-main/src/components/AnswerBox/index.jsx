import styles from "./index.module.css";

const AnswerBox = ({ answer }) => {
  return (
    <div className={styles.container}>
      <p>{answer}</p>
    </div>
  );
};

export default AnswerBox;
