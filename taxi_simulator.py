from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = """
q)uit, c)hoose taxi,d)rive
"""


def list_display(taxis):
    for i, taxi in enumerate(taxis):
        print(f'{i} - {taxi}')


def main():
    """Write a simulator program to test out taxi and silver service taxi class """
    taxis = [Taxi("Honda", 100), SilverServiceTaxi("Toyota", 100, 3),
             Taxi("Huynhdai", 143), SilverServiceTaxi("Kia", 120, 2)]
    total_cost = 0
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    choice = input(">>>").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            list_display(taxis)
            taxi_option = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_option]
            except IndexError:
                print("Invalid taxi choice")
        elif choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance_drive = int(input("Drive how far? "))
                current_taxi.drive(distance_drive)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_cost += trip_cost
            else:
                print("You need to choose a taxi before you can drive!")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_cost:.2f}")
        print(MENU)
        choice = input(">>>").lower()


if __name__ == '__main__':
    main()
