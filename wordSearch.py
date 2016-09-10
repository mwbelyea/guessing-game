import re
dir(re)

string = "Hi! My name is Mike. I'm learning how to build a search function with Python."

re.search("Mike", string)

m = re.search("Mike", string)

print(m)

start = m.start()
end = start + 4

print(start)
print(end)

string[start:end]