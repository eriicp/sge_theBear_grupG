from schema import read_sch

def registre():
    users = {
        "user1":{
            "id":1,
            "name":"Eric",
            "surname":"Parada",
            "age":18
        },
        "user2": {
            "id": 2,
            "name": "Hugo",
            "surname": "Murillo",
            "age": 18
        },
        "user3": {
            "id": 3,
            "name": "Oriol",
            "surname": "Martínez",
            "age": 19
        },
        "user4": {
            "id": 4,
            "name": "Itzan",
            "surname": "Jimenez",
            "age": 33
        }
    }
    return read_sch.schemas(users)