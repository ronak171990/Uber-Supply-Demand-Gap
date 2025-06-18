CREATE TABLE uber_data (
  request_id       NUMBER NOT NULL,
  pickup_point     VARCHAR2(20),
  driver_id        NUMBER,
  status           VARCHAR2(30) NOT NULL,
  request_timestamp DATE NOT NULL,
  drop_timestamp    DATE,
  request_hour     NUMBER,
  request_day      DATE,
  time_slot        VARCHAR2(20)
);

-- 1️ Total number of ride requests
SELECT COUNT(*) AS total_requests
FROM uber_data;

-- 2️ Total number of requests by trip status
SELECT status, COUNT(*) AS request_count
FROM uber_data
GROUP BY status
ORDER BY request_count DESC;

-- 3️ Breakdown of status by time slot (Morning, Night, etc.)
SELECT time_slot, status, COUNT(*) AS total
FROM uber_data
GROUP BY time_slot, status
ORDER BY time_slot;

-- 4️ Compare trip status (Completed, Cancelled, No Cars) by pickup location
SELECT pickup_point, status, COUNT(*) AS total
FROM uber_data
GROUP BY pickup_point, status
ORDER BY pickup_point;

-- 5️ Distribution of ride requests by hour of the day
SELECT request_hour, COUNT(*) AS total_requests
FROM uber_data
GROUP BY request_hour
ORDER BY request_hour;

-- 6️ Identify time slots with the highest number of cancellations
SELECT time_slot,
       COUNT(*) AS total_requests,
       SUM(CASE WHEN status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_count
FROM uber_data
GROUP BY time_slot
ORDER BY cancelled_count DESC;

-- 7️ Identify pickup point with the highest number of 'No Cars Available'
SELECT pickup_point,
       COUNT(*) AS total_requests,
       SUM(CASE WHEN status = 'No Cars Available' THEN 1 ELSE 0 END) AS no_car_count
FROM uber_data
GROUP BY pickup_point
ORDER BY no_car_count DESC;

-- 8️ Overall completion rate of all ride requests
SELECT 
  ROUND(
    100 * SUM(CASE WHEN status = 'Trip Completed' THEN 1 ELSE 0 END) / COUNT(*), 
    2
  ) AS completion_percentage
FROM uber_data;

-- 9️ Completion rate by time slot
SELECT time_slot,
  ROUND(
    100 * SUM(CASE WHEN status = 'Trip Completed' THEN 1 ELSE 0 END) / COUNT(*), 
    2
  ) AS completion_rate
FROM uber_data
GROUP BY time_slot
ORDER BY completion_rate ASC;

-- 10 Top 3 hours of the day with the highest number of cancellations
SELECT request_hour,
       COUNT(*) AS total,
       SUM(CASE WHEN status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled
FROM uber_data
GROUP BY request_hour
ORDER BY cancelled DESC
FETCH FIRST 3 ROWS ONLY;

