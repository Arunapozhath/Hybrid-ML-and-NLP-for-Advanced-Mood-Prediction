import mysql.connector

# Establishing the connection
conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Adithya@12',
    database='mental_health_project'
)

# Creating a cursor object
cursor = conn.cursor()

# Function to insert a new record
def insert_data(data):
    insert_query = """
    INSERT INTO mental_health_data (
        user_id, mood_score, activity_level, sleep_hours, stress_level,
        heart_rate, workload, nutrition_level, social_interactions,
        sentiment_score, age, gender, physical_health_score, location,
        daily_steps, hours_of_work, sleep_quality, weather_condition,
        social_media_posts, anxiety_level
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    try:
        cursor.execute(insert_query, data)
        conn.commit()
        print("Data inserted successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")

# Sample data to insert (Replace with your actual values)
sample_data = (
    1, 7.5, 8, 7.0, 5,
    72, 6, 7, 10,
    0.85, 25, "Female", 8.2, "Hyderabad",
    5000, 8, 9, "Sunny", "Feeling positive about the day", 3
)

# Insert the sample data
insert_data(sample_data)

# Close the cursor and connection
cursor.close()
conn.close()
