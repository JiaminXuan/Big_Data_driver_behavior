-- ************ TASK 3A ****************
-- yes there are more than one record for a given taxi at the same time
-- it might be caused by replicating lisence by illegal drivers.
select medallion, pickup_datetime,count(*) 
from trips 
group by medallion ,pickup_datetime 
order by count(*) desc 
limit 10;
-- ************ TASK 3B ****************
select medallion,sum(
	case when trips.pickup_longitude=0 
	and trips.pickup_latitude=0 
	and trips.dropoff_longitude=0 
	and trips.dropoff_latitude=0 then 1 else 0 end)/count(*)*100 as percentage_of_trips 
from trips 
group by medallion 
order by percentage_of_trips; 
-- ************ TASK 3C ****************
-- as we can see from the result, some drivers use many taxis
select t1.hack_license drivers, count(*) num_taxis
from (
	select medallion,hack_license 
	from trips 
	group by hack_license,medallion) t1 
group by hack_license;
