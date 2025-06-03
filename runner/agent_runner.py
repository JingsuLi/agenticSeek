# agent_runner.py
# scaffold — no real LLM calls yet

import yaml
import json
from datetime import datetime

def load_prompt(yaml_path):
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)
        return [step['prompt'] for step in data['steps']]

def mock_llm_call(prompt):
    return f"[mocked response] {prompt[:30]}..."

def run():
    prompts = load_prompt('../prompt_lab/basic_flow.yaml')
    trace = []

    for idx, p in enumerate(prompts):
        output = mock_llm_call(p)
        trace.append({
            "step": idx + 1,
            "input": p,
            "output": output,
            "success": True
        })

    with open(f"../trace_tools/trace_{datetime.now().isoformat()}.json", 'w') as f:
        json.dump({"steps": trace}, f, indent=2)

if __name__ == "__main__":
    run()
