"""Micro-proyecto 2: API con FastAPI conectada a PostgreSQL."""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app import db

app = FastAPI(title="Micro-proyecto 2")


class TareaNueva(BaseModel):
    titulo: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/tareas", status_code=201)
def crear_tarea(tarea: TareaNueva):
    conn = db.get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.execute("INSERT INTO tareas (titulo) VALUES (%s) RETURNING id", (tarea.titulo,))
            return {"id": cur.fetchone()[0], "titulo": tarea.titulo}
    finally:
        conn.close()


@app.get("/tareas")
def listar_tareas():
    conn = db.get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.execute("SELECT id, titulo, completada FROM tareas ORDER BY id")
            return [{"id": i, "titulo": t, "completada": c} for i, t, c in cur.fetchall()]
    finally:
        conn.close()


@app.delete("/tareas/{tarea_id}")
def eliminar_tarea(tarea_id: int):
    conn = db.get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.execute("DELETE FROM tareas WHERE id = %s", (tarea_id,))
            if cur.rowcount == 0:
                raise HTTPException(status_code=404, detail="Tarea no encontrada")
            return {"eliminada": tarea_id}
    finally:
        conn.close()
