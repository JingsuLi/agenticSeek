# trace_parser.py
# early scaffolding — not tested

import json

def load_trace(path):
    with open(path, 'r') as f:
        return json.load(f)

def get_failures(trace_data):
    return [s for s in trace_data['steps'] if not s.get('success', True)]

if __name__ == "__main__":
    trace = load_trace('sample_trace.json')
    failures = get_failures(trace)
    print(f"Found {len(failures)} failed steps.")
