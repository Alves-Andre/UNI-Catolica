--INTEGRANTES: ANDR� ALVES, LEONARDO VINICIUS, MATEUS TEIXEIRA, ERIKY BALTK,OSVALDO TEODORO 

SELECT * FROM filmes
SELECT genero FROM filmes GROUP BY genero
--1
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes

--2
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Com�dia';
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Drama';
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Fic��o e Fantasia';
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Mist�rio e Suspense';
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Arte';
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='A��o e Aventura'
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Anima��o';

--3
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Com�dia' AND ano_lancamento='2011' ;
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Drama' AND ano_lancamento='2011' ;
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Fic��o e Fantasia' AND ano_lancamento='2011' ;
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Mist�rio e Suspense' AND ano_lancamento='2011' ;
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Arte' AND ano_lancamento='2011' ;
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='A��o e Aventura'
SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes WHERE genero='Anima��o' AND ano_lancamento='2011' ;

--4
SELECT * FROM filmes WHERE preco_aluguel> (SELECT AVG(preco_aluguel) AS MEDIA_PRECO FROM filmes);

--5

--Iremos investir em todos os filmes listados na quest�o 4
