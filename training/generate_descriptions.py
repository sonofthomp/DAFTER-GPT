import openai
import json
import time
import os

openai.organization = os.environ.get('OPENAI_ORG')
openai.api_key = os.environ.get('OPENAI_PWD')

emails = json.loads(open('emails.json', 'r').read())
descriptions = []

for index, email in enumerate(emails):
	if email.count(' ') < 15: # ignore shorter emails
		continue

	description = openai.ChatCompletion.create(
		model="gpt-3.5-turbo", 
		messages=[
			{
				"role": "user",
				"content": f'''
								I am trying to train an AI to write emails for me.
								The AI will be given a brief description of the email the user wants to write.
								For example, the user might tell the AI:

								"Ask my computer science teacher, Mr. DW, if he had seen the black coat that I left in his classroom, room 307, during my computer graphics class. Explain that I checked the lost and found but didn't find it."

								And the AI should respond with something like:

								"Hi DW,

								I left my black coat in 307 yesterday during 10th period graphics.

								I talked with the CS Dojo senseis who occupied the room that afternoon, and they said that they put my coat on the table/metal box thing next to the door and left it there after the end of dojo.

								Assuming that the custodians didn't move it to the lost and found (which, having checked the lost and found, seems unlikely) and that it wasn't stolen, I believe my coat might have stayed there overnight.

								Did you happened to see my black coat today in 307?"

								On the next line, I will give you an email that I wrote. Your job is to tell me a prompt that could generate this response. Make sure that the prompt is specific but short in length. Make sure the prompt is in the same style as the prompt I listed above, and make sure that the prompt is in first-person POV.
								{email}
							'''
			}
		]
	)
	description = description['choices'][0]['message']['content']
	descriptions.append([email, description])
	email = email[1:50].replace('\n', ' ').replace('\r', '')
	description = description.replace('\n', ' ')

	print(f'Finished #{index} / {len(emails)}')

with open('email_descriptions.json', 'w') as f:
	f.write(json.dumps(emails, indent=4))