import { useState } from "react";
import "./App.css";
import AnswerBox from "./components/AnswerBox";
import ChatBox from "./components/ChatBox";
import "./styles/_font.css";

function App() {
  const [answer, setAnswer] = useState("");

  return (
    <div className="App">
      <ChatBox setAnswer={setAnswer} />
      {answer.length > 0 && <AnswerBox answer={answer} />}
    </div>
  );
}

export default App;
