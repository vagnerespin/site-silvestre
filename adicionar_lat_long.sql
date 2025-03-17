
-- Script SQL para corrigir sua tabela 'local' existente
-- Execute isso no seu banco de dados SQLite

ALTER TABLE local ADD COLUMN latitude FLOAT;
ALTER TABLE local ADD COLUMN longitude FLOAT;

-- Após isso, recadastre o Parque Cesamar com coordenadas válidas, ou use o script automático.
