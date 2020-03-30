
import os.path
from flask import Flask, render_template_string
from networkx.drawing.nx_agraph import graphviz_layout, write_dot
import matplotlib.pyplot as plt
import pygraphviz
import numpy as np
import networkx as nx
import wget
import re

#_URL = 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat'
# wget.download(_URL)


def exercise1():
    """
    "Use regex to make a list of distinct airports and a list of edges.
    (Each line in the file contains two airports, 
    where the first is out-degree and the second is in-degree"
    """
    pattern = re.compile(r'([A-Z]{3}),')
    airports = set()  # distinct list?
    edges = []
    #result_list = []
    with open('routes.dat', 'r', encoding='utf-8') as file_object:
        for line in file_object:
            result = re.findall(pattern, line)
            airport = result[0]
            edge = result[1]

            airports.add(airport)
            edges.append((airport, edge))
            #print(airport, edge)
    #         if (airport in result_list):
    #             print('here')
    #             result_list[airport].append([edge])
    #         else:
    #             # print('here2')
    #             data = list((airport, edge))
    #             # print(data)
    #             result_list.append(data)  # better way?
    #         # print(line)
    #         # print(result)
    #         # airports.append(result[0])
    #         # edges.append(result[1])
    #         # result_list.append(result[0])
    #         # result_list.append(result[1])
    # #result_list = []
    # # for airport, edge in zip(airports, edges):
    #     #result_list.extend([(airport, edge)])
    return airports, edges


airports, edges = exercise1()
#print('here', result)
result_np = np.array(edges)
print(edges[:10])
print(result_np)


def exercise2():
    """
    Create a directed graph and find the 30 airports with the most edges. Draw a graph over this subgraph
    """
    graph = nx.Graph()
    graph.add_nodes_from(airports)
    graph.add_edges_from(edges)
    print("Main graph:", nx.info(graph))
    top_30 = sorted(graph.degree, key=lambda x: x[1], reverse=True)[:30]
    print(top_30)
    sub_graph = nx.Graph(top_30)
    print("Sub graph:", nx.info(sub_graph))
    nx.draw(sub_graph, pos=graphviz_layout(sub_graph),
            node_size=30, width=.08, cmap=plt.cm.Blues,
            with_labels=True, font_size=12, node_color=range(len(sub_graph)))
    plt.show()  # saved as visualization.png


# exercise2()


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'img')


def exercise3():
    """
    Create a flask server that can show this graph
    """


@app.route('/', methods=['GET'])
def show_graph():
    index = """
    <html>
        <head>
            <title>Flask Shop</title>
        </head>
        <body>
            <p>hello</p>
            <img src="{{ image }}" alt="Graph image">
        </body>
    </html>
    """  # lazy
    path = os.path.join(app.config['UPLOAD_FOLDER'], 'visualization.png')
    print(path)
    # only works locally :^)
    return render_template_string(index, image=path)


if __name__ == '__main__':
    app.run(debug=True)
