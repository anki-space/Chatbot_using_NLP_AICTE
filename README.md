# Chatbot with NLP and Streamlit

## 📌 Project Overview
This project is an **intent-based chatbot** that understands and responds to user queries using **Natural Language Processing (NLP)** and **Machine Learning (ML)** techniques. The chatbot is trained using labeled intents and utilizes **Logistic Regression** for intent classification. The user interface is built with **Streamlit**, making it an interactive and user-friendly web application.

## 🎯 Learning Objectives
- Understand **NLP techniques** for intent recognition.
- Implement a chatbot using **Logistic Regression**.
- Utilize **TF-IDF vectorization** for text feature extraction.
- Build an interactive **UI using Streamlit**.
- Store and manage **conversation history**.
- Develop a **feedback system** to improve chatbot responses.

## 🛠 Tools & Technologies Used
- **Python**: Programming language used for development.
- **Streamlit**: Web framework for building interactive applications.
- **NLTK (Natural Language Toolkit)**: Used for text preprocessing and tokenization.
- **Scikit-learn**: Machine Learning library used for **TF-IDF vectorization** and **Logistic Regression**.
- **TF-IDF Vectorization**: Technique used to convert text data into numerical form.
- **Logistic Regression**: Machine learning algorithm used for intent classification.
- **CSV Storage**: Used for logging conversation history and feedback.

## ⚡ Problem Statement
- Traditional rule-based chatbots lack adaptability and struggle with intent recognition.
- Simple pattern-matching methods do not effectively understand user input.
- Manually attending to every user query is time-consuming and inefficient.
- There is a need for an intelligent chatbot with an **easy-to-use interface**.

## 🔍 Methodology
1. **Data Collection**: Created a JSON file with predefined intents and training patterns.
2. **Text Preprocessing**: Applied tokenization and vectorization using **NLTK and TF-IDF**.
3. **Model Training**: Trained a **Logistic Regression classifier** on labeled intent data.
4. **Chatbot Integration**: Built a function to process user input and return relevant responses.
5. **Web App Deployment**: Developed an **interactive UI using Streamlit**.
6. **User Interaction Features**:
   - **Chat history storage**
   - **Download chat history feature**
   - **Reset chat functionality**
   - **User feedback collection** for chatbot improvement

## 🚀 Features
- **Intelligent intent-based chatbot** using NLP.
- **User-friendly chat interface** with Streamlit.
- **Log conversation history** and allow users to download chat logs.
- **Reset chat feature** to clear previous conversations.
- **Feedback system** to collect and analyze user suggestions.
- **Future Scope**: Expand dataset, integrate **deep learning** models, and improve response accuracy.

## 📂 Project Structure
```
📦 Chatbot Project
 ┣ 📜 intents.json      # Intent dataset with user queries and responses
 ┣ 📜 chatbot.py        # Main chatbot script with NLP and ML integration Streamlit web app interface
 ┣ 📜 chat_log.csv      # Conversation history storage
 ┣ 📜 feedback.csv      # User feedback storage
 ┣ 📜 README.md         # Project documentation
```
## Screenshots

### 1️⃣ Chatbot Interface
<img width="955" alt="home" src="https://github.com/user-attachments/assets/8b2ac9f9-b12c-4db2-8805-022c4d7551e2" />


### 2️⃣ Conversation History Feature
<img width="952" alt="history" src="https://github.com/user-attachments/assets/99cb27c5-9c77-464b-acef-092bf8dae159" />


### 3️⃣ Feedback System
<img width="960" alt="feedback" src="https://github.com/user-attachments/assets/b71063a7-45d4-4e21-8790-71ef49ea2ab0" />



## 🏗 Installation & Setup
### Prerequisites
Ensure you have **Python 3.x** installed. Install the required dependencies using:
```bash
pip install -r requirements.txt
```

### Run the Chatbot
Execute the following command to launch the chatbot web application:
```bash
streamlit run chatbot.py
```

## 🎯 Conclusion
- Developed an **intent-based chatbot** capable of understanding and responding to user queries.
- Built an **interactive UI** using Streamlit for seamless user interaction.
- Incorporated **chat history storage, download, and reset features**.
- Implemented a **feedback system** for continuous improvement.
- Future improvements include **expanding the dataset** and **integrating deep learning models** for better accuracy.

## 🔗 Project Repository
The complete source code is available on GitHub: [github.com/anki-space/Chatbot_using_NLP_AICTE](https://github.com/anki-space/Chatbot_using_NLP_AICTE).

---
✉️ **For any queries, feel free to contribute or reach out!** 🚀

