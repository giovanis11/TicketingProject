import datetime

class Ticket:

  STAT_OPEN = "Open"
  STAT_RESOLVED = "Resolved"
  
  def __init__(self, ticket_id: int, title: str, description:str , category:str, issuer_username:str):
      self.ticket_id = ticket_id
      self.title = title
      self.description = description
      self.category = category.capitalize() or "Other"
      
      self.issuer_username = issuer_username
      self.created_at = datetime.now()

      self.status = "Open"
      self.resolved_by = None
      self.resolve_at = None

  def resolve(self, resolver_username):
    self.status = "Resolved"
    self.resolved_by = resolver_name
    self.resolved_at = datetime.datetime.now()

  def __str__(self):
    return(f"Ticket ID: {self.ticket_id} | Title: {self.title} | Category: {self.category}"
          f"Status: {self.status} | Issuer: {self.issuer} | Created: {self.created_at.strftime('%d-%m-%Y %H:%M)}
