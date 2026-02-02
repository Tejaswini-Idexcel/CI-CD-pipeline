import json

try:
    with open('stack_resources.json', 'r', encoding='utf-16') as f:
        data = json.load(f)
except:
    with open('stack_resources.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

for resource in data.get('StackResources', []):
    if resource['LogicalResourceId'] == 'PipelineArtifactBucket':
        print(resource['PhysicalResourceId'])
        break
