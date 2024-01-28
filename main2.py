from shapely.wkt import loads
import random
import requests
import json
import random
from datetime import datetime, timedelta


from pontos import todosPontos


def main(quarteirao, visita_trat, visita_bloq):
    headers = {
        "accept": "*/*",
        "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxLHN0YXViIiwiaXNzIjoiQXJib3Zpcm9zZXMiLCJyb2xlcyI6IltBRE1JTl0iLCJpYXQiOjE3MDY0MDE4ODUsImV4cCI6MTcwNjQ4ODI4NX0.ufPtAykLE-i6X1sOyDM8cQ_M5BSAirjmJDNEoGROnn84x9DqH86h-6X3m7cFhKd2w8zumVLduHlC9vZbR0LCnA",
        "Content-Type": "application/json",
    }
    if quarteirao:
        url = "http://localhost:8080/api/quarteirao"
        arquivo_wkt = "poligonos.txt"
        coordenadas_poligonos = []

        with open(arquivo_wkt, 'r') as file:
            for linha in file:
                linha = linha.strip()

                coordenadas_poligonos.append(linha)

        for i in range(len(coordenadas_poligonos)):
            print(coordenadas_poligonos[i])
            payload = {
                "localidade": {
                    "id": "c06dc84f-2c96-466d-a421-9ee528732742",
                    "descricao": "CONJ. RES. BRANCA VIEIRA",
                    "categoria": "6105",
                    "estrato": {
                        "id": "c06dc84f-2c96-466d-a421-9ee528732742",
                        "codigo": 3
                    }
                },
                "numero": i+1,
                "poligono": coordenadas_poligonos[i],
                "quantidadeImoveis": random.randint(20, 50)
            }

            payload_json = json.dumps(payload)

            response = requests.post(url, headers=headers, data=payload_json)

            print(f"Status Code: {response.status_code}")
            print("Response:")
            print(response.text)
            print("\n")

    if visita_trat:
        url = "http://localhost:8080/api/visita-tratamento"

        for i in range(0, int(len(todosPontos)/2)):
            dias_atras = random.randint(0, 15)
            data_aleatoria = datetime.utcnow() - timedelta(days=dias_atras)
            depositoA1 = random.randint(0, 5)
            depositoA2 = random.randint(0, 5)
            depositoB = random.randint(0, 5)
            depositoC = random.randint(0, 5)
            depositoD1 = random.randint(0, 5)
            depositoD2 = random.randint(0, 5)
            depositoE = random.randint(0, 5)

            payload = {
                "agente": None,
                "data": data_aleatoria.isoformat() + "Z",
                "depositoA1": depositoA1,
                "depositoA2": depositoA2,
                "depositoB": depositoB,
                "depositoC": depositoC,
                "depositoD1": depositoD1,
                "depositoD2": depositoD2,
                "depositoE": depositoE,
                "depositoEliminado": 1,
                "educacaoRealizada": True,
                "imovelInspecionadoLI": True,
                "imovelTratado": True,
                "larvaEncontrada": True,
                "observacao": "teste",
                "observacoes": "teste",
                "latitude": todosPontos[i]["pontoWKT"][1],
                "longitude": todosPontos[i]["pontoWKT"][0],
                "reclamacao": "teste",
                "tipoVisita": None,
            }

            payload_json = json.dumps(payload)

            response = requests.post(url, headers=headers, data=payload_json)

            print(f"Status Code: {response.status_code}")
            print("Response:")
            print(response.text)
            print("\n")

    if visita_bloq:
        url = "http://localhost:8080/api/visita-bloqueio"

        for i in range(int(len(todosPontos)/2), len(todosPontos)):
            dias_atras = random.randint(0, 15)
            data_aleatoria = datetime.utcnow() - timedelta(days=dias_atras)
            depositoA1 = random.randint(0, 5)
            depositoA2 = random.randint(0, 5)
            depositoB = random.randint(0, 5)
            depositoC = random.randint(0, 5)
            depositoD1 = random.randint(0, 5)
            depositoD2 = random.randint(0, 5)
            depositoE = random.randint(0, 5)

            payload = {
                "agente": None,
                "data": data_aleatoria.isoformat() + "Z",
                "depositoA1": depositoA1,
                "depositoA2": depositoA2,
                "depositoB": depositoB,
                "depositoC": depositoC,
                "depositoD1": depositoD1,
                "depositoD2": depositoD2,
                "depositoE": depositoE,
                "depositoEliminado": 1,
                "educacaoRealizada": True,
                "imovelInspecionadoLI": True,
                "imovelTratado": True,
                "larvaEncontrada": True,
                "observacao": "teste",
                "observacoes": "teste",
                "latitude": todosPontos[i]["pontoWKT"][1],
                "longitude": todosPontos[i]["pontoWKT"][0],
                "reclamacao": "teste",
                "tipoVisita": None,
            }

            payload_json = json.dumps(payload)

            response = requests.post(url, headers=headers, data=payload_json)

            print(f"Status Code: {response.status_code}")
            print("Response:")
            print(response.text)
            print("\n")


if __name__ == '__main__':
    main(False, True, True)
