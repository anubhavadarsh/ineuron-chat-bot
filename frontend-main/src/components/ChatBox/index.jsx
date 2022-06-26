import styles from "./index.module.css";
import useGetAnswer from "./hook";
import { useState } from "react";

const ChatBox = ({ setAnswer }) => {
  const [input, setInput] = useState("");

  const { getAnswer } = useGetAnswer();

  const handleChange = (e) => {
    setInput(e.target.value);
  };

  const handleFormSubmit = () => {
    if (input.length === 0) return;
    getAnswer(input, setAnswer);
  };

  return (
    <div className={styles.container}>
      <input
        type="text"
        value={input}
        onChange={handleChange}
        onBlur={handleFormSubmit}
      />
    </div>
  );
};

export default ChatBox;
