import json

try:
    with open('pipeline_state.json', 'r', encoding='utf-16') as f:
        data = json.load(f)
except:
    with open('pipeline_state.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

for stage in data.get('stageStates', []):
    name = stage['stageName']
    state = stage.get('latestExecution', {}).get('status', 'UNKNOWN')
    print(f"Stage: {name} - {state}")
    
    if state == 'Failed':
        for action in stage.get('actionStates', []):
            latest = action.get('latestExecution', {})
            if latest.get('status') == 'Failed':
                print(f"  Action: {action['actionName']} Failed")
                print(f"  Summary: {latest.get('summary')}")
                print(f"  Details: {latest.get('errorDetails', {}).get('message')}")
