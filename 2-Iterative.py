# Iterative Prompt Develelopment
# In this lesson, you'll iteratively analyze and refine your prompts to generate marketing copy from a product fact sheet.


## Setup
#### Load the API key and relevant Python libaries.
# In this course, we've provided some code that loads the OpenAI API key for you.

import openai

openai.api_key = "OPENAI_API_KEY"

#### helper function
# Throughout this course, we will use OpenAI's `gpt-3.5-turbo` model and the [chat completions endpoint](https://platform.openai.com/docs/guides/chat). 

# This helper function will make it easier to use prompts and look at the generated outputs:

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=1, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


## Generate a marketing product description from a product fact sheet
fact_sheet_chair = """
OVERVIEW
- Part of a beautiful family of mid-century inspired office furniture, 
including filing cabinets, desks, bookcases, meeting tables, and more.
- Several options of shell color and base finishes.
- Available with plastic back and front upholstery (SWC-100) 
or full upholstery (SWC-110) in 10 fabric and 6 leather options.
- Base finish options are: stainless steel, matte black, 
gloss white, or chrome.
- Chair is available with or without armrests.
- Suitable for home or business settings.
- Qualified for contract use.

CONSTRUCTION
- 5-wheel plastic coated aluminum base.
- Pneumatic chair adjust for easy raise/lower action.

DIMENSIONS
- WIDTH 53 CM | 20.87”
- DEPTH 51 CM | 20.08”
- HEIGHT 80 CM | 31.50”
- SEAT HEIGHT 44 CM | 17.32”
- SEAT DEPTH 41 CM | 16.14”

OPTIONS
- Soft or hard-floor caster options.
- Two choices of seat foam densities: 
 medium (1.8 lb/ft3) or high (2.8 lb/ft3)
- Armless or 8 position PU armrests 

MATERIALS
SHELL BASE GLIDER
- Cast Aluminum with modified nylon PA6/PA66 coating.
- Shell thickness: 10 mm.
SEAT
- HD36 foam

COUNTRY OF ORIGIN
- Italy
"""

prompt = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

Technical specifications: ```{fact_sheet_chair}```
"""
response = get_completion(prompt)
print(response)


## Issue 1: The text is too long 
#- Limit the number of words/sentences/characters.

# prompt = f"""
# Your task is to help a marketing team create a 
# description for a retail website of a product based 
# on a technical fact sheet.

# Write a product description based on the information 
# provided in the technical specifications delimited by 
# triple backticks.

# Use at most 50 words.

# Technical specifications: ```{fact_sheet_chair}```
# """
# response = get_completion(prompt)
# print(response)


## Issue 2. Text focuses on the wrong details
# - Ask it to focus on the aspects that are relevant to the intended audience.

# prompt = f"""
# Your task is to help a marketing team create a 
# description for a retail website of a product based 
# on a technical fact sheet.

# Write a product description based on the information 
# provided in the technical specifications delimited by 
# triple backticks.

# The description is intended for furniture retailers, 
# so should be technical in nature and focus on the 
# materials the product is constructed from.

# Use at most 50 words.

# Technical specifications: ```{fact_sheet_chair}```
# """
# response = get_completion(prompt)
# print(response)

# prompt = f"""
# Your task is to help a marketing team create a 
# description for a retail website of a product based 
# on a technical fact sheet.

# Write a product description based on the information 
# provided in the technical specifications delimited by 
# triple backticks.

# The description is intended for furniture retailers, 
# so should be technical in nature and focus on the 
# materials the product is constructed from.

# At the end of the description, include every 7-character 
# Product ID in the technical specification.

# Use at most 50 words.

# Technical specifications: ```{fact_sheet_chair}```
# """
# response = get_completion(prompt)
# print(response)

## Issue 3. Description needs a table of dimensions
# - Ask it to extract information and organize it in a table.

# prompt = f"""
# Your task is to help a marketing team create a 
# description for a retail website of a product based 
# on a technical fact sheet.

# Write a product description based on the information 
# provided in the technical specifications delimited by 
# triple backticks.

# The description is intended for furniture retailers, 
# so should be technical in nature and focus on the 
# materials the product is constructed from.

# At the end of the description, include every 7-character 
# Product ID in the technical specification.

# After the description, include a table that gives the 
# product's dimensions. The table should have two columns.
# In the first column include the name of the dimension. 
# In the second column include the measurements in inches only.

# Give the table the title 'Product Dimensions'.

# Format everything as HTML that can be used in a website. 
# Place the description in a <div> element.

# Technical specifications: ```{fact_sheet_chair}```
# """

# response = get_completion(prompt)
# print(response)