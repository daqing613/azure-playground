#!/usr/bin/env python
# coding=utf-8

import os
import time
import openai

openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = "2023-05-15"
openai.api_key = os.getenv("AZURE_OPENAI_KEY")

ncount = 0
while True:

    # Get list of available models
    model_list = openai.Model.list()
    print(type(model_list))
    time.sleep(5)
    ncount += 1
    print(ncount)