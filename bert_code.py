import mysql.connector
from transformers import pipeline
from datetime import datetime

# Specify a particular model for sentiment analysis
sentiment_analyzer = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

# Function to get sentiment score (0 = Negative, 1 = Positive)
def get_sentiment(text):
    result = sentiment_analyzer(text)
    return 1 if result[0]['label'] == 'POSITIVE' else 0


# Connect to the MySQL database
conn = mysql.connector.connect(
    host="127.0.0.1",  # Replace with your actual database host
    user="root",  # Replace with your actual username
    password="Adithya@12",  # Replace with your actual password
    database="mental_health_project"  # Replace with your actual database name
)

cur = conn.cursor()

# Query to select the social media posts that need sentiment analysis
cur.execute("SELECT user_id, social_media_posts FROM mental_health_data WHERE sentiment_score IS NULL")

# Fetch all rows from the query
rows = cur.fetchall()

# Process each row
for row in rows:
    user_id = row[0]
    social_media_post = row[1]

    # Get sentiment score from BERT
    sentiment_score = get_sentiment(social_media_post)

    # Update the sentiment score in the database for this user
    cur.execute("""
        UPDATE mental_health_data
        SET sentiment_score = %s
        WHERE user_id = %s
    """, (sentiment_score, user_id))

    # Print out the user_id and sentiment_score after update
    print(f"User ID: {user_id}, Sentiment Score: {sentiment_score}")


# Query to check the updated sentiment scores
cur.execute("SELECT user_id, sentiment_score FROM mental_health_data WHERE sentiment_score IS NOT NULL")

# Fetch the updated rows
updated_rows = cur.fetchall()

# Print the updated sentiment scores for all users
print("\nUpdated Sentiment Scores:")
for row in updated_rows:
    user_id = row[0]
    sentiment_score = row[1]
    print(f"User ID: {user_id}, Updated Sentiment Score: {sentiment_score}")


# Commit changes and close the connection
conn.commit()
cur.close()
conn.close()
