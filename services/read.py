from schema import read_sch

def registre():
    users = {
        "user1":{
            "id":1,
            "name":"Hugo",
            "surname":"Morillo",
            "age":31
        },
        "user2": {
            "id": 2,
            "name": "Eric",
            "surname": "Parado",
            "age": 12
        },
        "user3": {
            "id": 3,
            "name": "Oriol",
            "surname": "Oriolez",
            "age": 19
        }
    }
    return read_sch.schemas(users)