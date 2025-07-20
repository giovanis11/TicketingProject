from ticket_system import TicketSystem, Issuer, Resolver
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    system = TicketSystem()

    while True:
        clear_console()
        print("Welcome to the Software Support Ticketing Platform")
        print("1. Login as Ticket Issuer")
        print("2. Login as Ticket Resolver")
        print("3. Exit")
        choice = input("Select option: ").strip()

        if choice == '1':
            username = input("Enter your username: ").strip()
            user = Issuer(username)
            issuer_menu(system, user)
        elif choice == '2':
            username = input("Enter your username: ").strip()
            user = Resolver(username)
            resolver_menu(system, user)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Press Enter to continue.")
            input()

def issuer_menu(system, issuer):
    while True:
        clear_console()
        print(f"Logged in as Ticket Issuer: {issuer.username}")
        print("1. Issue a ticket")
        print("2. View my tickets")
        print("3. Logout")
        choice = input("Select option: ").strip()

        if choice == '1':
            title = input("Title: ").strip()
            description = input("Description: ").strip()
            print("Categories: Bug, Feature Request, General")
            category = input("Category: ").strip()
            if category not in ['Bug', 'Feature Request', 'General']:
                print("Invalid category. Press Enter to continue.")
                input()
                continue
            ticket = system.issue_ticket(title, description, category, issuer.username)
            print(f"Ticket issued with ID: {ticket.ticket_id}")
            input("Press Enter to continue...")
        elif choice == '2':
            tickets = system.list_tickets_by_issuer(issuer.username)
            if not tickets:
                print("You have no tickets.")
            else:
                for t in tickets:
                    print(t)
                    print("-" * 40)
            input("Press Enter to continue...")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Press Enter to continue.")
            input()

def resolver_menu(system, resolver):
    while True:
        clear_console()
        print(f"Logged in as Ticket Resolver: {resolver.username}")
        print("1. View open tickets")
        print("2. Resolve a ticket")
        print("3. Logout")
        choice = input("Select option: ").strip()

        if choice == '1':
            tickets = system.list_open_tickets()
            if not tickets:
                print("No open tickets.")
            else:
                for t in tickets:
                    print(t)
                    print("-" * 40)
            input("Press Enter to continue...")
        elif choice == '2':
            try:
                ticket_id = int(input("Enter the ticket ID to resolve: ").strip())
            except ValueError:
                print("Invalid ticket ID. Press Enter to continue.")
                input()
                continue
            ticket = system.find_ticket_by_id(ticket_id)
            if not ticket:
                print("Ticket not found. Press Enter to continue.")
                input()
                continue
            if ticket.status == 'Resolved':
                print("Ticket already resolved. Press Enter to continue.")
                input()
                continue
            message = input("Enter a message for the issuer: ").strip()
            success = system.resolve_ticket(ticket_id, resolver.username, message)
            if success:
                print("Ticket resolved successfully.")
            else:
                print("Failed to resolve ticket.")
            input("Press Enter to continue...")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Press Enter to continue.")
            input()

if __name__ == "__main__":
    main()
