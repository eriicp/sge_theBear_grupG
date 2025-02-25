from schema import read_sch

def registre():
    users = {
        "user1" : {
            "id":1,
            "name" : "Hugo",
            "surname": "Murillo",
            "age":49,
        },
        "user2" : {
            "id": 2,
            "name": "Eric",
            "surname": "Parada",
            "age":23,
        },
        "user3" : {
            "id": 3,
            "name": "Itzan",
            "surname": "Jimenez",
            "age":40,
        }
    }
    return read_sch.schemas(users)