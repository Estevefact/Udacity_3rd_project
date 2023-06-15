CREATE EXTERNAL TABLE IF NOT EXISTS `stedi`.`step_trainer` (
    `serialnumber` string,
    `sensorReadingTime` bigint,
    `distanceFromObject` bigint
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES(
    'serialization.format' = '1'
) LOCATION 's3://project-stedi-eva/step_trainer/landing'
TBLPROPERTIES ('has_encrypted_data'='false');