import json
from ticket import Ticket

class User:
    def __init__(self, username):
        self.username = username

class Issuer(User):
    def __init__(self, username):
        super().__init__(username)

class Resolver(User):
    def __init__(self, username):
        super().__init__(username)

class TicketSystem:
    def __init__(self):
        self.tickets = []
        self.next_id = 1
        self.load_tickets()

    def load_tickets(self):
        try:
            with open('tickets.json', 'r') as f:
                data = json.load(f)
                for item in data:
                    ticket = Ticket(
                        item['ticket_id'],
                        item['title'],
                        item['description'],
                        item['category'],
                        item['issuer']
                    )
                    ticket.status = item['status']
                    ticket.resolver = item['resolver']
                    ticket.resolver_message = item.get('resolver_message')
                    self.tickets.append(ticket)
                if self.tickets:
                    self.next_id = max(t.ticket_id for t in self.tickets) + 1
        except FileNotFoundError:
            pass

    def save_tickets(self):
        data = []
        for t in self.tickets:
            data.append({
                'ticket_id': t.ticket_id,
                'title': t.title,
                'description': t.description,
                'category': t.category,
                'issuer': t.issuer,
                'status': t.status,
                'resolver': t.resolver,
                'resolver_message': t.resolver_message
            })
        with open('tickets.json', 'w') as f:
            json.dump(data, f, indent=4)

    def issue_ticket(self, title, description, category, issuer):
        ticket = Ticket(self.next_id, title, description, category, issuer)
        self.tickets.append(ticket)
        self.next_id += 1
        self.save_tickets()
        return ticket

    def list_tickets_by_issuer(self, issuer_username):
        return [t for t in self.tickets if t.issuer == issuer_username]

    def list_open_tickets(self):
        return [t for t in self.tickets if t.status == 'Open']

    def find_ticket_by_id(self, ticket_id):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                return ticket
        return None

    def resolve_ticket(self, ticket_id, resolver_username, message):
        ticket = self.find_ticket_by_id(ticket_id)
        if ticket and ticket.status == 'Open':
            ticket.resolve(resolver_username, message)
            self.save_tickets()
            return True
        return False
