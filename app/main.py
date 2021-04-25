import json
import mail

with open('config.json') as f:
    config=json.load(f)

print(config)

sender = config['sender']
receivers = config['receivers']
smtp_params = (config['host'], config['port'])



print(f'Hello {receivers[0]}, this are the params {smtp_params[0]}:{smtp_params[1]}')
print(f'MfG {sender}')

mail.sendmail(smtp_params, sender, receivers)