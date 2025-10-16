import requests
import sys
import time

# The URL of the application to check
APP_URL = "http://localhost:8080"

# Maximum number of retries
MAX_RETRIES = 5

# Time to wait between retries (in seconds)
RETRY_INTERVAL = 5

def check_app_health():
    """Check if the deployed app is healthy."""
    print(f"Checking application health at {APP_URL}...\n")

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.get(APP_URL, timeout=5)
            
            # Check if response code is 200 (OK)
            if response.status_code == 200:
                print(f"✅ App is UP! (Status Code: {response.status_code})")
                return True
            else:
                print(f"⚠️ App responded with {response.status_code}. Retrying...")
        except requests.exceptions.RequestException as e:
            print(f"❌ Attempt {attempt}: App not reachable. Error: {e}")
        
        time.sleep(RETRY_INTERVAL)

    print("🚨 Application failed health check after multiple attempts.")
    return False


if __name__ == "__main__":
    healthy = check_app_health()
    if not healthy:
        sys.exit(1)  # Exit with error code so Jenkins marks the build as failed
