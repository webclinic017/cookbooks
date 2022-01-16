import requests

def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandboxc8d1af8b9f27413da5f2bd5b5063ec98.mailgun.org/messages",
		auth=("api", "0ec62a675e80446d6c8f615d298a5691-7b8c9ba8-0c1d86db"),
		data={"from": "Mailgun Sandbox <postmaster@sandboxc8d1af8b9f27413da5f2bd5b5063ec98.mailgun.org>",
			"to": "Timon Kramer <laurin.kraemer@protonmail.com>",
			"subject": "Hello Timon Kramer",
			"text": "Congratulations Timon Kramer, you just sent an email with Mailgun!  You are truly awesome!"})

send_simple_message()