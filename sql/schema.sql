-- Schema e tabelas do sistema de competições
CREATE DATABASE IF NOT EXISTS competicoes CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE competicoes;

CREATE TABLE IF NOT EXISTS equipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
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
    nome VARCHAR(100) NOT NULL,
    tipo ENUM('teorica','pratica') NOT NULL,
    pontuacao_maxima INT NOT NULL,
    num_questoes INT NULL,
    tempo_limite INT NULL
);


CREATE TABLE IF NOT EXISTS resultados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    equipe_id INT NOT NULL,
    prova_id INT NOT NULL,
    pontuacao INT NOT NULL DEFAULT 0,
    CONSTRAINT fk_resultados_equipes FOREIGN KEY (equipe_id)
      REFERENCES equipes(id) ON DELETE CASCADE,
    CONSTRAINT fk_resultados_provas FOREIGN KEY (prova_id)
      REFERENCES provas(id) ON DELETE CASCADE,
    UNIQUE KEY uq_resultado (equipe_id, prova_id) -- garante 1 resultado por equipe/prova
);
