# api_server.py
from flask import Flask, jsonify
from flask_cors import CORS  # Importar la extensión CORS
import mysql.connector
import os

# Environment variables
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_USER = os.environ.get("DB_USER", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
DB_NAME = os.environ.get("DB_NAME", "skeleton")

app = Flask(__name__)
app.config
CORS(app)  # Habilitar CORS para todas las rutas

# Configuración de la conexión a MariaDB


def get_db_connection():
  conn = mysql.connector.connect(
      host=DB_HOST,
      user=DB_USER,
      password=DB_PASSWORD,
      database=DB_NAME
  )
  return conn

# Endpoint para obtener todas las partes del esqueleto


@app.route("/partes", methods=["GET"])
def get_partes():
  conn = get_db_connection()
  # Para obtener resultados como diccionarios
  cursor = conn.cursor(dictionary=True)

  # Obtener todas las partes del esqueleto
  cursor.execute("SELECT * FROM partes")
  partes = cursor.fetchall()

  # Cerrar la conexión
  cursor.close()
  conn.close()

  return jsonify(partes)

# Endpoint para obtener los huesos de una parte del esqueleto


@app.route("/partes/<parte_id>/huesos", methods=["GET"])
def get_huesos(parte_id):
  conn = get_db_connection()
  cursor = conn.cursor(dictionary=True)

  # Obtener los huesos de la parte del esqueleto
  cursor.execute("SELECT * FROM huesos WHERE parte_id = %s", (parte_id,))
  huesos = cursor.fetchall()

  # Cerrar la conexión
  cursor.close()
  conn.close()

  return jsonify(huesos)


if __name__ == "__main__":
  app.run(debug=True)
