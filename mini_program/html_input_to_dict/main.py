import json
import re

def write_to_json(data:dict):
    with open(file='data.json', mode='w') as file:
        json.dump(obj=data,fp=file,indent=4)

def html_input_to_dict(html: str = '') -> dict:
    # find all attributes with optional values
    matches = re.findall(r'(\w+)(?:="([^"]*)")?', html)
    return {k: (v if v else True) for k, v in matches}

# print(html_input_to_dict('<input type="text" placeholder="type filename" name="filename" id="filename" required>'))
# write_to_json(data=html_input_to_dict('<input type="text" placeholder="typing filename" name="filename" id="filename" required>'))