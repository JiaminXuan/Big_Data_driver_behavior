-- ************ TASK 2A ****************
select fare_amount amount, count(fare_amount) num_trips 
from fares 
group by amount 
order by num_trips desc;
-- ************ TASK 2B ****************
select count(*) 
from fares 
where total_amount<10;
-- ************ TASK 2C ****************
select passenger_count number_of_passenger,count(passenger_count ) num_trips 
from trips 
group by passenger_count;
-- ************ TASK 2D ****************
select date(pickup_datetime) day, sum(total_amount) total_revenue 
from fares 
group by date(pickup_datetime);
-- ************ TASK 2E ****************
select medallion, count(*) num_trips 
from trips 
group by medallion;
