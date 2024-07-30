from pymongo import MongoClient
import datetime

# Connect to MongoDB
client = MongoClient('mongodb+srv://admin:admin@krishs.djn4o6k.mongodb.net/')
db = client['flight_status_db']
flights = db.flights
users = db.users

# Dummy flight data
flight_data = [
    {
        "flight_id": "6E 2341",
        "airline": "Indigo",
        "status": "On Time",
        "departure_gate": "A12",
        "arrival_gate": "B7",
        "scheduled_departure": datetime.datetime(2024, 7, 26, 14, 0, 0),
        "scheduled_arrival": datetime.datetime(2024, 7, 26, 18, 0, 0),
        "actual_departure": None,
        "actual_arrival": None
    },
    {
        "flight_id": "6E 2342",
        "airline": "Indigo",
        "status": "Delayed",
        "departure_gate": "C3",
        "arrival_gate": "D4",
        "scheduled_departure": datetime.datetime(2024, 7, 26, 16, 0, 0),
        "scheduled_arrival": datetime.datetime(2024, 7, 26, 20, 0, 0),
        "actual_departure": None,
        "actual_arrival": None
    },
    {
        "flight_id": "6E 2343",
        "airline": "Indigo",
        "status": "Cancelled",
        "departure_gate": "E2",
        "arrival_gate": "F1",
        "scheduled_departure": datetime.datetime(2024, 7, 26, 12, 0, 0),
        "scheduled_arrival": datetime.datetime(2024, 7, 26, 16, 0, 0),
        "actual_departure": None,
        "actual_arrival": None
    }
]

# Insert flight data
flights.drop()  # Clear existing collection
flights.insert_many(flight_data)

# Dummy user data with assigned flights
user_data = [
    {
        "username": "user1",
        "password": "password1",
        "assigned_flights": ["6E 2341"]
    },
    {
        "username": "user2",
        "password": "password2",
        "assigned_flights": ["6E 2342"]
    },
    {
        "username": "user3",
        "password": "password3",
        "assigned_flights": ["6E 2343"]
    }
]

# Insert user data
users.drop()  # Clear existing collection
users.insert_many(user_data)

print("Dummy data inserted successfully!")
