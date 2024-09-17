from pathlib import Path

from dulwich.repo import BASE_DIRECTORIES

API_URL = "https://api.hh.ru/vacancies"
BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR.joinpath("data", "vacancies.json")
