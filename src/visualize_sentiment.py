import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your sentiment output file
df = pd.read_csv('output/sentiment_results.csv')  # adjust path

# Sentiment distribution
plt.figure(figsize=(6,4))
sns.countplot(x='sentiment', data=df, palette='Set2')
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('visuals/sentiment_distribution.png')
plt.show()

# Sentiment over time
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])
    time_series = df.groupby(df['date'].dt.date)['sentiment'].value_counts().unstack().fillna(0)
    time_series.plot(kind='line', figsize=(10,5))
    plt.title('Sentiment Over Time')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('visuals/sentiment_over_time.png')
    plt.show()
