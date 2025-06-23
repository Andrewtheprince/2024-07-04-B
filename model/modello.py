from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        pass

    @staticmethod
    def getAnni():
        return DAO.getAnni()