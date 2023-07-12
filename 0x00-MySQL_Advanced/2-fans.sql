-- Create a temporary table to store the aggregated fan counts per origin
CREATE TEMPORARY TABLE temp_country_fans AS
SELECT origin, COUNT(*) AS nb_fans
FROM metal_bands
GROUP BY origins;

-- Rank the origins based on the fan counts
SELECT origin, nb_fans
FROM temp_country_fans
ORDER BY nb_fans DESC;
