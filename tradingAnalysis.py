import praw
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from timedelta import Timedelta 
from datetime import datetime 
import datetime as dt            #library for date management
                    #library for data manipulation
import matplotlib.pyplot as plt  #library for plotting




# Reddit API credentials
client_id = 'hidden'
client_secret = 'hidden' # you can get your own at https://www.reddit.com/wiki/api/
user_agent = 'test'

# Initialize Reddit instance
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

# Subreddit name for AITA
# Define subreddit and keyword
subreddit_name = 'wallstreetbets'



keyword = 'SPY'
#input('What Stock do you want to analyze: ')

# Fetch posts from the subreddit containing the keywordstart_time = int((datetime.utcnow() - timedelta(days=1)).timestamp())
    
    # Fetch posts containing the keyword from the last 24 hours
class trader:
    def __init__(self, keyword):
        self.keyword = keyword

    def get_dates(): 
            today = datetime.now()
            three_days_prior = today - Timedelta(days=3)
            return today.strftime('%Y-%m-%d'), three_days_prior.strftime('%Y-%m-%d')

    # Define function to analyze sentiment of a text
    def analyze_sentiment(self, text, analyzer):
        sentiment = analyzer.polarity_scores(text)
        return sentiment['compound']  # Using compound score as overall sentiment

    # Define function to make trading decision based on sentiment
    def make_trading_decision(sentiment_score):
        if sentiment_score >= 0.1:
            return 'BUY'
        else:
            return 'SELL'
    
    def run_trading_analysis(self):# Initialize DataFrame to store results
        subreddit = reddit.subreddit(subreddit_name)
        posts = subreddit.search(keyword, sort='new', time_filter='all', limit=20)
        analyzer = SentimentIntensityAnalyzer()
        results = []
        buyCount = 0;
        sellCount = 0;
        holdCount = 0;

        # Iterate through fetched posts and analyze sentiment
        for post in posts:
            title_sentiment = self.analyze_sentiment(post.title, analyzer)
            body_sentiment = self.analyze_sentiment(post.selftext, analyzer)
            total_sentiment = (title_sentiment + body_sentiment) / 2  # Average sentiment of title and body
            decision = trader.make_trading_decision(total_sentiment)
            if(decision == 'BUY'):
                buyCount += 1
            elif(decision == 'SELL'):
                sellCount = sellCount + 1
            else:
                holdCount += 1
            results.append({
                'Title': post.title,
                'Sentiment': total_sentiment,
                'Decision': decision
            })

        # Convert results to DataFrame for easier analysis
        results_df = pd.DataFrame(results)

        def ans():
            if(buyCount > sellCount):
                return 'BUY'
            else:
                return 'SELL'
            
        print(results_df)
        if(buyCount > sellCount):
            print('Overall Suggestion -- BUY')
            return 'BUY'
        elif(sellCount > buyCount):
            print('Overall Suggestion -- SELL')
            return 'SELL'
        else:
            print('Overall Suggestion -- HOLD')
            return 'BUY'
    # Call ans() and capture its return value


    # Print results
    
trader_instance = trader(keyword)
trader_instance.run_trading_analysis()
