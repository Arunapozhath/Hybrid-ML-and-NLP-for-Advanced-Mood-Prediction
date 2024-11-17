import streamlit as st
import pickle
import numpy as np

def main():
    st.title(":rainbow[Mental Health Mood Prediction]")

    # Load the trained model and scaler
    model = pickle.load(open("model.sav", "rb"))
    scaler = pickle.load(open("scaler.sav", "rb"))

    # Input fields using sliders with appropriate ranges
    user_id = st.slider("User ID", 0, 1000, 1)
    activity_level = st.slider("Activity Level", 0.0, 10.0, 5.0)
    sleep_hours = st.slider("Sleep Hours", 0.0, 24.0, 7.0)
    stress_level = st.slider("Stress Level", 0.0, 10.0, 5.0)
    heart_rate = st.slider("Heart Rate", 40, 180, 70)
    workload = st.slider("Workload", 0.0, 10.0, 5.0)
    nutrition_level = st.slider("Nutrition Level", 0.0, 10.0, 5.0)
    social_interactions = st.slider("Social Interactions", 0.0, 10.0, 5.0)
    sentiment_score = st.slider("Sentiment Score", -1.0, 1.0, 0.0)
    age = st.slider("Age", 0, 120, 25)
    gender = st.slider("Gender (1 for Male, 0 for Female)", 0, 1, 0)
    physical_health_score = st.slider("Physical Health Score", 0.0, 10.0, 5.0)
    location = st.slider("Location (Numeric)", 0, 1000, 0)
    daily_steps = st.slider("Daily Steps", 0, 30000, 5000)
    hours_of_work = st.slider("Hours of Work", 0.0, 24.0, 8.0)
    sleep_quality = st.slider("Sleep Quality", 0.0, 10.0, 5.0)
    weather_condition = st.slider("Weather Condition (Numeric)", 0, 100, 50)
    anxiety_level = st.slider("Anxiety Level", 0.0, 10.0, 5.0)
    day = st.slider("Day", 1, 31, 1)
    hour = st.slider("Hour", 0, 23, 12)
    minute = st.slider("Minute", 0, 59, 30)

    # Feature list in the correct order
    features = [
        user_id, activity_level, sleep_hours, stress_level, heart_rate, workload,
        nutrition_level, social_interactions, sentiment_score, age, gender,
        physical_health_score, location, daily_steps, hours_of_work, sleep_quality,
        weather_condition, anxiety_level,day, hour, minute
    ]

    # Button to make predictions
    pred = st.button('PREDICT')

    if pred:
        try:
            # Convert input to numerical array and reshape for prediction
            features = np.array(features).reshape(1, -1)

            # Standardize the features manually using the scaler
            scaled_features = scaler.transform(features)

            # Display scaled features for reference (optional)
            st.write("Scaled Features:", scaled_features)

            # Make the prediction
            prediction = model.predict(scaled_features)

            # Display the prediction
            st.success(f"Predicted Mood Score: {prediction[0]}")

        except Exception as e:
            st.error(f"An error occurred: {e}")

# Run the app
if __name__ == '__main__':
    main()
