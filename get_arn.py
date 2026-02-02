import json

try:
    with open('connections.json', 'r', encoding='utf-16') as f:
        data = json.load(f)
except:
    with open('connections.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

found_arn = ""
for conn in data.get('Connections', []):
    if conn['ConnectionStatus'] == 'AVAILABLE':
        found_arn = conn['ConnectionArn']
        break

# If no available, take the first one (likely pending)
if not found_arn and data.get('Connections'):
    found_arn = data['Connections'][0]['ConnectionArn']

with open('valid_arn.txt', 'w') as f:
    f.write(found_arn)
    
print(f"Saved: {found_arn}")
