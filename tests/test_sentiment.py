from app.analyzer import analyze_sentiment

def test_positive():
    assert analyze_sentiment("I love this!") == "positive"
