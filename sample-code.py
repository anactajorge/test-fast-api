from pydantic import BaseModel

class Address(BaseModel):
    city: str
    zipcode: str

class UserData(BaseModel):
    user_id: int
    address: Address

class APIResponse(BaseModel):
    status: str
    data: UserData

# Raw dictionary from your API request
raw_json = {
    "status": "success",
    "data": {
        "user_id": 101,
        "address": {
            "city": "Manila",
            "zipcode": "1000"
        }
    }
}

# 1. CONVERT raw JSON to a usable Python object
validated = APIResponse.model_validate(raw_json)


# 2. GET USER ID
# Use dot notation to drill directly down to the value:
user_id = validated.data.user_id
print(user_id)  
# Output: 101 (as a clean Python integer)


# 3. GET ADDRESS AS A PURE DICTIONARY
# Access the address object, then call .model_dump() to convert just that nest into a dict:
address_dict = validated.data.address.model_dump()
print(address_dict)  
# Output: {'city': 'Manila', 'zipcode': '1000'}