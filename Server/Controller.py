import sqlite3

class Controller(object):
    __SQLite3 = None

    def __init__(self):
        self.__SQLite3 = sqlite3.connect('data.db')

    def QueryRead(self, query):
        if not query: return
        cursor = self.__SQLite3.cursor()
        try:
            cursor.execute(query)
        except Exception  as e:
            return e
        
    def Close(self):
        self.__SQLite3.close()
