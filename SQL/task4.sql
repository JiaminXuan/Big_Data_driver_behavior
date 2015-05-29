-- ************ TASK 4 ****************
CREATE TABLE medallions (
       medallion varchar(50),
       name varchar(75),
       type varchar(30),
       current_status varchar(10),
       DMV_license_plate varchar(10),
       vehicle_VIN_number varchar(20),
       vehicle_type varchar(10),
       model_year DECIMAL(4),
       medallion_type varchar(30),
       agent_number INTEGER,
       agent_name varchar(50),
       agent_telephone_number varchar(15),
       agent_website varchar(50),
       agent_address varchar(75),
       last_updated_date DATE,
       last_updated_time TIME
);
LOAD DATA LOCAL INFILE 'licenses.txt' 
INTO TABLE trips 
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;
create index alltrips_idx 
       on alltrips(medallion);
create table finaltable 
select * 
from alltrips natural join medallions;

-- ************ TASK 4A****************
select vehicle_type, 
sum(trip_distance) total_trips, 
sum(total_amount) total_revenue,
avg(tip_amount/total_amount)*100 avg_tip_percentage 
from finaltable 
group by vehicle_type;
-- ************ TASK 4B****************
select medallion_type, 
sum(trip_distance) total_trips, 
sum(total_amount) total_revenue,
avg(tip_amount/total_amount)*100 avg_tip_percentage 
from finaltable 
group by medallion_type;
-- ************ TASK 4C****************
select agent_name, 
sum(total_amount) total_revenue 
from finaltable 
group by agent_name 
order by total_revenue desc 
limit 10;
