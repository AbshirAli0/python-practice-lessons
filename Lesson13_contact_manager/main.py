import json
from rich.table import Table
from rich.console import Console

contacts = [
    {"name": "Abshir", "phone": "111-222-3333", "tags": {"friend", "gym"}}
]

#add contact
new_contact = {"name": "Joe", "phone": "222-344-5666", "tags": {"co-worker", "work"}}
contacts.append(new_contact)

#update
for c in contacts:
    if c["name"] == "Abshir":
        c["name"] = "Bob"

#delete
contacts = [c for c in contacts if c["name"] != "Bob"]

#create a table
console = Console()
table = Table(title = "Contact List")

table.add_column("Name", style="cyan")
table.add_column("Phone #", style="magenta")
table.add_column("Tags", style="green")

for c in contacts:
    table.add_row(c["name"], c["phone"], ", ".join(c["tags"]))
console.print(table)



#second section


# load contacts from Json

try:
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    contacts = []

# add CRUD Function
contacts = []

def add_contacts(contacts, name, phone, tags):
    contacts.append({
        "name": name, 
        "phone": phone, 
        "tags": tags})

# Read CRUD Function

def read_contacts(contacts):
    console = Console()
    table = Table(title = "2nd Contact List")

    table.add_column("Name", style="cyan")
    table.add_column("Phone #", style="magenta")
    table.add_column("Tags", style="green")

    for c in contacts:
        table.add_row(c["name"], c["phone"], ", ".join(c["tags"]))
    console.print(table)


# Update CRUD Function

def update_contacts(contacts, old_name, new_name = None, new_phone = None, new_tags = None):
    for c in contacts:
        if c["name"] == old_name:
            if new_name:
                c["name"] = new_name
            if new_phone:
                c["phone"] = new_phone
            if new_tags:
                c["tags"] =  set(new_tags) 
            return

# Delete CRUD Function

def del_contacts(contacts, name):
    return [c for c in contacts if c["name"] != name ]


# Call Functions

add_contacts(contacts, "Mike","333-555-7777", ["friend", "school"])

add_contacts(contacts, "Michelle","932-483-5437", ["friend", "school"])

add_contacts(contacts, "Sarah","453-321-7227", ["friend", "school"])



update_contacts(contacts, old_name="Mike", new_name="Kevin", new_phone="455-556-6678", new_tags={"friend", "school"} )


contacts = del_contacts(contacts, "Sarah")

read_contacts(contacts)


# Save contacts

json_ready = []
for c in contacts:
    json_ready.append({
        "name": c["name"],
        "phone": c["phone"],
        "tags": list(c["tags"])
    })

with open("contacts.json", "w") as f:
    json.dump(json_ready, f, indent = 100)


# 2nd Quesiton - Grocery List Manager

# Basic Crud
groceries = [ {
            "name": "cereal", 
            "price": 3.50, 
            "meal": "Breakfast"
                }
             ]
          
             
#create
groceries.append( {"name": "burgers", "price": 4.0, "meal": "lunch"})
groceries.append( {"name": "pasta", "price": 2.0, "meal": "Dinner"})

#update
for g in groceries:
    if g["name"] == "burgers":
        g["price"] = 2.5 



#delete

groceries = [g for g in groceries if g["name"] != "pasta"]

#read

console = Console()
table = Table(title = "Groceries list")

table.add_column("name", style="cyan")
table.add_column("price", style="magenta")
table.add_column("meal", style="green")

for g in groceries:
    table.add_row(g["name"], str(g["price"]), g["meal"])

#console.print(table)

# Reusable crud

#create

def add_groceries(groceries, name, price, meal):
    groceries.append({
        "name": name,
        "price": price,
        "meal": meal
    })

#Update

def update_groceries(groceries, old_name, new_name = None, new_price = None, new_meal = None):
    for g in groceries:
        if g["name"] == old_name:
            if new_name:
                g["name"] = new_name
            if new_price is not None:
                g["price"] = new_price
            if new_meal:
                g["meal"] = new_meal
            return 
        

# delete
def del_groceries(groceries, name):
    return [g for g in groceries if g["name"] != name ]

    
def read_groceries(groceries) :

    console = Console()
    table = Table(title = "REUSABLE Groceries list")

    table.add_column("name", style="cyan")
    table.add_column("price", style="magenta")
    table.add_column("meal", style="green")

    for g in groceries:
        table.add_row(g["name"], str(g["price"]), g["meal"])

    console.print(table)

    
add_groceries(groceries, "Fish", 3.00, "Dinner")
update_groceries(groceries, "Fish", new_name = "Salmon", new_price=2.25, new_meal="Lunch")
update_groceries(groceries, "cereal", new_price=2.20)
groceries = del_groceries(groceries, "burgers")
read_groceries(groceries)
