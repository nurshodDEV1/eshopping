import requests
def send_sms(phone_number,messsage):
    url = "http://notify.eskiz.uz/api/message/sms/send"

    payload={'mobile_phone': phone_number,
             'message':messsage,
             'from': '4546',
             'callback_url': 'http://0000.uz/test.php'}
    files=[

    ]
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9ub3RpZnkuZXNraXoudXpcL2FwaVwvYXV0aFwvbG9naW4iLCJpYXQiOjE2NDYyNTM3NzIsImV4cCI6MTY0ODg0NTc3MiwibmJmIjoxNjQ2MjUzNzcyLCJqdGkiOiJpV1NrTUJDUUN0RWJvbTZZIiwic3ViIjo1LCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.3o3zSgkR6egCLkrja47HK5nQBR3ByQ5rys6jar8W8zg'
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)
