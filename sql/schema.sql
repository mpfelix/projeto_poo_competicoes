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

