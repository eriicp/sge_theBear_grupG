def venda_schema(venda) -> dict:
    return {
        "Id_Venda": venda.Id_Venda,
        "Data_Venda": venda.Data_Venda,
        "Client_Venda": venda.Client_Venda,
        "Producte_Venda": venda.Producte_Venda,
        "Quantitat": venda.Quantitat,
        "Preu_Unitari": venda.Preu_Unitari,
        "Total": venda.Total,
        "Metode_Pagament": venda.Metode_Pagament,
        "Id_Punt": venda.Id_Punt
    }

def vendes_schema(vendes) -> list[dict]:
    return [venda_schema(v) for v in vendes]
