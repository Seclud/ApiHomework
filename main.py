import requests


response = requests.get('https://fakestoreapi.com/products')
json_response = response.json()

print("Все продукты, цена которых <20")
for product in json_response:
    if product["price"] < 20:
        print(product)

print("Все категории товаров")
categories=[]
for product in json_response:
    if product["category"] not in categories:
        categories.append(product["category"])
print(categories)

print("Все продукты с категорией jewelery")
for product in json_response:
    if product["category"] == "jewelery":
        print(product)

print("Все пользователи")
users_response = requests.get('https://fakestoreapi.com/users')
json_user_response = users_response.json()
print(json_user_response)

print("Создание нового пользователя")
new_user_data = {"email": "aboba@mail.com", "username": "us3r","password": "<PASSWORD>","name": {"firstname":"John","lastname":"Doe"},
                 "address":{"city":"kilcoole","street":"7835 old road", "number":3,"zipcode":"12942-3912","geolocation":{"lat":"-37.1209","long":"81.1923"}},
                 "phone":"1-234-567-8901"}
new_user_response = requests.post('https://fakestoreapi.com/users', json=new_user_data)
print(new_user_response.json())