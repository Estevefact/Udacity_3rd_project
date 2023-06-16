CREATE EXTERNAL TABLE IF NOT EXISTS `stedi`.`step_trainer` (
    `serialnumber` string,
    `z`	float,
    `sensorReadingTime` bigint,
    `distanceFromObject` bigint,
    `sharewithpublicasofdate` bigint,
    `birthday` string,
    `registrationDate` bigint,
    `sharewithResearchasofDate` bigint,
    `customerName` string,
    `email` string,
    `lastUpdateDate` bigint,
    `phone` string,
    `sharewithfriendsasofdate` bigint,
    `x` float,
    `y` float,
    `user` string
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES(
    'serialization.format' = '1'
) LOCATION 's3://project-stedi-eva/accelerator/curated/'
TBLPROPERTIES ('has_encrypted_data'='false');