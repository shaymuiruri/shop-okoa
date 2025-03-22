import requests

# Making a GET request to retrieve a list of users
response = requests.get('http://localhost:8000/api/user/list/')
if response.status_code == 200:
    users = response.json()
    print(users)
else:
    print(f'Error: {response.status_code}')

# Making a POST request to sign in a user
signin_data = {
    'phone_number': 'your_phone_number',
    'password': 'your_password'
}
response = requests.post('http://localhost:8000/api/user/signin/', json=signin_data)
if response.status_code == 200:
    print("User signed in successfully")
else:
    print(f'Error: {response.status_code}')

# Making a POST request to sign up a user
signup_data = {
    'first_name': 'John',
    'last_name': 'Doe',
    'id_number': '1234567890',
    'phone_number': 'your_phone_number',
    'password': 'your_password',
    'tag_id': 'tag_id_value',
    'trust_score_token': 'trust_score_token_value',
    'user_type': 'customer'
}
response = requests.post('http://localhost:8000/api/user/signup/', json=signup_data)
if response.status_code == 201:
    print("User signed up successfully")
else:
    print(f'Error: {response.status_code}')
