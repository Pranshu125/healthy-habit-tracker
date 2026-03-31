"""
tracker.py - Core habit tracking logic with CSV persistence
"""

import csv
import os
from datetime import date, timedelta
from models.predictor import HabitPredictor


DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/habits.csv")


class HabitTracker:
    def __init__(self):
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["habit", "date", "completed"])

    def _read_all(self):
        rows = []
        with open(DATA_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
        return rows

    def _write_all(self, rows):
        with open(DATA_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["habit", "date", "completed"])
            writer.writeheader()
            writer.writerows(rows)

    def add_habit(self, name):
        rows = self._read_all()
        today = str(date.today())
        # Avoid duplicate entries for today
        for row in rows:
            if row["habit"].lower() == name.lower() and row["date"] == today:
                print(f"  ✗ Habit '{name}' already exists for today.")
                return
        rows.append({"habit": name, "date": today, "completed": "False"})
        self._write_all(rows)

    def list_habits(self):
        rows = self._read_all()
        return list({row["habit"] for row in rows})

    def log_habit(self, name):
        rows = self._read_all()
        today = str(date.today())
        found = False
        for row in rows:
            if row["habit"].lower() == name.lower() and row["date"] == today:
                row["completed"] = "True"
                found = True
                break
        if not found:
            rows.append({"habit": name, "date": today, "completed": "True"})
        self._write_all(rows)
        print(f"\n  ✓ '{name}' logged as completed for {today}!")

    def get_streak(self, name):
        rows = self._read_all()
        completed_dates = sorted(
            {row["date"] for row in rows
             if row["habit"].lower() == name.lower() and row["completed"] == "True"},
            reverse=True
        )
        if not completed_dates:
            return 0
        streak = 0
        check_date = date.today()
        for d in completed_dates:
            if str(check_date) == d:
                streak += 1
                check_date -= timedelta(days=1)
            else:
                break
        return streak

    def show_summary(self):
        habits = self.list_habits()
        if not habits:
            print("\n  No habits found. Start adding habits!")
            return
        print("\n  ╔══════════════════════════════════════╗")
        print("  ║         HABIT SUMMARY REPORT         ║")
        print("  ╚══════════════════════════════════════╝")
        rows = self._read_all()
        for habit in habits:
            habit_rows = [r for r in rows if r["habit"].lower() == habit.lower()]
            total = len(habit_rows)
            done = sum(1 for r in habit_rows if r["completed"] == "True")
            streak = self.get_streak(habit)
            rate = (done / total * 100) if total > 0 else 0
            print(f"\n  Habit      : {habit}")
            print(f"  Logged Days: {total}")
            print(f"  Completed  : {done} ({rate:.1f}%)")
            print(f"  Streak     : {streak} day(s)")
        print()

    def predict_streak(self):
        habits = self.list_habits()
        if not habits:
            print("\n  No habits to predict. Add and log habits first!")
            return
        print("\n  Available habits:")
        for i, h in enumerate(habits, 1):
            print(f"  {i}. {h}")
        name = input("\n  Enter habit name to predict: ").strip()
        if name not in habits and name.lower() not in [h.lower() for h in habits]:
            print(f"  ✗ Habit '{name}' not found.")
            return

        rows = self._read_all()
        predictor = HabitPredictor()
        prediction = predictor.predict(rows, name)
        print(f"\n  ╔══════════════════════════════════════╗")
        print(f"  ║        ML STREAK PREDICTION          ║")
        print(f"  ╚══════════════════════════════════════╝")
        print(f"  Habit   : {name}")
        print(f"  Current : {self.get_streak(name)} day streak")
        print(f"  Predicted streak next week: {prediction} days")
        print(f"  Tip: {'Keep it up! You are on a great streak!' if prediction > 3 else 'Try to be more consistent this week!'}")
        print()
