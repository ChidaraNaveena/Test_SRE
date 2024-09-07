import os
import json
from datetime import datetime

def load_logs(directory, start_date, end_date):
    logs = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.log') or file.endswith('.0.log'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    for line in f:
                        try:
                            log_entry = json.loads(line)
                            log_date = datetime.strptime(log_entry['EventDateTime'], '%Y-%m-%d %H:%M:%S.%f')
                            if start_date <= log_date <= end_date:
                                logs.append(log_entry)
                        except json.JSONDecodeError:
                            continue
    return logs

def search_logs(logs, search_string):
    return [log for log in logs if search_string in json.dumps(log)]

# Example Usage
start_date = datetime(2024, 8, 6)
end_date = datetime(2024, 8, 7)
logs = load_logs('/path/to/logs', start_date, end_date)
search_results = search_logs(logs, 'Gateway Time-out')

for result in search_results:
    print(result)
