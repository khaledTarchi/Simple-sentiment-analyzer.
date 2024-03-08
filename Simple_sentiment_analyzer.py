import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import random


nltk.download('vader_lexicon')


class Creative_Sentiment_Analysis:
    
    def __init__(self):
        self.sentiment_analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):
        sentiment_score = self.sentiment_analyzer.polarity_scores(text)['compound']

        if sentiment_score >= 0.5:
            return "Wow! That's fantastic! 😃"
        elif 0.2 <= sentiment_score < 0.5:
            return "I sense some positivity! Keep it up! 👍"
        elif -0.2 <= sentiment_score < 0.2:
            return "Neutral vibes... Interesting! 🤔"
        elif -0.5 <= sentiment_score < -0.2:
            return "Feeling a bit down? Cheer up! 🙁"
        else:
            return "Oh no, that seems tough. I'm here for you! 😢"

    def generate_creative_response(self, text):
        sentiment_response = self.analyze_sentiment(text)
        creative_options = [
            "Your words inspire creativity in me! 🌟",
            "Let's turn those emotions into a masterpiece! 🎨",
            "I sense a story waiting to be told! ✨"
        ]
        return f"{sentiment_response}\n{random.choice(creative_options)}"

print("\n\n Enter text:")
user_text = input("----->>>>>")
creative_sentiment_analysis = Creative_Sentiment_Analysis()
response = creative_sentiment_analysis.generate_creative_response(user_text)
print(response)
