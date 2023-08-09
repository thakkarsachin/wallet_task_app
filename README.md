A Wallet Service API for the given assignment - https://documenter.getpostman.com/view/8411283/SVfMSqA3?version=latest

## APIs
* http://localhost/api/v1/init - POST (Initialize my account for wallet)
* http://localhost/api/v1/wallet - POST (Enable my wallet)
* http://localhost/api/v1/wallet - GET (View my wallet balance)
* http://localhost/api/v1/wallet/transactions - GET (View my wallet transactions)
* http://localhost/api/v1/wallet/deposits - POST (Add virtual money to my wallet)
* http://localhost/api/v1/wallet/withdrawals - POST (Use virtual money from my wallet)
* http://localhost/api/v1/wallet - PATCH (Disable my wallet)

## Installation and Running

0. Prerequisites
   * Download and Install Python - https://www.python.org/downloads/release/python-3114/
   * Install virtual environment
     ``` ShellScript
     pip install virtualenv
     ```
1. Create a virtual environment
   ``` ShellScript
   python -m venv env
   ```
     - for Windows
     ``` ShellScript
     .\env\Scripts\activate   
     ```
     - for macOS/Linux
     ``` ShellScript
     source env/bin/activate
     ```
2. install djangorestframework
   ```
   pip install djangorestframework
   ```
3. Clone the repo
   ```
   git clone https://github.com/thakkarsachin/wallet_task_app.git
   ```
4. Do migrate
   ```
   cd wallet_task_app
   python manage.py makemigrations
   python manage.py migrate
   ```
5. In a terminal go to path where `manage.py` is located and run below script to add data
   ```
   python manage.py shell
   ```
   ``` python
   >>> from walletApp import models
   >>> models.Customer.objects.create(id="wefq324-ver-324fa-ff4f32")
   >>> models.Customer.objects.create(id="3dfvgd-gh4j3bhj-bhd347")
   >>> models.Customer.objects.create(id="sca4c-sdvb5-cfe63")
   >>> exit()
   ```
6. Now run the application
   ```
   python manage.py runserver
   ```

## Testing APIs

### 1. Init Wallet (generate token)
```
curl --location 'http://localhost:8000/api/v1/init/' --form 'customer_xid="wefq324-ver-324fa-ff4f32"'
```

### 2. Enable Wallet
```
curl --location --request POST 'http://localhost:8000/api/v1/wallet/' \
--header 'Authorization: Token 79e599598a03220f9f2a7dade11e4bdbf6478ed2'
```

### 3. View wallet balance
```
curl --location 'http://localhost:8000/api/v1/wallet/' \
--header 'Authorization: Token 79e599598a03220f9f2a7dade11e4bdbf6478ed2'
```

### 4. View wallet transactions
```
curl --location "http://localhost:8000/api/v1/wallet/transactions" \
--header 'Authorization: Token 79e599598a03220f9f2a7dade11e4bdbf6478ed2'
```

### 5. Add virtual money to wallet
```
curl --location 'http://localhost:8000/api/v1/wallet/deposits/' \
--header 'Authorization: Token 79e599598a03220f9f2a7dade11e4bdbf6478ed2' \
--form 'amount="100000"' \
--form 'reference_id="50535246-dcb2-4929-8cc9-004ea06f5241"'
```

### 6. Use virtual money from wallet
```
curl --location 'http://localhost:8000/api/v1/wallet/withdrawals/' \
--header 'Authorization: Token 79e599598a03220f9f2a7dade11e4bdbf6478ed2' \
--form 'amount="100"' \
--form 'reference_id="50535246-dcb2-4929gde63d-004ea06f5241"'
```

### 7. Disable my wallet
```
curl --location --request PATCH 'http://localhost:8000/api/v1/wallet/' \
--header 'Authorization: Token 79e599598a03220f9f2a7dade11e4bdbf6478ed2' \
--form 'is_disabled="true"'
```
