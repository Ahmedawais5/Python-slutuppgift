from datetime import datetime 
## KLASSER ##
class customer:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone 
        self.email = email
        self.interactions = []
        self.last_interaction = None

    def add_interaction(self, interaction):
         # Få nuvarande datum och tid
        current_time = datetime.now()

        # Lägger till interaktionen i listan (med datum och tid)
        self.interactions.append((interaction, current_time))

        # Uppdatera senaste interaktion till nuvarande tid
        self.last_interaction = current_time
       
        # Hur många dagar som gått sedan senaste interaktionen.
        # Return antalet dagar eller None om ingen interaktion har gjorts.
    def calculate_days_since_last_interaction (self):
        if self.last_interaction is None:
            return None
        
        # Skillnaden mellan senaste interaktionen och nutid
        diffrence= datetime.now() - self.last_interaction
        return diffrence.days


customer = customer("Ahmed Awais", "Ahmedawaiis@hotmail.com", "0762133117")
print(f"Kundens namn: {customer.name}")
print(f"Antal dagar sedan senaste interaktion: {customer.calculate_days_since_last_interaction()}")  # Borde vara None

print("lägger till en interaktion: Gillat inlägg")
customer.add_interaction("Gillat ett inlägg")
print(f"Senaste interaktion: {customer.last_interaction}")


days = customer.calculate_days_since_last_interaction()

print(f"Antal dagar sedan senaste interaktion: {days}")  # Bör vara 0 om samma dag       
        