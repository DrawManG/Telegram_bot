# Telegram chatbot for monitoring offensive messages

This is a Telegram chatbot designed to monitor offensive messages and respond with a variety of commands. The bot has the following commands:

1. `start666` - Starts the bot and verifies admin access
2. `delete_message_with_phrase` - Filters the chat for messages containing offensive language
3. `-sms` - Deletes the message to which a response was made
4. `-mut` - Issues a mute to the user who posted the offending message
5. `-bon` - Issues a ban to the user who posted the offending message

## Installation

To install the chatbot, copy the `context.py` file to your project folder. This file should contain the following variables:

1. `forbidden_words` - an array of offensive words that will trigger a bot response when detected
2. `forbidden_words2` - a test array for detecting multiple keywords in a message
3. `TOKEN` - the bot's token
4. `allowed_users` - the IDs of all admin users (entered manually)

## Docker Installation

To install and run the chatbot using Docker, follow these steps:

1. Run `sudo usermod -aG docker $USER` to add your user account to the Docker group
2. Run `docker build -t my_bot_image .` to build the Docker image
3. Run `docker run -d my_bot_image` to start the bot in a Docker container. 

The base code and MD-file created by ChatGPT.

If you have any questions, please don't hesitate to ask! 
TG: @trigantail
