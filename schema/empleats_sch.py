def empleat_schema(empleat) -> dict:
    return {
        "Id_Empleat": empleat.Id_Empleat,
        "Nombre_Empleat": empleat.Nombre_Empleat,
        "Puesto_Empleat": empleat.Puesto_Empleat,
        "Departament_Empleat": empleat.Departament_Empleat,
        "Email_Empleat": empleat.Email_Empleat,
        "Telefon_Empleat": empleat.Telefon_Empleat,
        "Id_Gerent_Empleat": empleat.Id_Gerent_Empleat
    }

def empleats_schema(empleats) -> list[dict]:
    return [empleat_schema(e) for e in empleats]
