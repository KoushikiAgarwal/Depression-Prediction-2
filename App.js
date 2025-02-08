import React, { useState } from "react";
import axios from "axios";
import "./App.css"; // We'll style it using App.css

function App() {
  const [inputText, setInputText] = useState("");
  const [result, setResult] = useState("");
  const [confidence, setConfidence] = useState("");
  const [backgroundColor, setBackgroundColor] = useState("#fff"); // Default color

  const handleChange = (e) => {
    setInputText(e.target.value);
  };

  const handleSubmit = async () => {
    try {
      const response = await axios.post("http://localhost:5000/predict", {
        text: inputText,
      });
      const prediction = response.data.prediction;
      setResult(prediction);
      setConfidence(response.data.confidence);

      // Change background color based on prediction
      if (prediction === "Depressed") {
        setBackgroundColor("rgb(169, 0, 0)"); // Dark red background for depressed
      } else {
        setBackgroundColor("rgb(0, 128, 0)"); // Green background for not depressed
      }
    } catch (error) {
      console.error("There was an error!", error);
    }
  };

  return (
    <div className="App" style={{ backgroundColor }}>
      <div className="container">
        <h1>Depression Prediction</h1>
        <textarea
          rows="4"
          cols="50"
          value={inputText}
          onChange={handleChange}
          placeholder="Type your thoughts here"
        />
        <br />
        <button onClick={handleSubmit}>Submit</button>

        <div className="result">
          <h2>Prediction: {result}</h2>
    
        </div>
      </div>
    </div>
  );
}

export default App;
