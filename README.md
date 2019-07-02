# synapseFi_Task | mercury.co

## Installation
* Git clone the repository
* Get client id and secret key from synapseFi and add it to webapp/config.py file
* Install Docker and docker-compose (https://docs.docker.com/compose/install/)
* Go to synapseFi_project folder in terminal, where you can see docker-compose.yml file
* Run following commands:
    - docker-compose build
    - docker-compose up

## API Documentation

* Create User (post)
    - 127.0.0.1:80/user/<string:user_id=None>
```python
body={
  "logins": [
    {
      "email": "test@synapsefi.com"
    }
  ],
  "phone_numbers": [
    "901.111.1111",
    "test@synapsefi.com"
  ],
  "legal_names": [
    "Test User"
  ],
  "extra": {
    "supp_id": "122eddfgbeafrfvbbb",
    "cip_tag":1,
    "is_business": false
  }
}
```  

* Get/View User (get)
    - 127.0.0.1:80/user/<string:user_id="5d1a704b50fefc643509002f">

* Update User (get)
    - 127.0.0.1:80/user/<string:user_id="5d1a704b50fefc643509002f">
```python
body={
  "documents":[{
    "id":"2a4a5957a3a62aaac1a0dd0edcae96ea2cdee688ec6337b20745eed8869e3ac8",
    "email":"test2@synapsefi.com"
  }]
}
```


* Other APIs
  - Add/Delete KYC Document   (127.0.0.1:80/kyc/<string:user_id>)

  - Add/Update/View Deposit Account    (127.0.0.1:80/deposit_acc/<string:user_id>')
  - Add/View/Modify    (127.0.0.1:80/issue_routing/<string:user_id>/<string:node_id>/<string:subnet_id>')
  - Fund or Withdraw from deposit acount  (127.0.0.1:80/fund_withdraw/<string:user_id>/<string:node_id>')
  - Add/Update/View/Delete Debit card   (127.0.0.1:80/debitcard/<string:user_id>/<string:node_id>/<string:subnet_id>')
  - View Statements   (127.0.0.1:80/statements/')
