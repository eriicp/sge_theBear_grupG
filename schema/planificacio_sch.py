def planificacio_schema(plan) -> dict:
    return {
        "Id_Planificacio": plan.Id_Planificacio,
        "Projecte": plan.Projecte,
        "Tasca": plan.Tasca,
        "Responsable": plan.Responsable,
        "Data_Inici": plan.Data_Inici,
        "Data_Fi": plan.Data_Fi,
        "Estat_Tasca": plan.Estat_Tasca,
        "Material_Utilitzat": plan.Material_Utilitzat,
        "Comentaris": plan.Comentaris
    }

def planificacions_schema(plans) -> list[dict]:
    return [planificacio_schema(p) for p in plans]
