-- session 33


-- aggregation function (Group By)


select
	-- distinct
	customer_id
from 
	payment
group by 
	customer_id 
order by 
	customer_id;

-- aggregation function (SUM)

select
	customer_id,
	SUM(amount) as summe
from 
	payment
group by
	customer_id
order by 
	summe asc;

-- LIMIT
-- which customer paid the most?
select
	customer_id,
	SUM(amount) as summe
from 
	payment
group by
	customer_id
order by 
	summe desc
limit 1;


-- JOIN

select
	p.customer_id,
	c.first_name,
	c.last_name,
	SUM(amount) as summe
from 
	payment p
left join 
	customer c
on
	c.customer_id  = p.customer_id
group by
	p.customer_id,
	c.first_name,
	c.last_name
order by 
	summe desc
limit 1;

-- count of customers
select count(*) from customer;

-- count of payments
select count(*) from payment;
-- count of staff
select count(*) from staff;



select 
	staff_id,
	count(payment_id)
from 
	payment
group by
	staff_id;

-- payment-ийг өдөр өдрийнх нь хэмжээгээр нь харуулна уу
-- payment_date | sum(amount)
--payment_date |   sum
--------------+---------
-- 2007-05-14   |  514.18
-- 2007-04-30   | 5723.89
-- 2007-04-29   | 2717.60
-- 2007-04-28   | 2622.73
--...

select 
	payment_date::date payment_date,
	sum(amount)
from 
	payment
group by
	payment_date::date
order by
	payment_date desc;

-- Having

SELECT
  customer_id,
  SUM (amount) amount
FROM
  payment
GROUP BY
  customer_id
having
	sum(amount) > 200
ORDER BY
  amount DESC;

-- customer id нь 300-гаас их, store_id-ны тоог олно уу

-- store_id | count
----------+-------
--        1 |   326

SELECT
  store_id,
  COUNT (customer_id)
FROM
  customer
GROUP BY
  store_id
HAVING
  COUNT (customer_id) > 300;

--- grouping sets
DROP TABLE IF EXISTS sales;

CREATE TABLE sales (
    brand VARCHAR NOT NULL,
    segment VARCHAR NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (brand, segment)
);

INSERT INTO sales (brand, segment, quantity)
VALUES
    ('ABC', 'Premium', 100),
    ('ABC', 'Basic', 200),
    ('XYZ', 'Premium', 100),
    ('XYZ', 'Basic', 300)
RETURNING *;
-- brand segment group 
SELECT
    brand,
    segment,
    SUM (quantity)
FROM
    sales
GROUP BY
    brand,
    segment;

-- brand group
SELECT
    brand,
    SUM (quantity)
FROM
    sales
GROUP BY
    brand;
-- segment group

SELECT
    segment,
    SUM (quantity)
FROM
    sales
GROUP BY
    segment;


-- solution
SELECT
    brand,
    segment,
    SUM (quantity)
FROM
    sales
GROUP BY
    GROUPING SETS (
        (brand, segment),
        (brand),
        (segment),
        ()
    );

