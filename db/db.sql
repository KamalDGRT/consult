CREATE TABLE `user_type`(
    `ut_id` INT(11),
    `role_name` VARCHAR(256)
);

ALTER TABLE `user_type`
ADD
    PRIMARY KEY(`ut_id`);

ALTER TABLE `user_type`
    MODIFY
    `ut_id` INT(11) NOT NULL AUTO_INCREMENT;

CREATE TABLE `user` (
`user_id` INT(11) NOT NULL,
`user_name` VARCHAR(50),
`email` VARCHAR(256),
`password` VARCHAR(256),
`ut_id` INT(11)
);

ALTER TABLE `user`
ADD
    PRIMARY KEY(`user_id`);

ALTER TABLE `user`
    MODIFY
    `user_id` INT(11) NOT NULL AUTO_INCREMENT;

CREATE TABLE `doctor_data` (
`doctor_id` INT(11) NOT NULL,
`doctor_skill` VARCHAR(256),
`added_by` INT(11) NOT NULL
);

CREATE TABLE `patient_details` (
`patient_id` INT(11) NOT NULL,
`blood_type` VARCHAR(20)
);

CREATE TABLE `appointment`(
`app_id` INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
`patient_id` INT(11) NOT NULL,
`status` INT(2) DEFAULT 0,
`booked_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
`approved_at` DATETIME,
`accepted_by` INT(11) NOT NULL
);

INSERT INTO user (user_name, email, password, ut_id) VALUES ('Kamal', 'kamal@gmail.com', 'kamal', 1);

INSERT INTO doctor_data (doctor_id, doctor_skill, added_by) VALUES (3, "General", 1);
INSERT INTO doctor_data (doctor_id, doctor_skill, added_by) VALUES (4, "Neurologist", 1);

INSERT INTO patient_details (patient_id, blood_type) VALUES (2, "AB-ve");
