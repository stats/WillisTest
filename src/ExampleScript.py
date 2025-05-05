
from dotenv import load_dotenv
import os

load_dotenv()

debug_mode = os.getenv("TEST_MODE", False)
output_dir = os.getenv("OUTPUT_DIR", "/myoutput")
port = os.getenv("PORT", 3001)


print(f"TestMode : {debug_mode}\nOutput Dir: {output_dir}\nPort: {port}")

print("This script Works")