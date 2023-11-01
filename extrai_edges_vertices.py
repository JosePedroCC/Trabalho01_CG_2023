import sys

def parse_edges(face_str):
    face_str = face_str.replace('f ','')
    # Divide a string da face em partes usando espaço como delimitador
    parts = face_str.split(' ')

    # Inicializa uma lista para armazenar as arestas
    edges = []

    # Loop através das partes da face
    for i in range(len(parts)):
        vertex_data = parts[i].split('/')
        current_vertex = int(vertex_data[0])
        vertex_data = parts[(i+1)%len(parts)].split('/')
        next_vertex = int(vertex_data[0])
        edges.append((current_vertex, next_vertex))

    return edges

def parse_vertices(vertices_str):
    # Remove o '\n' do final da linha
    vertices_str = vertices_str.rstrip('\n')
    # Divide a string de vertices em partes usando espaço como delimitador
    parts = vertices_str.split(' ')

    vertices = f"[{parts[1]}, {parts[2]}, {parts[3]}, 1.0], "

    return vertices

def main():
    nome_arquivo = "cena.obj"

    if len(sys.argv) > 1:
        nome_arquivo = sys.argv[1]

    entrada = open(nome_arquivo, mode='r', encoding='UTF-8')
    esaida = open('global_edges2.py', mode='w', encoding='UTF-8')
    vsaida = open('global_vertices2.py', mode='w', encoding='UTF-8')

    esaida.write("edges = (\n\t")
    vsaida.write("vertices = [\n")
    line = entrada.readline()
    while line:
        if line.find('f ') != -1:
            edges = parse_edges(line)
            for edge in edges:
                esaida.write(f"({edge[0]-251}, {edge[1]-251}), ")
            esaida.write("\n\t")

        elif line.find('v ') != -1:
            vsaida.write("\t"+parse_vertices(line))
            vsaida.write("\n")

        line = entrada.readline()

    posicao = esaida.tell() - 5
    esaida.seek(posicao)
    esaida.truncate()
    esaida.write("\n)")

    posicao = vsaida.tell() - 4
    vsaida.seek(posicao)
    vsaida.truncate()
    vsaida.write("\n]")

    entrada.close()
    esaida.close()
    vsaida.close()

if __name__ == "__main__":
    main()
