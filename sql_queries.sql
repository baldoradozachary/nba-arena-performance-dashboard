-- NBA Arena Performance & Fan Experience Optimization
-- Sample SQL queries for portfolio/demo use

-- 1. Average attendance by team
SELECT team, ROUND(AVG(attendance), 0) AS avg_attendance
FROM nba_arena_data
GROUP BY team
ORDER BY avg_attendance DESC;

-- 2. Average attendance rate by team
SELECT team,
       ROUND(AVG(CAST(attendance AS FLOAT) / arena_capacity), 3) AS avg_attendance_rate
FROM nba_arena_data
GROUP BY team
ORDER BY avg_attendance_rate DESC;

-- 3. Total revenue by team
SELECT team, SUM(revenue_usd) AS total_revenue
FROM nba_arena_data
GROUP BY team
ORDER BY total_revenue DESC;

-- 4. Best drawing opponents
SELECT opponent, ROUND(AVG(attendance), 0) AS avg_attendance
FROM nba_arena_data
GROUP BY opponent
ORDER BY avg_attendance DESC;

-- 5. Fan satisfaction and attendance
SELECT fan_satisfaction_score,
       ROUND(AVG(attendance), 0) AS avg_attendance
FROM nba_arena_data
GROUP BY fan_satisfaction_score
ORDER BY fan_satisfaction_score DESC;

-- 6. Win vs loss attendance comparison
SELECT
    CASE
        WHEN team_score > opponent_score THEN 'Win'
        ELSE 'Loss'
    END AS game_result,
    ROUND(AVG(attendance), 0) AS avg_attendance,
    ROUND(AVG(revenue_usd), 2) AS avg_revenue
FROM nba_arena_data
GROUP BY game_result;

-- 7. Revenue per fan by team
SELECT team,
       ROUND(AVG(CAST(revenue_usd AS FLOAT) / attendance), 2) AS avg_revenue_per_fan
FROM nba_arena_data
GROUP BY team
ORDER BY avg_revenue_per_fan DESC;

-- 8. Highest revenue games
SELECT date, team, opponent, attendance, revenue_usd
FROM nba_arena_data
ORDER BY revenue_usd DESC
LIMIT 10;
