import streamlit as st
a=st.chat_input("enter your command")
if a: 	
	st.chat_message("user").write(a)
	if a.lower()== "hi"||"hello":
		st.chat_message("ai").write("Bot: Hello! Nice to meet you.")
	elif a.lower()== "how are you":
		st.chat_message("ai").write("Bot: I am fine. Thank you for asking!")
	elif a.lower() == "what is your name":
		st.chat_message("ai").write("Bot: My name is ChatBot.")
	elif a.lower() == "who are you":
		st.chat_message("ai").write("Bot: I am a chatbot.")
	elif a.lower()== "what are you doing":
		st.chat_message("ai").write("Bot: I am chatting with you.")
	elif a.lower() == "what is your favorite color":
		st.chat_message("ai").write("Bot: My favorite color is blue.")
	elif a.lower() == "do you like music":
		st.chat_message("ai").write("Bot: Yes! I love music.")
	elif a.lower() == "what is your hobby":
		st.chat_message("ai").write("Bot: My hobby is talking with people.")
	elif a.lower() == "are you happy":
		st.chat_message("ai").write("Bot: Yes, I am always happy!")
	elif a.lower() == "thank you":
		st.chat_message("ai").write("Bot: You're welcome!")
	elif a.lower() == "good morning":
		st.chat_message("ai").write("Bot: Good morning! Have a wonderful day.")
	elif a.lower() == "good night":
		st.chat_message("ai").write("Bot: Good night! Sweet dreams.")
	elif a.lower() == "bye":
		st.chat_message("ai").write("Bot: Goodbye! See you again.")
	elif a.lower() ==("what is your favorite time of the day"):
		st.chat_message("ai").write("my favoratie time of the day is evening")

