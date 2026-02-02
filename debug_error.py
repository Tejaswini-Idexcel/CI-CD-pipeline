import json

try:
    with open('pipeline_error.json', 'r', encoding='utf-16') as f:
        data = json.load(f)
except:
    with open('pipeline_error.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

for stage in data.get('stageStates', []):
    name = stage['stageName']
    latest_exec = stage.get('latestExecution', {})
    state = latest_exec.get('status', 'UNKNOWN')
    print(f"Stage: {name} - {state}")
    
    if state == 'Failed' or True: # Print details for all for context
        for action in stage.get('actionStates', []):
            latest = action.get('latestExecution', {})
            print(f"  Action: {action['actionName']} - {latest.get('status')}")
            if latest.get('status') == 'Failed':
                print(f"  Summary: {latest.get('summary')}")
                print(f"  Details: {latest.get('errorDetails', {}).get('message')}")
