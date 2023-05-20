import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def get_activity_suggestions(mood):
    suggestions = {
        "Happy": ["Go for a walk in nature", "Listen to uplifting music", "Call a friend"],
        "Sad": ["Write in a journal", "Watch a funny movie", "Practice deep breathing"],
        "Anxious": ["Try meditation or mindfulness", "Engage in physical exercise", "Take a break from screens"],
        "Stressed": ["Take a warm bath or shower", "Practice yoga or stretching", "Spend time with a pet"],
        "Angry": ["Take a break and count to 10", "Write down your feelings in a letter (but don't send it)", "Engage in a creative activity"]
    }
    if mood in suggestions:
        return suggestions[mood]
    else:
        return []

def track_mood(data, mood, timestamp):
    data = data.append({"Mood": mood, "Timestamp": timestamp}, ignore_index=True)
    return data

def plot_mood_over_time(data):
    mood_counts = data["Mood"].value_counts()
    fig, ax = plt.subplots()
    ax.bar(mood_counts.index, mood_counts.values)
    ax.set_xlabel("Mood")
    ax.set_ylabel("Count")
    ax.set_title("Mood Distribution Over Time")
    st.pyplot(fig)

def main():
    st.title("Mental Health Tracker")
    st.write("Welcome to the Mental Health Tracker App!")
    st.write("Track your mood and emotions, and get activity suggestions to improve your well-being.")

    data = pd.DataFrame(columns=["Mood", "Timestamp"])

    mood = st.selectbox(
        "Select your current mood",
        ("Happy", "Sad", "Anxious", "Stressed", "Angry")
    )

    timestamp = pd.to_datetime("today")
    data = track_mood(data, mood, timestamp)

    st.write(f"You selected: {mood}")

    activity_suggestions = get_activity_suggestions(mood)

    if activity_suggestions:
        st.write("Activity Suggestions:")
        for suggestion in activity_suggestions:
            st.write(f"- {suggestion}")
    else:
        st.write("No activity suggestions available for this mood.")

    st.write("## Mood Over Time")
    plot_mood_over_time(data)

if __name__ == '__main__':
    main()
