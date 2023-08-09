A Wallet Service API for the given assignment - https://documenter.getpostman.com/view/8411283/SVfMSqA3?version=latest

## APIs
* http://localhost/api/v1/init - POST (Initialize my account for wallet)
* http://localhost/api/v1/wallet - POST (Enable my wallet)
* http://localhost/api/v1/wallet - GET (View my wallet balance)
* http://localhost/api/v1/wallet/transactions - GET (View my wallet transactions)
* http://localhost/api/v1/wallet/deposits - POST (Add virtual money to my wallet)
* http://localhost/api/v1/wallet/withdrawals - POST (Use virtual money from my wallet)
* http://localhost/api/v1/wallet - PATCH (Disable my wallet)

## Installation

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
   python manage.py makemigrations
   python manage.py migrate
   ```
5. In a terminal go to path where `manage.py` is located and run below script to add data
   ```
   cd PATH_TO_MANAGE.PY
   python manage.py shell
   ```
   ``` python
   >>> from walletApp import models
   >>> models.Customer.objects.create(id="wefq324-ver-324fa-ff4f32")
   >>> models.Customer.objects.create(id="3dfvgd-gh4j3bhj-bhd347")
   >>> models.Customer.objects.create(id="sca4c-sdvb5-cfe63")
   ```
6. Now run the application
   ```
   python manage.py runserver
   ```
   
