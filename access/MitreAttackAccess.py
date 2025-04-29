from attackcti import attack_client

# Initialize the client
lift = attack_client()

# Fetch enterprise ATT&CK data
enterprise = lift.get_enterprise()

# Define your keyword
keyword = "phishing"

# Filter techniques by keyword in name or description
filtered_techniques = [
    technique for technique in enterprise['techniques']
    if keyword.lower() in technique['name'].lower() or
       keyword.lower() in technique.get('description', '').lower()
]

# Display filtered techniques
for tech in filtered_techniques:
    print(f"{tech['external_references'][0]['external_id']} - {tech['name']}")
