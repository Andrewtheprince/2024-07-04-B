from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._idMap = {}

    @staticmethod
    def getAnni():
        return DAO.getAnni()

    @staticmethod
    def getStati(anno):
        return DAO.getStati(anno)

    def buildGraph(self, anno, stato):
        self._graph.clear()
        self._idMap.clear()
        sightning = DAO.getAvvistamenti(anno, stato)
        self._graph.add_nodes_from(sightning)
        for nodo in sightning:
            self._idMap[nodo.id] = nodo
        archi = DAO.getArchi(stato, anno)
        for arco in archi:
            if self._idMap[arco["id1"]].distance_HV(self._idMap[arco["id2"]]) < 100:
                self._graph.add_edge(self._idMap[arco["id1"]], self._idMap[arco["id2"]])

    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges(), nx.number_connected_components(self._graph)

    def infoComponenteConnessa(self):
        componenti = list(nx.connected_components(self._graph))
        componente_maggiore = max(componenti, key=len)
        sottografo = self._graph.subgraph(componente_maggiore).copy()
        return sottografo.nodes()