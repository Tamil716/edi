import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r"D:\oracle\instantclient\instantclient_21_7")


def connect(config):
    print('Connect')
    try:
        # connection = cx_Oracle.connect('dbqa/Qadevu$er@ohisnapdevdb25:1521/basetech6')
        connection = cx_Oracle.connect(
            config.user_name,
            config.password,
            config.dsn,
            encoding='UTF-8')
        print('Connected successfully')
        return connection
    except cx_Oracle.DatabaseError as er:
        print('There is an error in the Oracle database:', er)
        return er


def close(connection):
    if connection:
        connection.close()
        print('Connection closed')


def execute(query, connection):
    result = [];
    try:
        cur = connection.cursor()

        # fetchall() is used to fetch all records from result set
        cur.execute(query)
        rows = cur.fetchall()
        # print(rows)
        col_names = [row[0] for row in cur.description]
        result.append(col_names);
        result.append(rows)
        # print(result)
        # fetchmany(int) is used to fetch limited number of records from result set based on integer argument passed in it
        # cur.execute(statement)
        # # commit() to make changes reflect in the database
        # connection.commit()
        # print('Record inserted successfully')

        # fetchone() is used fetch one record from top of the result set
        # cur.execute('select * from pcmp.users')
        # rows = cur.fetchone()
        # print(rows)
        return result;
    except cx_Oracle.DatabaseError as er:
        print('There is an error in the Oracle database:', er)
        result.append('There is an error in the Oracle database:'+str(er))
        return result;

    except Exception as er:
        print('Error:' + str(er))
        result.append('Error:' + str(er))
        return result;
    finally:
        if cur:
            cur.close()


def insert(query, connection):
    try:
        # print(query)
        cur = connection.cursor()
        cur.execute(query)
        # # commit() to make changes reflect in the database
        connection.commit()
        print('Record inserted successfully')

        # fetchone() is used fetch one record from top of the result set
        # cur.execute('select * from pcmp.users')
        # rows = cur.fetchone()
        # print(rows)
        return 'Record inserted successfully';
    except cx_Oracle.DatabaseError as er:
        print('There is an error in the Oracle database:', er)
        return er;

    except Exception as er:
        print('Error:' + str(er))
        return str(er)
    finally:
        if cur:
            cur.close()
