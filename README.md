# Claire - A Rule-Based Chatbot

## Usage

ClaireBot is a simple rule-based chatbot built using NLTK (Natural Language Toolkit) in Python. It provides predefined responses to customer support queries like order status, refunds, returns, and general greetings.

## Features

1. Provides responses based on predefined patterns.
2. Recognizes keywords related to order status, return policy, complaints, and delivery time.
3. Uses NLTK’s regex-based chat module for pattern matching.
4. Simple command-line interface for interaction.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required dependencies:.

```bash
pip install nltk
```

## Customization

To modify responses, update the pairs list in app.py:
```python
pairs = [
    [r"hi|hello|hey", ["Hello! How can I assist you today?", "Hi there! How can I help you?"]],
    [r"i need help", ["How can I help you?"]],
    [r"where is my order?|order status", ["Can you please provide your order number?"]],
]
```
