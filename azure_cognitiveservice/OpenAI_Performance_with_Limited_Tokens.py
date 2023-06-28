import openai
import time
import os

openai.api_key = "xxxxxxxxxxxxxxx"
openai.api_base = "https://xxxxx.openai.azure.com/" # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = 'azure'
openai.api_version = '2023-05-15' # this may change in the future

deployment_name='gpt3' #This will correspond to the custom name you chose for your deployment when you deployed a model. 


# Set up the prompt and length of completions
prompt = "爱情心理学"
lengths = [10, 20, 50]

try:
    # Loop through the lengths and generate completions
    for length in lengths:
        start_time = time.time()
        response = openai.Completion.create(
            engine=deployment_name,
            prompt=prompt,
            max_tokens=length
        )
        completion = response.choices[0].text.strip()
        end_time = time.time()
        execution_time = end_time - start_time

        # Print the completion and execution time
        print(f"Completion length: {length}")
        print(f"Completion: {completion}")
        print(f"Execution time: {execution_time} seconds")
        
except Exception as e:
    print(e)
