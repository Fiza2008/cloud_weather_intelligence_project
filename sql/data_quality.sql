SELECT COUNT(*) AS total_rows FROM weather_observations;

SELECT COUNT(*) AS null_temperature
FROM weather_observations
WHERE temperature_c IS NULL;

SELECT COUNT(*) AS invalid_humidity
FROM weather_observations
WHERE humidity_pct < 0 OR humidity_pct > 100;

SELECT COUNT(*) AS negative_rainfall
FROM weather_observations
WHERE precipitation_mm < 0;

SELECT COUNT(*) AS duplicate_city_date
FROM (
    SELECT date, city, COUNT(*) AS c
    FROM weather_observations
    GROUP BY date, city
    HAVING c > 1
);
