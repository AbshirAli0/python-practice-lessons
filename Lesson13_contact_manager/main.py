import json
from rich.table import Table
from rich.console import Console

#first section


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