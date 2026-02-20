import json
import random
from faker import Faker

fake = Faker()

# Define our Engineering Firm's Business Units
units = ["Technical Training", "Informatics & IT", "Engineering Design", "Corporate Admin"]
priorities = ["Standard", "Urgent", "Critical"]

def generate_sample():
    unit = random.choice(units)
    priority = random.choice(priorities)
    name = fake.name()
    company = fake.company()
    
    # Templates for different professional services
    templates = {
        "Technical Training": [
            f"Hello, I'm {name} from {company}. We need a 3-day advanced Python workshop for 15 engineers next month.",
            f"Does your firm offer certifications in AI/ML? We are looking to upskill our data team. Regards, {name}."
        ],
        "Informatics & IT": [
            f"Our CRM is not syncing with our internal database. Can your IT team help with an API integration? Thanks, {name}.",
            f"We need a security audit for our cloud infrastructure at {company}. Please send a proposal."
        ],
        "Engineering Design": [
            f"We are looking for a structural engineer to review the blueprints for our new facility in {fake.city()}.",
            f"Hi, {name} here. We need a CAD specialist for a short-term mechanical design project."
        ],
        "Corporate Admin": [
            f"Please send the updated invoice for the January consulting services to {fake.email()}.",
            f"We would like to discuss a long-term partnership agreement with your firm. Who is the best person to contact?"
        ]
    }
    
    email_text = random.choice(templates[unit])
    
    # The "Ideal JSON" for the CRM to digest
    structured_data = {
        "sender": name,
        "organization": company,
        "assigned_unit": unit,
        "priority_level": priority,
        "summary": "Auto-generated summary of request" # The model will learn to summarize too!
    }
    
    return {
        "instruction": "Analyze the following service request. Classify it into a Business Unit, determine priority, and extract sender details in JSON format.",
        "input": email_text,
        "output": json.dumps(structured_data)
    }

# Generate 150 samples (a bit more for better variety)
dataset = [generate_sample() for _ in range(150)]

with open("data/train_data.jsonl", "w") as f:
    for entry in dataset:
        f.write(json.dumps(entry) + "\n")

print(f"Generated 150 diverse engineering service requests in data/train_data.jsonl")