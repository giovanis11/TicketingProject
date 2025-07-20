class Ticket:
    def __init__(self, ticket_id, title, description, category, issuer):
        self.ticket_id = ticket_id
        self.title = title
        self.description = description
        self.category = category
        self.issuer = issuer
        self.status = 'Open'
        self.resolver = None
        self.resolver_message = None  

    def resolve(self, resolver, message):
        self.status = 'Resolved'
        self.resolver = resolver
        self.resolver_message = message

    def __str__(self):
        resolved_by = f" (Resolved by {self.resolver})" if self.status == 'Resolved' else ""
        message = f"\n   Message from resolver: {self.resolver_message}" if self.resolver_message else ""
        return (f"[#{self.ticket_id:03}] {self.title} "
                f"({self.category}) - {self.status}{resolved_by}{message}")
