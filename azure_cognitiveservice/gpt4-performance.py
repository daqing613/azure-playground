#!/usr/bin/env python
# coding=utf-8

import os
import time
import openai
import asyncio


openai.api_type = "azure"
openai.api_base = "https://wptest005.openai.azure.com/"
openai.api_version = "2023-05-15"
openai.api_key = "72ca8644ddda4d8c80f90e9bf3d54cc0"

print(openai.api_key)
print(openai.api_base)

async def make_request():
    try:
        response = await loop.run_in_executor(None, lambda: openai.ChatCompletion.create(
            engine="gpt4-8k",
            messages=[{"role":"user","content":"爱情心理学， 要求1万字"}],
            max_tokens=166,
            stop=None
        ))
        print(response)
    except Exception as e:
        print(f"Exception occurred: {e}")

async def run_requests():
    count = 0
    while True:
        start_time = time.time()
        tasks = [asyncio.create_task(make_request()) for _ in range(1)]
        await asyncio.gather(*tasks)
        end_time = time.time()
        execution_time = end_time - start_time
        count += 8
        print(f"Execution time: {execution_time} seconds")
        print(f"Count Number: {count}")
        print("Wait for 1 second")
        await asyncio.sleep(1)  # Wait for 1 second before making the next set of requests


loop = asyncio.get_event_loop()
loop.run_until_complete(run_requests())