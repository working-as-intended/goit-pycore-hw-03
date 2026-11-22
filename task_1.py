from datetime import datetime


# Обчислює кількість днів між заданою датою і сьогодні.
# Якщо дата некоректна, повертає None.
def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()

        return (today - given_date).days

    except (ValueError, TypeError):
        return None
