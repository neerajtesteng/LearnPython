from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC36e30bf3df584d58579cbd15c9765cec"
# Your Auth Token from twilio.com/console
auth_token  = "b94bb8a7e20253ff09f6d2697c5548fb"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16692335559",
    from_="+15072837416",
    body="MY PYTHON SCRIPT TEXT")

print(message.sid)