# traderbot
This program fetches the latest Reddit posts from r/wallstreetbets, filters them by a specific stock, and analyzes their sentiment using VADER. Based on the sentiment analysis, it makes real-time trading decisions to buy the stock using Lumibot and compares it against the SPY.

# example
![newplot](https://github.com/purvajpatel/traderbot/assets/62811831/56dea56b-fb2b-4779-bb17-f7f8c5c5c5dd)

<img width="614" alt="Screenshot 2024-05-29 at 4 41 01 PM" src="https://github.com/purvajpatel/traderbot/assets/62811831/5ec2e73b-f65f-4a2a-8a63-a71a68cc8d0f">

# learnings
Overall, WallStreetBets is not the best tool to follow investment advice.

# limitations
Reddit does not allow to pull posts from specific date ranges (ex. March 12th to April 12th) instead only being able to use 'hot', 'top', and new. This makes it difficult to truly back-test large amounts of data.

