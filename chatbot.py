import os
import json
import datetime
import csv
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# SSL configuration for NLTK
ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

# Load intents from the JSON file
file_path = os.path.abspath("intents.json")  # Adjust path if needed
with open(file_path, "r") as file:
    intents = json.load(file)

# Create the vectorizer and classifier
vectorizer = TfidfVectorizer()
clf = LogisticRegression(random_state=0, max_iter=10000)

# Preprocess the data
tags, patterns = [], []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

# Training the model
x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)

# Chatbot response function
def chatbot(input_text):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])

# Main App Function
def main():
    st.title("Chatbot Conversations with NLP Intents")

    # Initialize session state for chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []


     # Sidebar Navigation
    st.sidebar.header("🔹 Navigation")
    menu = st.sidebar.radio("Go to", ["Home", "Conversation History","Feedback", "About"])

    # Additional Sidebar Features
    st.sidebar.markdown("---")
    st.sidebar.subheader("⚙️ Reset Chat History")

    # Reset Chat History
    if st.sidebar.button("Reset Chat History"):
          st.session_state.chat_history = []
          if os.path.exists('chat_log.csv'):
               os.remove('chat_log.csv')
          st.success("🔄 Chat history has been reset!")


    # Download Chat History
    st.sidebar.markdown("---")
    st.sidebar.subheader("💾 Download Chat")
    if os.path.exists('chat_log.csv'):
       with open("chat_log.csv", "rb") as file:
          st.sidebar.download_button("Download Chat Log", file, "chat_log.csv", "text/csv")



    # Home Page
    if menu == "Home":
        st.subheader("💬 Chat with the Bot")
        st.write("Type your message below and press Enter to chat.")

        # Display chat history dynamically
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        # Chat input
        user_input = st.chat_input("You:")
        if user_input:
            st.session_state.chat_history.append({"role": "user", "content": user_input})

            # Display user message
            with st.chat_message("user"):
                st.write(user_input)

            # Get chatbot response
            bot_response = chatbot(user_input) if user_input.lower() not in ['goodbye', 'bye'] else "Thank you for chatting! 😊"
            st.session_state.chat_history.append({"role": "assistant", "content": bot_response})

            # Display bot response
            with st.chat_message("assistant"):
                st.write(bot_response)

            # Save conversation to CSV
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open('chat_log.csv', 'a', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([user_input, bot_response, timestamp])

    # Conversation History
    elif menu == "Conversation History":
        st.subheader("📜 Chat History")
        if os.path.exists('chat_log.csv'):
            with open('chat_log.csv', 'r', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader, None)  # Skip header row if exists
                for row in csv_reader:
                    with st.chat_message("user"):
                        st.write(f"User: {row[0]}")
                    with st.chat_message("assistant"):
                        st.write(f"Bot: {row[1]}")
                    st.write(f"🕒 {row[2]}")
                    st.markdown("---")
        else:
            st.write("⚠️ No conversation history available.")
    elif menu == "Feedback":
     st.subheader("📢 Provide Your Feedback")
     feedback = st.text_area("Tell us what you think...")

     if st.button("Submit Feedback"):
          if feedback.strip():
               timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

               # Save feedback in a CSV file (permanent storage)
               with open("feedback.csv", "a", newline="", encoding="utf-8") as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerow([timestamp, feedback])

               st.success("✅ Thank you for your feedback!")

          else:
               st.warning("⚠️ Please enter some feedback before submitting.")

     # Display Previous Feedback
     st.markdown("---")
     st.subheader("📜 Previous Feedback")
     if os.path.exists("feedback.csv"):
          with open("feedback.csv", "r", encoding="utf-8") as csvfile:
               csv_reader = csv.reader(csvfile)
               for row in csv_reader:
                    st.write(f"🕒 {row[0]} - 💬 {row[1]}")
     else:
          st.write("No feedback received yet.")

    elif menu == "About":
        st.write("The goal of this project is to create a chatbot that can understand and respond to user input based on intents. The chatbot is built using Natural Language Processing (NLP) library and Logistic Regression, to extract the intents and entities from user input. The chatbot is built using Streamlit, a Python library for building interactive web applications.")

        st.subheader("📌Project Overview:")
        st.write("""
        The project is divided into two parts:
        1. NLP techniques and Logistic Regression algorithm is used to train the chatbot on labeled intents and entities.
        2. For building the Chatbot interface, Streamlit web framework is used to build a web-based chatbot interface. The interface allows users to input text and receive responses from the chatbot.
        """)

        st.subheader("📚 Dataset:")
        st.write("""
        The dataset used in this project is a collection of labelled intents and entities. The data is stored in a list.
        - Intents: The intent of the user input (e.g. "greeting", "budget", "about")
        - Entities: The entities extracted from user input (e.g. "Hi", "How do I create a budget?", "What is your purpose?")
        - Text: The user input text.
        """)

        st.subheader("💻 Streamlit Chatbot Interface:")
        st.write("The chatbot interface is built using Streamlit. The interface includes a text input box for users to input their text and a chat window to display the chatbot's responses. The interface uses the trained model to generate responses to user input.")

        st.subheader("🔗Conclusion:")
        st.write("In this project, a chatbot is built that can understand and respond to user input based on intents. The chatbot was trained using NLP and Logistic Regression, and the interface was built using Streamlit. This project can be extended by adding more data, using more sophisticated NLP techniques, deep learning algorithms.")


if __name__ == '__main__':
    main()

