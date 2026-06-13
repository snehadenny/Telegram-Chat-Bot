🤖 Telegram AI Chat Bot (Python Project)

A simple Python-based Telegram chatbot that uses the Telegram Bot API and a custom AI logic engine to automatically respond to user messages in real time.

This project demonstrates how automation, REST APIs, and basic AI logic can be combined to build a working chatbot system using Python.

---

📌 Features

- Real-time message handling via Telegram Bot API  
- Automated responses using custom AI logic  
- Polling-based message fetching system  
- Lightweight and easy to run Python application  
- Modular design (bot logic + AI engine separation)  

---

# 📸 Chatbot Preview

<table>
  <tr>
    <td align="center">
      <img src="chat1.jpeg" width="240px"><br>
      <b>Conversation Example 1</b>
    </td>
    <td align="center">
      <img src="chat2.jpeg" width="240px"><br>
      <b>Conversation Example 2</b>
    </td>
  </tr>
</table>

---
🧠 Technologies Used

| Area            | Tools / Libraries              |
|----------------|--------------------------------|
| Language        | Python 3.x                     |
| API             | Telegram Bot API              |
| HTTP Requests   | requests library              |
| Data Format     | JSON                          |
| Architecture    | REST API + Polling System     |

---

📁 Project Structure

Telegram-Chat-Bot/

├── bot.py              # Main bot script (handles messages & polling)
├── aiengine.py         # AI response logic engine
├── requirements.txt    # Dependencies
└── README.md           # Project documentation

---

⚙️ How to Run Locally

1. Clone the Repository
```bash
git clone https://github.com/your-username/Telegram-Chat-Bot.git
cd Telegram-Chat-Bot
```
2. Install Dependencies
```
pip install -r requirements.txt
```
3. Create Telegram Bot
- Open Telegram
- Search for @BotFather
- Create a new bot
- Copy the BOT TOKEN
  
4. Configure Token
Add your token in bot.py:
```
TOKEN = "YOUR_BOT_TOKEN"
```
5. Run the Bot
```
python bot.py
```
## 🌐 Output

- Bot continuously listens for messages
- Processes input using AI logic engine
- Sends automated replies instantly

# 📊 Advantages

- Simple and lightweight implementation
- Easy integration with Telegram Bot API
- Good beginner-level Python project
- Demonstrates real-time API communication
- Easy to extend with new AI logic

# ⚠️ Limitations

- Uses polling instead of webhook (less efficient)
- No database for storing chat history
- Limited AI intelligence (rule-based responses)
- No memory/context retention
- Not suitable for production-scale systems

# 🚀 Future Scope

- Integration with NLP/AI models for smarter replies
- Switch from polling to webhook system
- Add database for chat history
- Add voice message support
- Improve context-aware conversation handling
- Deploy bot on cloud platforms

📄 License

This project is licensed under the MIT License.

🙋‍♂️ Author

Sneha Denny
