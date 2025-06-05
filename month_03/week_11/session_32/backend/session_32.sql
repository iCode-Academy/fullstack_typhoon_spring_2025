-- session 32

-- actor доторх бүх датаг харъя

select * from actor;

-- city доторх бүх датаг харъя
select * from city;

-- country доторх бүх датаг харъя
select * from country;

-- filter where clause
-- United states-ийг сонгоно уу

select * from country where country = 'United States';

-- country_id нь 93 байгаа улсыг харуулна уу
select * from country where country_id = 93;

-- actor_id нь 5 гэсэн жүжигчинг харуулна уу
select * from actor where actor_id = 5;

-- country_id нь 93 байгаа хотуудыг харуулна уу
select * from city where country_id = 93;

-- india гэдэг улсыг хотуудыг харуулна уу
select * from country where country = 'India';
select * from city where country_id = 44;

-- JOIN
select * from city c
join country co
on co.country_id = c.country_id;


select c.city, co.country from city c
join country co
on co.country_id = c.country_id;

-- Examples
CREATE TABLE basket_a (
    a INT PRIMARY KEY,
    fruit_a VARCHAR (100) NOT NULL
);
CREATE TABLE basket_b (
    b INT PRIMARY KEY,
    fruit_b VARCHAR (100) NOT NULL
);

INSERT INTO basket_a (a, fruit_a)
VALUES
    (1, 'Apple'),
    (2, 'Orange'),
    (3, 'Banana'),
    (4, 'Cucumber');

INSERT INTO basket_b (b, fruit_b)
VALUES
    (1, 'Orange'),
    (2, 'Apple'),
    (3, 'Watermelon'),
    (4, 'Pear');

select * from basket_a ba ;
select * from basket_b b;

-- JOIN буюу INNER JOIN
SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
INNER JOIN basket_b
    ON fruit_a = fruit_b;

-- LEFT JOIN
SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
LEFT JOIN basket_b
   ON fruit_a = fruit_b;


-- LEFT ANTI JOIN
SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
LEFT JOIN basket_b
    ON fruit_a = fruit_b
WHERE b IS NULL;

-- RIGHT JOIN
SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
RIGHT JOIN basket_b ON fruit_a = fruit_b;

-- FULL OUTER JOIN
SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
FULL OUTER JOIN basket_b
    ON fruit_a = fruit_b;

-- FULL JOIN
SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
FULL JOIN basket_b
   ON fruit_a = fruit_b
WHERE a IS NULL OR b IS NULL;

-- Exercises 
-- customer id, нэр болон овгийг төлсөн payment amount болон хэддэх өдөр төлсөн бэ
-- гэдгийг нь  бүх датаг  харуулсан query бичнэ үү. INNER JOIN ашиглаарай.
/*
customer_id | first_name  |  last_name   | amount |        payment_date
-------------+-------------+--------------+--------+----------------------------
         416 | Jeffery     | Pinson       |   2.99 | 2007-02-14 21:21:59.996577
         516 | Elmer       | Noe          |   4.99 | 2007-02-14 21:23:39.996577
         239 | Minnie      | Romero       |   4.99 | 2007-02-14 21:29:00.996577
         592 | Terrance    | Roush        |   6.99 | 2007-02-14 21:41:12.996577
          49 | Joyce       | Edwards      |   0.99 | 2007-02-14 21:44:52.996577
...
*/

SELECT
  c.customer_id,
  c.first_name,
  c.last_name,
  p.amount,
  p.payment_date
FROM
  customer c
  INNER JOIN payment p ON p.customer_id = c.customer_id
ORDER BY
  c.customer_id asc;

-- Exercises
SELECT
  c.customer_id,
  c.first_name || ' ' || c.last_name as customer_name,
  s.first_name || ' ' || s.last_name as staff_name,
  p.amount,
  p.payment_date
FROM
  customer c
  INNER JOIN payment p USING (customer_id)
  INNER JOIN staff s using(staff_id)
ORDER BY
  payment_date;


-- LEFT JOIN
-- film_id, film title, inventory_id-г нь харуулсан киноны title-аар нь 
-- буурах дарааллаар харуулах query бичнэ үү.
SELECT
  film.film_id,
  film.title,
  inventory.inventory_id
FROM
  film
  LEFT JOIN inventory ON inventory.film_id = film.film_id
ORDER BY
  film.title;

-- тухайн кино нь film_id нь NULL байгаа бүх датаг харуулна уу. Дээрх шиг
-- film_id, film title, inventory_id-г cонгож харуулаарай.

SELECT
  film.film_id,
  inventory.inventory_id,
  film.title
FROM
  film
  LEFT JOIN inventory using(film_id)
where
	inventory.inventory_id  is null
ORDER BY
  film.title;

-- 

