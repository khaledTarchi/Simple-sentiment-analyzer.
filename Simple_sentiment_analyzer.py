import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QTextEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from nltk.sentiment import SentimentIntensityAnalyzer
import random
import nltk

nltk.download('vader_lexicon')


class SentimentAnalyzerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.sentiment_analyzer = SentimentIntensityAnalyzer()

        # Create GUI components
        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText("Enter text here...")
        self.result_label = QLabel(self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("QLabel { color: #333; font-size: 16px; }")

        self.analyze_button = QPushButton('Analyze Sentiment', self)
        self.analyze_button.clicked.connect(self.analyze_button_clicked)
        self.analyze_button.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; border: none; "
                                          "padding: 10px 20px; border-radius: 5px; font-size: 16px; }"
                                          "QPushButton:hover { background-color: #45a049; }")

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.result_label)
        layout.addWidget(self.analyze_button)

        self.setLayout(layout)

        # Set up the main window
        self.setWindowTitle('Sentiment Analyzer')
        self.setGeometry(300, 300, 400, 250)
        self.setStyleSheet("background-color: #f0f0f0;")

    def analyze_button_clicked(self):
        user_text = self.text_edit.toPlainText()
        creative_sentiment_analysis = CreativeSentimentAnalysis()
        response = creative_sentiment_analysis.generate_creative_response(user_text)
        self.result_label.setText(response)


class CreativeSentimentAnalysis:
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SentimentAnalyzerApp()
    
    # Set a custom font for the application
    font = QFont("Arial", 12)
    app.setFont(font)
    
    window.show()
    sys.exit(app.exec_())
