
import os

# Read environment variable
api_key = os.getenv('MY_API_KEY')

# Check environment variable
if api_key:
    print("SUCCESS: Environment variable found!")
    print("Value:", api_key)
else:
    print("ERROR: Environment variable not found!")
import os

# for key, value in os.environ.items():
#     print(key, "=", value)