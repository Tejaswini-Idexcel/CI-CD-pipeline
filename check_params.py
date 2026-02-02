import json

try:
    with open('stack_info.json', 'r', encoding='utf-16') as f:
        data = json.load(f)
except:
    with open('stack_info.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

parameters = data['Stacks'][0].get('Parameters', [])
token_present = any(p['ParameterKey'] == 'GitHubToken' for p in parameters)
print(f"GitHubToken Present: {token_present}")

for p in parameters:
    print(f"Key: {p['ParameterKey']}")
