# orderbot
OrderBot is a simple bot that helps you order pizza. It is based on the OpenAI 'completion' API method.

You will need Streamlit: ***pip install streamlit***.

You'll also need to add you OpenAI API KEY. Please modify the code accordingly to set ***openai.api_key*** with your api key. It can be as simple as:

   ***openai.api_key = <YOUR_API_KEY>***

To run the bot, enter the following command in the terminal: 

   ***streamlit run app_bot_streamlit.py*** 

This command assumes you are in the same folder as the .py file.

To get started, say ***Hi*** in the input box.

ToDos:
1. Clean the input box after each user input.
2. Have the bot great you first.
