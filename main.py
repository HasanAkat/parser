import json

from resume_parser import resumeparse

data = resumeparse.read_file("DATA/00001.txt")

with open('data.json', 'w') as f:
    json.dump(data, f)