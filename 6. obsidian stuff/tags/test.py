import os

# assign directory
directory = 'gen'
 
# iterate over files in
# that directory
for root, dirs, files in os.walk(directory):
    for filename in files:
        raw_name = filename[:-3]
        blah = f'''---
BC-dataview-note:: "[[{raw_name}]]"
BC-dataview-note-field:: down
---
```dataview
list from [[]]
```
'''
        with open(os.path.join(root, filename),'r') as file:
            data = file.read()
            data = data[93+len(raw_name):]

        with open(os.path.join(root, filename), 'w') as file:
            file.write(data)
