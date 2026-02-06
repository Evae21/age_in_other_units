from datetime import date
import argparse


def calculate_age_units(birth_date: date) -> dict:
    today = date.today()
    if birth_date > today:
        raise ValueError("Дата народження в майбутньому")

    days = (today - birth_date).days

    return {
        "років": round(days / 365.25, 1),
        "місяців": round(days / 30.437, 0),
        "тижнів": days // 7,
        "днів": days,
        "годин": days * 24,
        "хвилин": days * 24 * 60,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Калькулятор віку в різних одиницях")
    parser.add_argument("--year", type=int, required=True, help="Рік народження")
    parser.add_argument("--month", type=int, required=True, help="Місяць (1-12)")
    parser.add_argument("--day", type=int, required=True, help="День")
    args = parser.parse_args()

    try:
        bd = date(args.year, args.month, args.day)
        units = calculate_age_units(bd)

        print(f"\nТобі виповнилося приблизно:")
        for unit, value in units.items():
            if unit == "років":
                print(f"  {value:>8.1f} {unit}")
            else:
                print(f"  {value:>8,.0f} {unit}")
    except ValueError as e:
        print(f"Помилка: {e}")
