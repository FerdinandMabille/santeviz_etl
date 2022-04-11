# coding: utf-8

# # Module
import psycopg2


def test_connexion(param_connexion_db):
    """
    Fonction permettant de tester la connexion avec la bdd PostgreSQL

    Paramètre :
        param_connexion_db[dict] : éléments de connexion à la bdd PostgreSQL
    """
    print("--- TEST_CONNEXION ---\n")
    # Attributions des paramètres de connexion
    user = param_connexion_db["user"]
    password = param_connexion_db["password"]
    host = param_connexion_db["host"]
    port = param_connexion_db["port"]
    database = param_connexion_db["database"]

    try:
        conn = psycopg2.connect(
            user = user,
            password = password,
            host = host,
            port = port,
            database = database
        )
    
        cur = conn.cursor()

        # Afficher la version de PostgreSQL
        cur.execute("SELECT version();")
        version = cur.fetchone()
        print("--- Connecté à la base de données :", database)
        print("--- Version :", version, "\n")

        # Fermeture de la connexion à la base de données
        cur.close()
        conn.close()
        print("--- La connexion PostgreSQL est fermée\n")

    except (Exception, psycopg2.Error) as error:
        print("--- Erreur lors de la connexion à PostgreSQL :", error)


def init_postgre_db():
    print("--- INIT_POSTGRE_DB ---\n")


def create_table():
    print("--- CREATE_TABLE ---\n")


def dump_data():
    print("--- DUMP_DATA ---\n")