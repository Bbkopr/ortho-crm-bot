import os

print("===== ENV TEST =====")
print("TOKEN EXISTS:", "TOKEN" in os.environ)
print("TOKEN VALUE:", os.environ.get("TOKEN"))
print("====================")
