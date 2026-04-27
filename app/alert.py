import requests

def send_alert():
    try:
        requests.get("http://127.0.0.1:8000/alert")
    except:
        print("⚠️ Alert API not running")