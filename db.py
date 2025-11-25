import sqlite3

DB_PATH = 'myDB.db'

def _get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def create_user(data):
    required = ['nombre', 'apellido', 'email']
    for r in required:
        if r not in data:
            raise ValueError(f"Falta el campo requerido: {r}")

    with _get_conn() as conn:
        cur = conn.cursor()
        try:
            cur.execute("""
                INSERT INTO users (nombre, apellido, email, edad)
                VALUES (?, ?, ?, ?)
            """, (data.get('nombre'), data.get('apellido'),
                  data.get('email'), data.get('edad')))
            conn.commit()
            return get_user(cur.lastrowid)
        except sqlite3.IntegrityError as e:
            raise ValueError(str(e))

def get_all_users():
    with _get_conn() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        return [dict(r) for r in rows]

def get_user(user_id):
    with _get_conn() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE id=?", (user_id,))
        row = cur.fetchone()
        return dict(row) if row else None

def update_user(user_id, data):
    campos = ['nombre', 'apellido', 'email', 'edad']
    sets = []
    valores = []

    for c in campos:
        if c in data:
            sets.append(f"{c}=?")
            valores.append(data[c])

    if not sets:
        raise ValueError("No hay campos válidos para actualizar.")

    valores.append(user_id)

    with _get_conn() as conn:
        cur = conn.cursor()
        try:
            cur.execute(f"UPDATE users SET {', '.join(sets)} WHERE id=?", valores)
            conn.commit()
            if cur.rowcount == 0:
                return None
            return get_user(user_id)
        except sqlite3.IntegrityError as e:
            raise ValueError(str(e))

def delete_user(user_id):
    with _get_conn() as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE id=?", (user_id,))
        conn.commit()
        return cur.rowcount > 0
