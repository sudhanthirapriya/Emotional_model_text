responses = {
    'joy': "I'm so happy for you! What's making your day so good?",
    'sadness': "I'm sorry you're feeling this way. Do you want to talk about it?",
    'anger': "That sounds frustrating. What happened?",
    'fear': "It’s okay to feel this way. Can I help with anything?"
}

def generate_response(emotion):
    return responses.get(emotion.lower(), "I'm here to listen.")
