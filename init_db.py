import mysql.connector

# Configuração da conexão
DB_CONFIG = {
    "host": "localhost",
    "user": "root",       # ajuste se necessário
    "password": "",       # ajuste se necessário
    "database": "competicoes"
}

# Script SQL para criação das tabelas
CREATE_SCRIPT = """
CREATE DATABASE IF NOT EXISTS competicoes
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE competicoes;

CREATE TABLE IF NOT EXISTS equipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS membros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    equipe_id INT NOT NULL,
    CONSTRAINT fk_membros_equipes FOREIGN KEY (equipe_id)
      REFERENCES equipes(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS provas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE,
    tipo ENUM('teorica','pratica') NOT NULL,
    pontuacao_maxima INT NOT NULL,
    num_questoes INT NULL,
    tempo_limite INT NULL
);

CREATE TABLE IF NOT EXISTS resultados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    equipe_id INT NOT NULL,
    prova_id INT NOT NULL,
    pontuacao DECIMAL(10,2) NOT NULL,
    UNIQUE KEY uq_resultado (equipe_id, prova_id),
    CONSTRAINT fk_resultados_equipes FOREIGN KEY (equipe_id)
      REFERENCES equipes(id) ON DELETE CASCADE,
    CONSTRAINT fk_resultados_provas FOREIGN KEY (prova_id)
      REFERENCES provas(id) ON DELETE CASCADE
);
"""

# Dados iniciais
EQUIPES = [
    ("Equipe Alpha",),
    ("Equipe Beta",),
    ("Equipe Gamma",)
]

PROVAS = [
    ("Matemática", "teorica", 100, 20, 60),
    ("Programação", "pratica", 200, None, 180),
    ("Robótica", "pratica", 150, None, 120),
]

RESULTADOS = [
    ("Equipe Alpha", "Matemática", 85.0),
    ("Equipe Beta", "Matemática", 90.0),
    ("Equipe Gamma", "Programação", 150.0),
    ("Equipe Alpha", "Robótica", 120.0),
]


def init_db():
    # Conexão inicial (sem banco)
    conn = mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )
    cur = conn.cursor()
    for stmt in CREATE_SCRIPT.split(";"):
        stmt = stmt.strip()
        if stmt:
            cur.execute(stmt)
    conn.commit()
    cur.close()
    conn.close()

    # Conexão com banco já criado
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()

    # Inserir equipes (evita duplicados)
    for e in EQUIPES:
        cur.execute("INSERT IGNORE INTO equipes (nome) VALUES (%s)", e)

    # Inserir provas (evita duplicados)
    for p in PROVAS:
        cur.execute(
            "INSERT IGNORE INTO provas (nome, tipo, pontuacao_maxima, num_questoes, tempo_limite) VALUES (%s, %s, %s, %s, %s)",
            p
        )

    # Inserir resultados (upsert)
    for equipe_nome, prova_nome, pontos in RESULTADOS:
        cur.execute("SELECT id FROM equipes WHERE nome=%s", (equipe_nome,))
        equipe = cur.fetchone()
        cur.execute("SELECT id FROM provas WHERE nome=%s", (prova_nome,))
        prova = cur.fetchone()
        if equipe and prova:
            cur.execute(
                """
                INSERT INTO resultados (equipe_id, prova_id, pontuacao)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE pontuacao = VALUES(pontuacao)
                """,
                (equipe[0], prova[0], pontos)
            )

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Banco de dados inicializado com sucesso (idempotente)!")


if __name__ == "__main__":
    init_db()
