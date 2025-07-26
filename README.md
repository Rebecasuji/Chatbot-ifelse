# 🤖 Rule-Based Chatbot using Python (if-else logic)

## 📌 Project Title
RuleBot - A Simple Rule-Based Chatbot Using If-Else Statements in Python

---

## 🧠 Objective

The purpose of this project is to **understand the basic structure of a chatbot** using a **rule-based approach with if-else statements**. This project simulates basic **Natural Language Processing (NLP)** by recognizing user inputs through keyword matching and returning appropriate responses.

It helps beginners:
- Learn input/output loops
- Practice conditional logic (`if`, `elif`, `else`)
- Understand how a chatbot interacts
- Lay the foundation for advanced NLP and ML-based chatbots

---

## 💡 Key Features

- 🔄 Continuous chat loop using `while` loop
- 📥 Accepts dynamic user input via `input()`
- 🧠 Responds based on simple keyword recognition
- 🗣️ Handles basic questions like greetings, bot name, user name, time
- 👋 Exit when the user types "bye", "exit", or "quit"
- 🔎 Demonstrates basic string parsing and logic-based decision making

---

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **IDE**: Visual Studio Code (or any Python-supported editor)
- **No external libraries required**

---

## 📂 Project Structure

rule_based_chatbot/
├── chatbot.py # Main chatbot script
└── README.md # Project documentation


## 🚀 How to Run This Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/rule-based-chatbot.git
cd rule-based-chatbot

Code Overview
Here’s a breakdown of some key logic:

while True:
    user_input = input("You: ").lower().strip()
