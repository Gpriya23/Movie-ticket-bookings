# Movie-ticket-bookings
class TicketBooking:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.available_seats = list(range(1, total_seats + 1))
        self.booked_tickets = {}

    def display_menu(self):
        print("\n1. View Available Seats")
        print("2. Book Ticket")
        print("3. View My Tickets")
        print("4. Exit")

    def view_available_seats(self):
        print("\nAvailable Seats:", self.available_seats)

    def book_ticket(self, user_name):
        if not self.available_seats:
            print("No seats available.")
            return
        seat = self.available_seats.pop(0)
        if user_name in self.booked_tickets:
            self.booked_tickets[user_name].append(seat)
        else:
            self.booked_tickets[user_name] = [seat]
        print(f"Ticket booked! Seat number: {seat}")

    def view_my_tickets(self, user_name):
        tickets = self.booked_tickets.get(user_name, [])
        print(f"\n{user_name}'s Tickets: {tickets if tickets else 'No tickets booked.'}")

    def main(self):
        user_name = input("Enter your name: ")
        while True:
            self.display_menu()
            choice = input("\nEnter your choice: ")
            if choice == "1":
                self.view_available_seats()
            elif choice == "2":
                self.book_ticket(user_name)
            elif choice == "3":
                self.view_my_tickets(user_name)
            elif choice == "4":
                print("Thank you for using the Ticket Booking System!")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    system = TicketBooking(total_seats=10)
    system.main()
