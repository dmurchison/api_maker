import os

class Config():
    DB_HOST = os.get_env('DB_HOST', 'localhost')
    DB_PORT = os.get_env('DB_PORT', 5432)
    DB_USER = os.get_env('DB_USER', 'postgres')
    DB_PASSWORD = os.get_env('DB_PASSWORD', 'postgres')

