from database.DB_connect import DBConnect

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