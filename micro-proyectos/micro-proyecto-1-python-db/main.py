"""Micro-proyecto 1: CRUD básico en PostgreSQL con Python."""
import os

import psycopg2
from dotenv import load_dotenv


def get_connection():
    """Abre una conexión usando DATABASE_URL del archivo .env."""
    load_dotenv()
    url = os.getenv("DATABASE_URL")
    if not url:
        raise RuntimeError("Falta DATABASE_URL. Copia .env.example a .env y complétalo.")
    return psycopg2.connect(url)


def crear_tabla(conn):
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


def agregar_tarea(conn, titulo):
    with conn, conn.cursor() as cur:
        cur.execute("INSERT INTO tareas (titulo) VALUES (%s) RETURNING id", (titulo,))
        return cur.fetchone()[0]


def listar_tareas(conn):
    with conn, conn.cursor() as cur:
        cur.execute("SELECT id, titulo, completada FROM tareas ORDER BY id")
        return cur.fetchall()


def completar_tarea(conn, tarea_id):
    with conn, conn.cursor() as cur:
        cur.execute("UPDATE tareas SET completada = TRUE WHERE id = %s", (tarea_id,))
        return cur.rowcount


def eliminar_tarea(conn, tarea_id):
    with conn, conn.cursor() as cur:
        cur.execute("DELETE FROM tareas WHERE id = %s", (tarea_id,))
        return cur.rowcount


def main():
    conn = get_connection()
    try:
        crear_tabla(conn)
        nueva = agregar_tarea(conn, "Terminar el micro-proyecto 1")
        completar_tarea(conn, nueva)
        for tarea in listar_tareas(conn):
            print(tarea)
        eliminar_tarea(conn, nueva)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
