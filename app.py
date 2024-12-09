from flask import Flask, render_template, request

app = Flask(__name__)

# Define a list of emotions for detection
emotion_list = ['neutral', 'anger', 'joy', 'love', 'excitement', 'surprise', 'sadness', 'confusion']

# Predefined responses for the bot
responses = {
    "neutral": "This is a response from the chatbot.",
    "anger": "Calm down, there's no need to be angry.",
    "joy": "I'm glad you're feeling joyful!",
    "love": "I love you too!",
    "excitement": "That sounds really exciting!",
    "surprise": "Wow, I didn’t see that coming!",
    "sadness": "I'm sorry you're feeling sad.",
    "confusion": "Can you clarify that for me?"
}

# Function to detect emotion from user input
def detect_emotion(user_input):
    for emotion in emotion_list:
        if emotion in user_input.lower():
            return emotion
    return 'neutral'

@app.route('/', methods=['GET', 'POST'])
def home():
    conversation = []  # Initialize conversation as an empty list

    if request.method == 'POST':
        user_message = request.form['text']  # Get user message from form input
        bot_emotion = detect_emotion(user_message)  # Detect emotion from user input
        bot_response = responses.get(bot_emotion, "Sorry, I didn't understand that.")  # Get bot response

        # Append user message and bot response to the conversation
        conversation.append({'type': 'user', 'message': user_message})
        conversation.append({'type': 'bot', 'message': bot_response, 'emotion': bot_emotion})

    return render_template('index.html', conversation=conversation)


if __name__ == '__main__':
    app.run(debug=True)
