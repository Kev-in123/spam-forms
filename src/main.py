import requests
import threading

def submit_form():
    while True:
        data = {}
        r = requests.post(
            url=
            "https://docs.google.com/forms/d/e/form-id/formResponse",
            data=str(data))
        print(r.status_code)

threads = []

for _ in range(50):
    t = threading.Thread(target=submit_form)
    t.daemon = True
    threads.append(t)

for _ in range(50):
    threads[_].start()

for _ in range(50):
    threads[_].join()
