# synapseFi_Task | mercury.co

## Installation
* Git clone the repository
* Get client id and secret key from synapseFi and add it to webapp/config.py file
* Install Docker and docker-compose (https://docs.docker.com/compose/install/)
* Go to synapseFi_project folder and check that there is docker-compose.yml file
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
