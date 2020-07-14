import os

for file in os.listdir("/home/busterdancy/Documents/Programming/Python Stuff"):
    if file.startswith("search"):
        print(os.path.join("/home/busterdancy/Documents/Programming/Python Stuff", file))
for file in os.listdir("/home/busterdancy/Documents/Programming/Python Stuff"):
    if file.startswith("late"):
        print(os.path.join("/home/busterdancy/Documents/Programming/Python Stuff", file))