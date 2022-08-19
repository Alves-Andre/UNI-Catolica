--INTEGRANTES: ANDRÉ ALVES, LEONARDO VINICIUS, MATEUS TEIXEIRA, ERIKY BALTK,OSVALDO TEODORO 

SELECT * FROM filmes
SELECT genero FROM filmes GROUP BY genero
--1
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes

--2
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Comédia';
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Drama';
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Ficção e Fantasia';
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Mistério e Suspense';
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Arte';
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Ação e Aventura'
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Animação';

--3
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Comédia' AND ano_lancamento='2011' ;
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Drama' AND ano_lancamento='2011' ;
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Ficção e Fantasia' AND ano_lancamento='2011' ;
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Mistério e Suspense' AND ano_lancamento='2011' ;
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Arte' AND ano_lancamento='2011' ;
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Ação e Aventura'
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Animação' AND ano_lancamento='2011' ;

--4
SELECT * FROM filmes WHERE preco_aluguel> (SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes);

--5

--Iremos investir em todos os filmes listados na questão 4
