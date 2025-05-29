from attackcti import attack_client


client = attack_client()


enterprise = client.get_enterprise()


keyword = "phishing"


filtered_techniques = [
    technique for technique in enterprise['techniques']
    if keyword.lower() in technique['name'].lower() or
       keyword.lower() in technique.get('description', '').lower()
]


for tech in filtered_techniques:
    print(f"{tech['external_references'][0]['external_id']} - {tech['name']}")
