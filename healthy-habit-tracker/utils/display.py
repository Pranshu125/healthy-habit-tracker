"""
display.py - CLI display helpers
"""


def show_banner():
    print("""
  ╔══════════════════════════════════════════╗
  ║     🌿 HEALTHY HABIT TRACKER v1.0 🌿     ║
  ║   Track habits. Predict progress. Win.   ║
  ╚══════════════════════════════════════════╝
    """)


def show_menu():
    print("  ─────────────────────────────────────────")
    print("  MENU")
    print("  ─────────────────────────────────────────")
    print("  1. Add a new habit")
    print("  2. Log habit completion for today")
    print("  3. View summary & streaks")
    print("  4. Predict future streak (ML)")
    print("  5. Exit")
    print("  ─────────────────────────────────────────")
    return input("  Enter your choice (1-5): ").strip()
