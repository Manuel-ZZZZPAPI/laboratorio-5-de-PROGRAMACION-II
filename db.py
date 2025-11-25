# db.py
import sqlite3
from typing import Optional, Dict, Any, List

DB_PATH = "myDB.db"

def _get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def _row_to_dict(row: sqlite3.Row) -> Dict[str, Any]:
    return dict(row) if row is not None else None

# Read: todos o por id
def get(user_id: Optional[int] = None):
    conn = _get_conn()
    cur = conn.cursor()
    if user_id is None:
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        result = [dict(r) for r in rows]
    else:
        cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cur.fetchone()
        result = dict(row) if row else None
    conn.close()
    return result

# Create: recibe dict con campos mínimos
def post(data: Dict[str, Any]):
    required = ["nombre"]
    for r in required:
        if r not in data or not data[r]:
            raise ValueError(f"Falta campo requerido: {r}")

    conn = _get_conn()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO users (nombre, apellido, email)
            VALUES (?, ?, ?)
        """, (data.get("nombre"), data.get("apellido"), data.get("email")))
        conn.commit()
        new_id = cur.lastrowid
    except sqlite3.IntegrityError as e:
        conn.close()
        raise e
    conn.close()
    return get(new_id)

# Update
def put(user_id: int, data: Dict[str, Any]):
    # Verificar que existe
    existing = get(user_id)
    if not existing:
        return None

    # Campos permitidos a actualizar
    allowed = ["nombre", "apellido", "email"]
    fields = []
    values = []
    for k in allowed:
        if k in data:
            fields.append(f"{k} = ?")
            values.append(data[k])
    if not fields:
        return existing  # nada que actualizar

    values.append(user_id)
    sql = f"UPDATE users SET {', '.join(fields)} WHERE id = ?"
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()
    conn.close()
    return get(user_id)

# Delete
def delete(user_id: int):
    existing = get(user_id)
    if not existing:
        return None
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    return existing
