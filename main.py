from datetime import date

def age_in_units(birth_year, birth_month, birth_day):
    today = date.today()
    birth = date(birth_year, birth_month, birth_day)
    
    days_old = (today - birth).days
    if days_old < 0:
        return "Ти ще не народився :)"
    
    years = days_old // 365.25
    months = days_old // 30.44
    weeks = days_old // 7
    hours = days_old * 24
    minutes = hours * 60
    
    print(f"Тобі виповнилося:")
    print(f"  {years:.1f} років")
    print(f"  {months:,.0f} місяців")
    print(f"  {weeks:,.0f} тижнів")
    print(f"  {days_old:,.0f} днів")
    print(f"  {hours:,.0f} годин")
    print(f"  {minutes:,.0f} хвилин")


if __name__ == "__main__":
    print("Скільки тобі років у різних одиницях?\n")
    try:
        y = int(input("Рік народження: "))
        m = int(input("Місяць (1-12): "))
        d = int(input("День: "))
        age_in_units(y, m, d)
    except (ValueError, TypeError):
        print("Перевір введені дані")
