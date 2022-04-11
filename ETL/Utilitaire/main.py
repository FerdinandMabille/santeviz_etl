# -*-coding:Latin-1 -*


# Modules
import argparse
import pandas as pd

from modules import route_postgre
from utils import utils


# Commandes
def __main__(args):
    if args.commande == "init_database":
        init_db()
    elif args.commande == "transform":
        transform()
    elif args.commande == "all":
        all_functions()
    elif args.commande == "test":
        test_etl()
    return


def test_etl():
    print("##### TEST_ETL #####")
    print("")
    path = "data_test/commune_2022.csv"
    data_csv = pd.read_csv(path)
    data = pd.DataFrame(data = data_csv)
    print(data.head())


def init_db():
    print("#####################")
    print("###### INIT_DB ######")
    print("#####################\n")

    print("--- Recuperation des parametres ---")
    param_postgre_db = utils.read_settings("settings/settings.json", dict = "postgre_db", elem = "postgre_santeviz")
    print("--- param_postgre_db :", param_postgre_db, "\n")

    route_postgre.test_connexion(param_postgre_db)


def transform():
    print("##### TRANSFORM #####")


def all_functions():
    print("##### ALL_FUNCTIONS #####")
    init_db()
    transform()


# Initialisation du parsing
parser = argparse.ArgumentParser()
parser.add_argument("commande", type=str, help="Commande à exécuter")
args = parser.parse_args()


# Core
if __name__ == "__main__":
    __main__(args)
