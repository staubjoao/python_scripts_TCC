import subprocess
from shapely.geometry import Polygon, Point, MultiPolygon
from shapely.wkt import loads
import random


def generate_random_point_in_polygon(polygon):
    min_x, min_y, max_x, max_y = polygon.bounds
    while True:
        point = Point(random.uniform(min_x, max_x),
                      random.uniform(min_y, max_y))
        if polygon.contains(point):
            return point


def main():
    arquivo_wkt = "poligonos.txt"
    token = "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxLHN0YXViIiwiaXNzIjoiQXJib3Zpcm9zZXMiLCJyb2xlcyI6IltBRE1JTl0iLCJpYXQiOjE3MDU5NzA1NzQsImV4cCI6MTcwNjA1Njk3NH0.lrLtp0rRjsQo0BDSBwIKSpfpWaDRMGXyAt8nDJRrhnYJzk55LGlsbirAikncVs5odtRD4PCUon58ZP26HlZ7pQ"

    coordenadas_poligonos = []

    with open(arquivo_wkt, 'r') as file:
        for linha in file:
            linha = linha.strip()

            polygon = loads(linha)

            polygon_coordinates = list(polygon.exterior.coords)

            coordenadas_poligonos.append(polygon_coordinates)

    for i, polygon_coords in enumerate(coordenadas_poligonos):
        quantidade_pontos = random.randint(1, 5)
        polygon = Polygon(polygon_coords)
        random_points = [generate_random_point_in_polygon(
            polygon) for _ in range(quantidade_pontos)]

        print(i)
        for point in random_points:
            if polygon.contains(point):
                comando_curl = (
                    f'curl -X POST "http://localhost:8080/api/ponto_geografico" '
                    f'-H "accept: */*" '
                    f'-H "Authorization: Bearer {token}" '
                    f'-H "Content-Type: application/json" '
                    f'-d \'{{ "ponto": "POINT({point.x} {point.y})", "pontoWKT": null }}\''
                )
                subprocess.run(comando_curl, shell=True)
                print()


if __name__ == '__main__':
    main()
