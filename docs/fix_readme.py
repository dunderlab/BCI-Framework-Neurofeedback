import os

with open('../README.md', 'r') as file:
    content = file.read()
content = content.replace(
    'images/', 'https://github.com/dunderlab/neurofeedback/blob/master/docs/source/notebooks/images/')
with open('../README.md', 'w') as file:
    file.write(content)
