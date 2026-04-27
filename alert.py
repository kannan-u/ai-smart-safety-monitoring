import requests

def send_alert():
    try:
        response = requests.get("http://127.0.0.1:8000/alert")
        print("Alert sent:", response.json())
    except Exception as e:
        print("Error sending alert:", e)