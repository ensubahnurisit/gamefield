from faker import Faker
import random

fake = Faker()

def generate_profile():
    return {
        "name": fake.name(),
        "birth_name": fake.name(),
        "clan": fake.word().title() + " Clan",
        "allegiance": random.choice(["Free Guilds", "Imperial Dominion", "Neutral Houses"]),
        "rank": random.choice(["Scout", "Captain", "Officer", "Seeker"]),
        "occupation": random.choice(["Pathfinder", "Enforcer", "Trader", "Hunter"])
    }

def generate_post():
    return fake.sentence()

def generate_answer():
    return fake.sentence()
