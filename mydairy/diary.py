#!/usr/bin/env python
import datetime
import sys
import os
from collections import OrderedDict

from peewee import *

# Init sqlite database
db = SqliteDatabase('diary.db')

# Create database model
class BaseModel(Model):
    class Meta:
        database = db # Init diary.db

class Entry(BaseModel):
    # Table fields
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)


# Create database and table if they dont exist
def initialize():
    db.connect()
    db.create_tables([Entry], safe=True)


# Func for clear display
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Display menu options
def menu_loop():
    """Show the menu"""
    choice = None

    while choice != 'q':
        clear()
        print("Enter 'q' to quit")
        for key, value in menu.items():
            print(f"{key}) {value.__doc__}")
        choice = input('Action: ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()


# Adds entries to database
def add_entry():
    """Add an entry."""
    print("Enter your entry. Press ctrl+d when finished")
    data = sys.stdin.read().strip()

    if data:
        if input('Save entry? [y/n]').lower() != 'n':
            Entry.create(content=data)
            print("Saved successfully!")


# Selects all entries from database
def view_entries(search_query=None):
    """View previous entries."""
    entries = Entry.select().order_by(Entry.timestamp.desc())
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))

    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %H:%M')
        clear()
        print(timestamp)
        print('='*len(timestamp))
        print(entry.content)
        print('\n\n'+ '='*len(timestamp ))
        print("n) next entry" )
        print("d) delete entry")
        print("q) return to main menu")

        next_action = input("Action: [n/d/q]  ").lower().strip()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)


# Searches entries by the query 
def search_entries():
    """Search entries for a string."""
    view_entries(input('Search query: '))


# Deletes model/table-row instance
def delete_entry(entry):
    """Delete an entry."""
    if input("Are you sure? [y/n] ").lower() == 'y':
        entry.delete_instance()
        print("Entry deleted!")


# Creates order dict
menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries),
])


# Script runs directly
if __name__ == '__main__':
    initialize()
    menu_loop()
