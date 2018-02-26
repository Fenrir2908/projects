import osa

url = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'

client = osa.client.Client(url)
print(client.types)

response = client.service.ConvertTemp(Temperature=15.00, FromUnit='degreeFahrenheit', ToUnit='degreeCelsius')

print(response)

url2 = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'

client2 = osa.client.Client(url2)
response2 = client2.service.Currencies()

print(response2.split(';'))

response3 = client2.service.ConvertToNum(fromCurrency='EUR', toCurrency='RUB', amount=126.50, rounding=True)
print(response3)