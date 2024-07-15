-- Data source : https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data/data

select * from carsales limit 10;
drop table carsales_valid;

Create temporary table carsales_valid as  
SELECT
"YEAR" as manufactured_year,
make,
model,
trim,
body,
transmission,
vin,
state,
case when condition is null then 0
else condition
end as car_condition,
case when odometer is null then 0
else odometer
end as odometer_valid,
color,
interior,
seller,
mmr,
sellingprice,
saledate,
substr(saledate, 12, 4) as sale_year,
substr(saledate, 5, 3) as sale_monthname,
substr(saledate, 9, 2) as sale_day,
case substr(saledate,5,3)
when 'Jan' then 1
when 'Feb' then 2
when 'Mar' then 3
when 'Apr' then 4
when 'May' then 5
when 'Jun' then 6
when 'Jul' then 7
when 'Aug' then 8
when 'Sep' then 9
when 'Oct' then 10
when 'Nov' then 11
when 'Dec' then 12
else Null
end as sale_month
from carsales
where 
length(state)<=2
and make <> ''
and saledate is not null;

--Q1: Sales in each state
select state,
count(*)
from carsales_valid
group by 1;

--Q2: make and model
select
make,
model,
count(*)
from carsales_valid
group by 1,2
order by count(*) desc;

--Q3: Avg state prices
select
state,
avg(sellingprice) as avg_selling_price
from carsales_valid
group by 1
order by avg_selling_price asc;

--Q4: avg prices per month
select
sale_year,
sale_month,
avg(sellingprice) as avg_selling_price
from carsales_valid
group by 1,2
order by 1,2;

--Q5: num sales each month
select
sale_month,
count(*)
from carsales_valid
group by 1
order by 1;

--Q6: Top 5 models for each body type
select *
from (
    select
    make,
    model,
    body,
    count(*) as num_sales,
    rank() over(partition by body order by count(*) desc) body_rank
    from carsales_valid
    group by 1,2,3
    order by body asc, num_sales desc
    )s
where body_rank <=5;

--Q7: sales higher than model avg
select
make,
model,
vin,
sale_year,
sale_month,
sale_day,
sellingprice,
avg_model,
sellingprice/avg_model as price_ratio
from (
    select 
    make,
    model,
    vin,
    sale_year,
    sale_month,
    sale_day,
    sellingprice,
    avg(sellingprice) over (partition by make, model) as avg_model,
    
    from carsales_valid
    ) s
where sellingprice > avg_model
order by price_ratio desc;


--Q8 : condition and sales price   
select
case
when car_condition between 0 and 9 then '0-9'
when car_condition between 10 and 19 then '10-19'
when car_condition between 20 and 29 then '20-29'
when car_condition between 30 and 39 then '30-39'
when car_condition between 40 and 49 then '40-49'
END as car_condition_bucket,
count(*) as num_sales,
avg(sellingprice) as avg_selling_price
from carsales_valid
group by car_condition_bucket
order by car_condition_bucket;

--Q9: odometer and sales price
select
case
when odometer_valid < 100000 then '0 - 99 999'
when odometer_valid < 200000 then '100 000 - 199 999'
when odometer_valid < 300000 then '200 000 - 299 999'
when odometer_valid < 400000 then '300 000 - 399 999'
when odometer_valid < 500000 then '400 000 - 499 999'
when odometer_valid < 600000 then '500 000 - 599 999'
when odometer_valid < 700000 then '600 000 - 699 999'
when odometer_valid < 800000 then '700 000 - 799 999'
when odometer_valid < 900000 then '800 000 - 899 999'
when odometer_valid < 1000000 then '900 000 - 999 999'
end as odometer_bucket,
count(*) as num_sales,
avg(sellingprice) as avg_selling_price
from carsales_valid
group by odometer_bucket
order by odometer_bucket asc;

--Q10: brand details
select
make,
count(distinct model) as num_models,
count(*) as num_sales,
min(sellingprice) as min_price,
max(sellingprice) as max_price,
avg(sellingprice) as avg_selling_price
from carsales_valid
group by make
order by avg_selling_price desc;

--Q11: cars sold multiple
select *
from(
    select *, count(*) over(partition by vin) as vin_sales
    from carsales_valid
    )s
where vin_sales > 1
order by vin;