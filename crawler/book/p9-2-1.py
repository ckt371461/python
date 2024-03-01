import requests
def send_simple_message(title,body):
	return requests.post(
		"https://api.mailgun.net/v3/sandbox15e7fc737e2f48d4b9fda5ec87c1bdc8.mailgun.org/messages",
		auth=("api", "e48db7b2db4e5acdf5a4c8d7a6a76c52-48c092ba-ccde8a9f"),
		data={"from": "Excited User <cktim371461@gmail.com>",
			"to": ["cktim371461@gmail.com"],
			"subject": "{}".format(title),
			"text": "{}".format(body)})
send_simple_message('信件主旨','通知內容')