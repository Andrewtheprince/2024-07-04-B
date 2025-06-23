from database.DB_connect import DBConnect
from model.sighting import Sighting
from model.state import State


class DAO:


    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)
        result = []
        query = """ SELECT distinct YEAR(s.datetime)
                    FROM sighting s
                    order by YEAR(s.datetime) asc"""
        cursor.execute(query)
        for row in cursor:
            result.append(row["YEAR(s.datetime)"])
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getStati(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """ SELECT DISTINCTROW s.*
                    FROM state s, sighting ss
                    where s.id = ss.state and year(ss.`datetime`) = %s
                    order by s.Name asc
                    """
        cursor.execute(query, (anno,))
        for row in cursor:
            result.append(State(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAvvistamenti(anno, idStato):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """ SELECT distinctrow *
                    FROM sighting s
                    where s.state = %s and year(s.`datetime`) = %s """
        cursor.execute(query, (idStato, anno,))
        for row in cursor:
            result.append(Sighting(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi(idStato, anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """ select *
                    from (  SELECT distinctrow s.id as id1, s.shape as shape1
                            FROM sighting s
                            where s.state = %s and year(s.`datetime`) = %s) a1, ( SELECT distinctrow s.id as id2, s.shape as shape2
										                                              FROM sighting s
										                                              where s.state = %s and year(s.`datetime`) = %s) a2
                    where a1.id1 != a2.id2 and a1.shape1 = a2.shape2 """
        cursor.execute(query, (idStato, anno, idStato, anno,))
        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result
