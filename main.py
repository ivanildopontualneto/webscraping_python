import requests

response = requests.get('https://www.walissonsilva.com/')

print('Status code: ', response.status_code)
print('\nHeader')
print(response.headers)

print('\nContent')
print(response.content)



