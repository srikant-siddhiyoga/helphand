# Django Helpers API Integration

## Backend setup for APIs

### Installation

   ```bash
   git clone https://github.com/srikant-siddhiyoga/helphand.git
   cd helphand/
   pip install -r requirements.txt
   python manage.py runserver 
```
## Create a responsive frontend using **Nextjs** for the following APIs

**http://127.0.0.1:8000/helpers/** 

**GET** -> list all the helpers

**POST** -> To add new helper,
pass the following data as json

```json
{
    "name": "Suraj chauhan",
    "cost": 250.0,
    "description": "He can Handles electrical issues, installations, and repairs.",
    "address": "mohali Punjab",
    "phone": "6211845989",
    "zipcode": "140055",
    "available": true,
    "helper_type": 1
}
```

**PATCH** -> To update the existing helper,
pass the  following data as json

```json
{
    "id": 10, #id of helper
    "available": true
    #"other fileds": value
}
```

**DELETE** -> To delete the existing helper,
pass the  following data as json

```json
{
    "id": 10, #id of helper
}
```


## For better understanding of API responses, please import the given POSTMAN collection in POSTMAN


