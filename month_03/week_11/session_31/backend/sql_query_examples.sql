-- dvd rental database
select * from actor;

select first_name from actor;

select first_name, last_name, email from customer;

SELECT
   first_name || ' ' || last_name as full_name,
   email
FROM
   customer;


SELECT
   first_name,
   last_name AS surname
FROM customer;

SELECT
    first_name || ' ' || last_name "Full Name"
FROM
    customer;


-- FROM -> SELECT -> ORDER BY

SELECT
  first_name,
  last_name
FROM
  customer
ORDER BY
  first_name ASC; -- ascending

SELECT
  first_name,
  last_name
FROM
  customer
ORDER BY
  first_name DESC;  -- descending


SELECT
  first_name,
  last_name
FROM
  customer
ORDER BY
  first_name ASC,
  last_name DESC;


SELECT
  first_name,
  LENGTH(first_name) len
FROM
  customer
ORDER BY
  len DESC;

-- DISTINCT
CREATE TABLE colors(
  id SERIAL PRIMARY KEY,
  bcolor VARCHAR,
  fcolor VARCHAR
);


INSERT INTO
  colors (bcolor, fcolor)
VALUES
  ('red', 'red'),
  ('red', 'red'),
  ('red', NULL),
  (NULL, 'red'),
  (NULL, NULL),
  ('green', 'green'),
  ('blue', 'blue'),
  ('blue', 'blue');
select bcolor from colors;

SELECT
  DISTINCT bcolor
FROM
  colors
ORDER BY
  bcolor;

SELECT
  DISTINCT bcolor, fcolor
FROM
  colors
ORDER BY
  bcolor,
  fcolor;

-- WHERE  filtering
-- 1
SELECT
  last_name,
  first_name
FROM
  customer
WHERE
  first_name = 'Jamie';

-- 2 -- AND
SELECT
  last_name,
  first_name
FROM
  customer
WHERE
  first_name = 'Jamie'
  AND last_name = 'Rice';


-- 3 -- OR
SELECT
  first_name,
  last_name
FROM
  customer
WHERE
  last_name = 'Rodriguez'
  OR first_name = 'Adam';


-- 4 -- IN
SELECT
  first_name,
  last_name
FROM
  customer
WHERE
  first_name IN ('Ann', 'Anne', 'Annie');


-- 5 -- LIKE
SELECT
  first_name,
  last_name
FROM
  customer
WHERE
  first_name LIKE 'Ann%';

-- 6 -- BETWEEN

SELECT
  first_name,
  LENGTH(first_name) name_length
FROM
  customer
WHERE
  first_name LIKE 'A%'
  AND LENGTH(first_name) BETWEEN 3
  AND 5
ORDER BY
  name_length;

-- <> not equal
SELECT
  first_name,
  last_name
FROM
  customer
WHERE
  first_name LIKE 'Bra%'
  AND last_name <> 'Motley';



