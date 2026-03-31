"""
Healthy Habit Tracker - Main Entry Point
A CLI-based habit tracker with ML-powered streak predictions.
"""

from utils.tracker import HabitTracker
from utils.display import show_menu, show_banner


def main():
    show_banner()
    tracker = HabitTracker()

    while True:
        choice = show_menu()

        if choice == "1":
            name = input("\nEnter habit name: ").strip()
            if name:
                tracker.add_habit(name)
                print(f"  ✓ Habit '{name}' added successfully!")
            else:
                print("  ✗ Habit name cannot be empty.")

        elif choice == "2":
            habits = tracker.list_habits()
            if not habits:
                print("\n  No habits tracked yet. Add one first!")
            else:
                print("\n  Your Habits:")
                for i, h in enumerate(habits, 1):
                    print(f"  {i}. {h}")
                habit = input("\nEnter habit name to log for today: ").strip()
                tracker.log_habit(habit)

        elif choice == "3":
            tracker.show_summary()

        elif choice == "4":
            tracker.predict_streak()

        elif choice == "5":
            print("\n  Thanks for using Healthy Habit Tracker. Stay consistent! 💪\n")
            break

        else:
            print("\n  Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()
