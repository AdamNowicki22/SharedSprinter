DROP TABLE sprinter;

CREATE TABLE sprinter
(id SERIAL PRIMARY KEY,
title VARCHAR(30),
user_story VARCHAR(255),
acceptance_criteria VARCHAR(255),
business_value INTEGER,
estimation INTEGER,
status VARCHAR(30));