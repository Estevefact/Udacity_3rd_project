CREATE EXTERNAL TABLE IF NOT EXISTS `stedi`.`step_trainer` (
    `serialnumber` string,
    `sensorReadingTime` bigint,
    `distanceFromObject` bigint,
    `.serialnumber` string,
    `sharewithpublicasofdate` bigint,
    `birthday` string,
    `registrationDate` bigint,
    `sharewithResearchasofDate` bigint,
    `customerName` string,
    `email` string,
    `lastUpdateDate` bigint,
    `phone` string,
    `sharewithfriendsasofdate` bigint
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES(
    'serialization.format' = '1'
) LOCATION 's3://project-stedi-eva/step_trainer/trusted/'
TBLPROPERTIES ('has_encrypted_data'='false');