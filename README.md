# 🌿 Healthy Habit Tracker

A command-line habit tracker with machine learning-powered streak predictions. Track your daily habits, view progress, and get AI-based forecasts for future consistency.

## Features

- ✅ Add and log habits daily  
- 📊 View summary reports with completion rates and streaks  
- 🔮 Predict future streaks using a custom linear regression model  
- 💾 Data stored locally in CSV format  
- 🚀 No external dependencies (pure Python standard library)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/healthy-habit-tracker.git
   cd healthy-habit-tracker

2. **Run the application**

```bash
python main.py

```


## Usage

```bash
  ╔══════════════════════════════════════════╗
  ║     🌿 HEALTHY HABIT TRACKER v1.0 🌿     ║
  ║   Track habits. Predict progress. Win.   ║
  ╚══════════════════════════════════════════╝

  MENU
  ─────────────────────────────────────────
  1. Add a new habit
  2. Log habit completion for today
  3. View summary & streaks
  4. Predict future streak (ML)
  5. Exit
  ─────────────────────────────────────────
  Enter your choice (1-5):


```
Add a new habit: Prompts for a habit name and initialises it for today (default completed = False).

Log habit completion: Marks the habit as completed for the current day.

View summary: Shows total logged days, completion percentage, and current streak for each habit.

Predict future streak: Uses historical data to estimate how many days you might maintain the habit over the next week.

## File Structure

```bash
healthy-habit-tracker/
├── data/
│   └── habits.csv               # CSV file storing all habit logs
├── utils/
│   ├── __init__.py
│   ├── display.py               # CLI display helpers
│   └── tracker.py               # Core HabitTracker class (CRUD, streaks)
├── models/
│   ├── __init__.py
│   └── predictor.py             # ML predictor with custom linear regression
├── main.py                      # Main application entry point
├── requirements.txt             # List of dependencies (none required)
└── README.md                    # This file


```


## ML Prediction Details
The streak prediction model is a simple linear regression that uses three features:

Completion rate (last 7 days)

Completion rate (last 14 days)

Current streak length

The model is trained on a mixture of synthetic and real data, and predicts the likely streak length after 7 more days. All calculations are done with custom gradient descent, eliminating the need for numpy or scikit-learn.

## Dependencies
This project uses only the Python standard library. No external packages are required.

csv, os, datetime – for data persistence and date handling

No additional ML libraries are needed

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
MIT


```bash

This README provides a clear overview, usage instructions, and technical insights. It assumes the user has basic Python knowledge and will run the project from the command line.


```
