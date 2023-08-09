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

0. Prerequisities
   * Download and Install Python - https://www.python.org/downloads/release/python-3114/
   * Install virtual environment
     ``` ShellScript
     pip install virtualenv
     ```
1. Create virtual environment
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
2. 
