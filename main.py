# import psycopg2
# from config import host, user, password, db_name


# try:
# #подключиться к существующей базе данных
#     connection = psycopg2.connect(
#         host = host
#         user = user
#         password = password
#         database = db_name )
# #курсор для выполнения операций с базой данных
#     cursor = connection.cursor()

#     with connection.cursor() as cursor:
#         cursor.execute(
#             "SELECT  version();"
#         )

#         print(f"Server version: {cursor.fetchone{}}")

# except Exception as ex:
#     print("[INFO] Error while working with PostgreSQl", ex)
# finally:
#     if connection:
#         connection.close()
#         print("[INFO] PostgreSQL connection closed")