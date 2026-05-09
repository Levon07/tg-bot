import feedparser

# free X accounts via RSS mirrors
FEEDS = [
    "https://nitter.net/elonmusk/rss",
    "https://nitter.net/Bitcoin/rss",
    "https://nitter.net/Coinbase/rss"
]

def get_latest_tweets():
    tweets = []

    for url in FEEDS:
        feed = feedparser.parse(url)

        for entry in feed.entries[:3]:
            tweets.append({
                "source": url,
                "title": entry.title,
                "published": entry.published
            })

    return tweets


def analyze_tweets(tweets):
    score = 0

    for t in tweets:
        text = t["title"].lower()

        if "bitcoin" in text or "btc" in text:
            if "up" in text or "surge" in text or "breakout" in text:
                score += 1
            if "down" in text or "drop" in text or "hack" in text:
                score -= 1

    return score


if __name__ == "__main__":
    tweets = get_latest_tweets()
    score = analyze_tweets(tweets)

    print("SENTIMENT SCORE:", score)