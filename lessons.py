import requests

url = 'https://requestb.in/1d9cgac1'
json = {
    'month' : 'may',
    'day' : '10',
    'result' : '1:0',
    'team' : 'manchester',
}
respounse = requests.post(url, data = '21.02.2018')

print(respounse.status_code)

url2 = 'http://httpbin.org'

params = {
    'id':[1,2,3],
}
respounse = requests.get(url2, params=params)

print(respounse.json())