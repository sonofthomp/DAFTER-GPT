import mailbox
import json
import sys
import re

if len(sys.argv) >= 2:
	PATH = sys.argv[1]
else:
	PATH = './Sent.mbox'

mb = mailbox.mbox(PATH)
num_emails = 0
emails = []

def is_footer(text):
	# I really need to learn regex
	words = text.split(' ')

	if words[0] != 'On':
		return False

	if not(words[1] in ['Sun,', 'Mon,', 'Tue,', 'Wed,',
						'Thu,', 'Fri,', 'Sat,']):
		return False

	if not(words[2] in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
						'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']):
		return False

	if not((len(words[3]) >= 2) and (words[3][:-1].isnumeric())):
		return False

	if not((len(words[4]) == 4) and (words[4].isnumeric())):
		return False

	if not(words[5] == 'at'):
		return False

	if len(words[6].split(':')) != 2:
		return False

	if not(words[7] in ['AM', 'PM']):
		return False

	return True

decoders = {
	'=E2=80=9C': '"',
	'=E2=80=9D': '"',
	'=E2=80=99': '"',
	'=E2=80=93': '–',
	'=E2=80=94': '.',
	'=E2=80=97': '*',
	'=E2=88=92': '.',
	'=E2=89=A4': '≤',
	'=E2=89=A5': '≥',
	'=E2=80=A2': '≥',
	'=C2=BA': 'º',
	'=3D': '-'
}

with open('email_descriptions.json', 'r') as f:
	email_descs = json.loads(f.read())

emails = []

for index in range(len(email_descs)):
	a, b = email_descs[index]
	body = a
	body = body.replace(' --=20 Gabriel Thompson gthompson30@stuy.edu https://www.gabe.biz/', '')
	re.sub(r'\s+', ' ', body)

	for key, replacement in decoders.items():
		body = body.replace(key, replacement)

	lines = body.split('\n')
	for index, line in enumerate(lines):
		if any([line.strip().startswith(i) for i in ['Resume:', '--']]):
			lines = lines[:index]
			break

	body = '\n'.join(lines)
	body = body.strip()

	b = b.strip()
	email_descs.append([body, b])


with open('email_descriptions.json', 'w') as f:
	f.write(json.dumps(email_descs, indent=4))