from schema import read_sch

def registre():
    users = {
        "user1":{
            "id":1,
            "name":"Hugo",
            "surname":"Murillo",
            "age":18
        },
        "user2": {
            "id": 2,
            "name": "Eric",
            "surname": "Parada",
            "age": 19
        },
        "user3": {
            "id": 3,
            "name": "Oriol",
            "surname": "Martínez",
            "age": 20
        },
        "user4": {
            "id": 4,
            "name": "Mesi",
            "surname": "Jimenez",
            "age": 68
        }
    }
    return read_sch.schemas(users)