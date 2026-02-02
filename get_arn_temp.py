import json
import subprocess

try:
    # Run AWS CLI command to get connections
    result = subprocess.run(
        ["aws", "codestar-connections", "list-connections", "--provider-type-filter", "GitHub", "--no-cli-pager"],
        capture_output=True,
        text=True
    )
    data = json.loads(result.stdout)
    
    found_arn = ""
    for conn in data.get('Connections', []):
        if conn['ConnectionName'] == 'MyGitHubConnection':
            found_arn = conn['ConnectionArn']
            break
    
    # Fallback to first one
    if not found_arn and data.get('Connections'):
        found_arn = data['Connections'][0]['ConnectionArn']
        
    print(found_arn)
    
except Exception as e:
    print(f"Error: {e}")
