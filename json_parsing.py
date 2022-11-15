import json

string_as_json_format = '{"json_text": "https://gist.github.com/KotovVitaliy/83e4eeabdd556431374dfc70d0ba9d37"}'
obj = json.loads(string_as_json_format)
print(obj['json_text'])