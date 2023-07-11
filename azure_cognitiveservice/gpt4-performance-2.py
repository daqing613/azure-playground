#!/usr/bin/env python
# coding=utf-8

import time
import aiohttp
import asyncio



api_base = "https://xxxxxxxx.openai.azure.com/"
api_version = "2023-05-15"
api_key = "xxxxxx"

async def make_request():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://wptest005.openai.azure.com/openai/deployments/gpt4-8k/chat/completions?api-version=2023-05-15",
                headers={"api-key": api_key, "Content-Type": "application/json"},
                json={

                    "messages": [{"role": "user", "content": "爱情心理学，要求1万字"}],
                },
            ) as response:
                data = await response.json()
                print(data)
    except Exception as e:
        print(f"Exception occurred: {e}")

async def run_requests():
    count = 0
    while count < 11:
        start_time = time.time()
        await make_request()
        end_time = time.time()
        execution_time = end_time - start_time
        count += 1
        print(f"Execution time: {execution_time} seconds")
        print(f"Count Number: {count}")
        if count < 11:
            sleep_time = 10 / 11  # 10 seconds divided by number of requests
            print(f"Wait for {sleep_time} seconds")
            await asyncio.sleep(sleep_time)  # Wait for the calculated sleep time before making the next request


loop = asyncio.get_event_loop()
loop.run_until_complete(run_requests())