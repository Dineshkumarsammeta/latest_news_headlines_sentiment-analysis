🗞️ Data README — News Headlines Sentiment Analysis
📘 Overview

This dataset is dynamically collected from multiple news sources using the NewsAPI.org
 service.
The data contains headline text, publication date, source name, and URL for the top news articles from trusted global publishers such as CNN, BBC News, and The Wall Street Journal.

These headlines are used for sentiment analysis, topic tracking, and trend visualization in the main project pipeline.

🧩 Data Sources

The following sources are fetched via NewsAPI using JSON endpoints:

Source	Endpoint URL	Type	Example Output
CNN	https://newsapi.org/v1/articles?source=cnn&sortBy=top&apiKey=YOUR_API_KEY	General News	Top U.S. and world headlines
The Washington Post	https://newsapi.org/v1/articles?source=the-washington-post&sortBy=top&apiKey=YOUR_API_KEY	Political, social	U.S. and global news
BBC News	https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=YOUR_API_KEY	Global	International coverage
ABC News (AU)	https://newsapi.org/v1/articles?source=abc-news-au&sortBy=top&apiKey=YOUR_API_KEY	Regional	Australian news
Financial Times	https://newsapi.org/v1/articles?source=financial-times&sortBy=top&apiKey=YOUR_API_KEY	Business	Finance & market news
Bloomberg	https://newsapi.org/v1/articles?source=bloomberg&sortBy=top&apiKey=YOUR_API_KEY	Business	Financial updates
Wall Street Journal	https://newsapi.org/v1/articles?source=the-wall-street-journal&sortBy=top&apiKey=YOUR_API_KEY	Business	Market trends & analysis
📦 Example Fetch Code (from pipeline)
import pandas as pd

cnn = pd.read_json('https://newsapi.org/v1/articles?source=cnn&sortBy=top&apiKey=YOUR_API_KEY')
bbc = pd.read_json('https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=YOUR_API_KEY')
wsj = pd.read_json('https://newsapi.org/v1/articles?source=the-wall-street-journal&sortBy=top&apiKey=YOUR_API_KEY')

# Combine multiple sources into a single dataframe
news_data = pd.concat([cnn, bbc, wsj], ignore_index=True)
news_data.to_csv("data/headlines_raw.csv", index=False)

⚙️ Columns
Column Name	Description
source	News source (e.g., CNN, BBC)
author	Article author (if available)
title	News headline
description	Short article summary
url	Link to the full article
urlToImage	Associated image link
publishedAt	Publication timestamp
🧪 Usage

Fetch JSON data using your NewsAPI key.

Store as CSV/JSON in the data/ folder for reproducibility.

Use src/pipeline.py or src/fetch.py to preprocess, clean, and run sentiment analysis.

The processed sentiment outputs are stored in metrics/metrics.csv and used for dashboard visualisation.

⚖️ Data Licensing & Attribution

Source: NewsAPI.org

License: Content provided under News API Developer Terms
.

Attribution: Headlines and metadata are property of their respective publishers.

Note: This project uses only top headlines metadata (titles & timestamps) for educational and research purposes — no full text content is stored.

🧭 Notes

Ensure your API key is valid and stored securely in a .env file (NEWS_API_KEY).

API free tier may have rate limits — consider caching results locally.

For production, schedule fetching via cron or Airflow DAG.
