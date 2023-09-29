import openai
import os

openai.organization = os.environ.get('OPENAI_ORG')
openai.api_key = os.environ.get('OPENAI_PWD')

def get_completion(input_phrase, model='davinci:ft-personal-2023-05-08-17-18-25', length=600, num_choices=1):
    print('getting completion....')
    print(length)
    length = int(length)
    completion = openai.Completion.create(
        engine=model,
        prompt=input_phrase,
        temperature=0.51,
        max_tokens=length,
        top_p=1,
        best_of=3,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["Period", "period", 'https://', 'http://']
    )
    completion = completion['choices'][0]['text']    
    print('completion: ' + completion)

    return completion