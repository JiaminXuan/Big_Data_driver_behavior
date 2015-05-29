-- *************** TASK 1 ****************

CREATE TABLE trips (
medallion varchar(50),
hack_license varchar(50),
vendor_id VARCHAR(3),
rate_code SMALLINT,
store_and_fwd_flag VARCHAR(3),
pickup_datetime TIMESTAMP,
dropoff_datetime TIMESTAMP,
passenger_count SMALLINT,
trip_time_in_secs INT,
trip_distance DECIMAL(12,5),
pickup_longitude DECIMAL(15,10),
pickup_latitude DECIMAL(15,10),
dropoff_longitude DECIMAL(15,10),
dropoff_latitude DECIMAL(15,10)
);

CREATE TABLE fares (
       medallion varchar(50),
       hack_license varchar(50),
       vendor_id VARCHAR(3),
       pickup_datetime TIMESTAMP,
       payment_type VARCHAR(3),
       fare_amount DECIMAL(15,10),
       surcharge DECIMAL(15,10),
       mta_tax DECIMAL(15,10),
       tip_amount DECIMAL(15,10),
       tolls_amount DECIMAL(15,10),
       total_amount DECIMAL(15,10)
);

LOAD DATA LOCAL INFILE 'trip_data_week1.csv' 
INTO TABLE trips 
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;
LOAD DATA LOCAL INFILE 'fare_data_week1.csv' 
INTO TABLE fares 
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;
create index trips_idx 
       on trips(medallion,hack_license,vendor_id,pickup_datetime);
create index fares_idx 
       on fares(medallion,hack_license,vendor_id,pickup_datetime);
create table alltrips 
       select * 
       from trips natural join fares;