import json

try:
    with open('pipeline_error.json', 'r', encoding='utf-16') as f:
        data = json.load(f)
except:
    with open('pipeline_error.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

failed_msg = "No failure found in JSON"

for stage in data.get('stageStates', []):
    for action in stage.get('actionStates', []):
        latest = action.get('latestExecution', {})
        if latest.get('status') == 'Failed':
            failed_msg = f"Action: {action['actionName']}\nSummary: {latest.get('summary')}\nDetails: {latest.get('errorDetails', {}).get('message')}"

with open('error_msg.txt', 'w') as f:
    f.write(failed_msg)
