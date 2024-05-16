import calendar

def display_calendar(year, month):
    # Krijo një objekt kalendar për vitin dhe muajin e caktuar
    cal = calendar.monthcalendar(year, month)

    # Shfaq kalendarin për muajin dhe vitin e dhënë
    print(calendar.month_name[month], year)
    print(" Mon Tue Wed Thu Fri Sat Sun")
    for week in cal:
        for day in week:
            if day == 0:
                print("    ", end="")
            else:
                print(f"{day:3} ", end="")
        print()

def main():
    print("Mirësevini në aplikacionin kalendar!")
    year = int(input("Shkruani vitin (p.sh., 2024): "))
    month = int(input("Shkruani numrin e muajit (1-12): "))

    # Kontrolloni nëse input-i është në rangun e vlefshmërisë
    if month < 1 or month > 12:
        print("Numri i muajit është i pavlefshëm.")
        return

    # Shfaqni kalendarin për vitin dhe muajin e dhënë
    display_calendar(year, month)

if __name__ == "__main__":
    main()
