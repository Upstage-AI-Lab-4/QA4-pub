import os

try:
    # 환경 변수-> UPSTAGE_API_KEY
    api_key = os.getenv("UPSTAGE_API_KEY")

    # api setup test 
    if api_key:
        print(f"API Key is set: {api_key}")
    else:
        print("API Key is not set.")

except Exception as e:
    print(f"An error occurred: {e}")

