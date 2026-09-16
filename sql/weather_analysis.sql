-- Average temperature by city
SELECT city, ROUND(AVG(temperature_c), 2) AS avg_temperature_c
FROM weather_observations
GROUP BY city
ORDER BY avg_temperature_c DESC;

-- Average humidity by city
SELECT city, ROUND(AVG(humidity_pct), 2) AS avg_humidity
FROM weather_observations
GROUP BY city
ORDER BY avg_humidity DESC;

-- Monthly rainfall
SELECT
    year,
    month,
    month_name,
    ROUND(SUM(precipitation_mm), 2) AS rainfall_mm
FROM weather_observations
GROUP BY year, month, month_name
ORDER BY year, month;

-- Hottest recorded observations
SELECT date, city, temperature_c
FROM weather_observations
ORDER BY temperature_c DESC
LIMIT 10;

-- Wind analysis
SELECT city, ROUND(AVG(wind_speed_kmh), 2) AS avg_wind_kmh
FROM weather_observations
GROUP BY city
ORDER BY avg_wind_kmh DESC;
