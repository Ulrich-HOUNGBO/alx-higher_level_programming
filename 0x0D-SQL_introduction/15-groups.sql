--lists the `score`and number of occuranceswith each scorewith 'number'
SELECT score, COUNT(score) AS 'number' FROM second_table GROUP BY score ORDER BY number DESC;