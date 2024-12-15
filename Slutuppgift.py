from datetime import datetime, timedelta 
## KLASSER ##
class Customer:
    def __init__(self, name, email, phone ):
        self.name = name
        self.email = email
        self.phone = phone 
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
    
    def is_inactive(self, days=30):
        days_since = self.calculate_days_since_last_interaction()
        if days_since is None:
            return False
        return days_since > days


class CustomerDataSystem:
    def __init__(self, name):
        self.name = name
        self.customers = []       
    #Lägger till ny kund 
    def add_customer(self, name, email, phone):
        #Loppar igenom och kollar om eposten redan finns
        for customer in self.customers:
            if customer.email == email:
                ## Finns eposten redan kommer det här felmeddelnadet
                raise ValueError (f"Det här e-posten {email} finns redan.")
        new_customer = Customer(name, email, phone)
        self.customers.append(new_customer)
        print(f"{name} du är nu en ny kund!")

    #Tar bort en kund 
    def remove_customer(self, email):
        # Loopar igenom listan för att hitta kunden
        for customer in self.customers:
            if customer.email == email:
                self.customers.remove(customer)
                print(f"Kunden med epost {email} har nu tagits bort.")
                return
            # Felmeddelandet kommer upp om kund ej finns i listan
        raise KeyError (f"Kunden med epost{email} hittades inte.")
        
# Uppdaterar info på den kund
    def update_contact_info(self, name, email, new_email = None, new_phone = None):
        for customer in self.customers:
            if customer.email == email:
                if new_email: 
                    customer.email == new_email
                    print(f"{name}s epost har uppdaterats till {new_email}.")
                if new_phone:
                    customer.phone = new_phone
                    print(f"{name}s telefonnummer har uppdaterats till {new_phone}.")
                return
        raise KeyError (f"{name}s epost med {email} hittades inte.")

    def add_interaction_for_customer(self, email, interaction):
        
        for customer in self.customers:
            #print(f"Check {customer.email} är {email}.")
            if customer.email == email:
                customer.add_interaction(interaction)
                print(f"Interaktion {interaction} har lagts till för {email}.")
                return
        raise KeyError(f"Ingen kund med epost {email} hittades.")

    ## Hämtar alla interaktioner för en kund.
    def get_interactions_for_customer(self, email):
        
        for customer in self.customers:
            if customer.email == email:
                print(f"Interaktioner för kund med {email}:")
                ## Visar varje interaktion och när de gjordes
                for interaction, date in customer.interactions:
                    print(f" {interaction} datum: {date}")  
                return
        raise KeyError (f"Kundens email {email} hittades inte")

    def list_all_customers(self):
        
        # Skriver ut en lista över alla kunder i systemet.

        print(f"Alla kunder i systemet '{self.name}':")
        if not self.customers:
            print("Det finns inga kunder i systemet.")
        for customer in self.customers:
            print(f" Namn: {customer.name}, E-post: {customer.email}, Telefon: {customer.phone}")

    def list_inactive_customers(self, days=30):
        print (f"Kunder som har varit inatkiva i mer än {days} dagar.")
        found_inactive = False
        for customer in self.customers:
            if customer.is_inactive(days):
                days_since = customer.calculate_days_since_last_interaction()
                print(f"- Namn: {customer.name}, Dagar sedan senaste interaktion: {days_since}")
                found_inactive = True
        if not found_inactive: 
            print("Inga inaktiva kunder hittades.")


# Enkel användning av systemet
print("Skapar kundsystemet.")
system = CustomerDataSystem("AWAIS AB")

print("\nLägger till kunder.")
system.add_customer("Ahmed Awais", "Ahmedawaiis@hotmail.com", "0762133117")
system.add_customer("Gabriel Mousa", "GabrielMousa@hotmail.com", "0762137131")
try:
    system.add_customer("Gabriel Mousa", "GabrielMousa@hotmail.com", "0762137131")
except ValueError as e: 
    print(e)
print("\nVisar alla kunder:")
system.list_all_customers()

print("\nLägger till en interaktion för Ahmed")
system.add_interaction_for_customer("Ahmedawaiis@hotmail.com", "Gillat ett inlägg")

print("\nLägger till en gammal interaktion för Gabriel.")
system.add_interaction_for_customer("GabrielMousa@hotmail.com", "Besökt webbplats")
system.customers[1].last_interaction -= timedelta(days=31)

print("\nLista över inaktiva kunder:")
system.list_inactive_customers()

print("\nVisar Ahmeds interaktioner:")
system.get_interactions_for_customer("Ahmedawaiis@hotmail.com")

print("\nUppdaterar Gabriels kontaktinformation.")
system.update_contact_info("Gabriel Mousa", "GabrielMousa@hotmail.com", new_phone="07123456789")

print("\nTar bort Ahmed från kundlistan")
system.remove_customer("Ahmedawaiis@hotmail.com")

print("\nVisar alla kunder efter borttagning:")
system.list_all_customers()