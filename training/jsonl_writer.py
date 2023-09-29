import json

jsonl = ""

with open('email_descriptions.json', 'r') as f:
	content = json.loads(f.read())

for completion, prompt in content:
	completion = completion.strip()
	prompt = prompt.strip()

	jsonl += json.dumps({"prompt": prompt, "completion": completion}) + '\n'

with open('training_data.jsonl', 'w') as f:
	f.write(jsonl)