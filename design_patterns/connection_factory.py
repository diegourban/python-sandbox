# -*- coding: utf-8 -*-
import MySQLdb

class Connection_factory(object):

    def get_connection(self):
        # tratamento de erro omitido
        return MySQLdb.connect(host="localhost",
            user='root',
            passwd='',
            db='alura')


if __name__ == '__main__':
    # -*- coding: utf-8 -*-
    from connection_factory import Connection_factory

    # escondeu os detalhes de criação do banco
    # tratamento de erro omitido
    connection = Connection_factory().get_connection()

    cursor = connection.cursor()
    cursor.execute('SELECT * from cursos')

    for linha in cursor:
        print
        linha

    connection.close()