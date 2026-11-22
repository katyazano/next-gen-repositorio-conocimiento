"""Acceso a PostgreSQL. Reutiliza la lógica del micro-proyecto 1."""
import os

import psycopg2
from dotenv import load_dotenv


def get_connection():
    load_dotenv()
    url = os.getenv("DATABASE_URL")
    if not url:
        raise RuntimeError("Falta la variable de entorno DATABASE_URL.")
    return psycopg2.connect(url)


def crear_tabla():
    conn = get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS tareas (
                    id SERIAL PRIMARY KEY,
                    titulo TEXT NOT NULL,
                    completada BOOLEAN NOT NULL DEFAULT FALSE
                )
                """
            )
    finally:
        conn.close()
