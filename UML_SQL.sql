CREATE DATABASE joy_of_coding;
USE joy_of_coding;

CREATE TABLE `EPISODES` (
  `episode_id` integer PRIMARY KEY,
  `title` integer,
  `colors` varchar(255),
  `subjects` varchar(255),
  `month` varchar(255)
);

CREATE TABLE `EPISODE_COLORS` (
  `episode_id` integer PRIMARY KEY,
  `color_id` integer
);

CREATE TABLE `COLORS` (
  `color_id` integer,
  `color_name` integer
);

CREATE TABLE `SUBJECTS` (
  `subject_id` integer,
  `subject_name` varchar(255)
);

CREATE TABLE `EPISODE_SUBJECT` (
  `episode_id` interger PRIMARY KEY,
  `subject_id` interger
);

CREATE TABLE `EPISODE_AIR_DATE` (
  `month` varchar(255)
);

ALTER TABLE `EPISODE_COLORS` ADD FOREIGN KEY (`color_id`) REFERENCES `EPISODES` (`episode_id`);

ALTER TABLE `EPISODE_SUBJECT` ADD FOREIGN KEY (`subject_id`) REFERENCES `EPISODES` (`episode_id`);

CREATE TABLE `EPISODE_COLORS_COLORS` (
  `EPISODE_COLORS_color_id` integer,
  `COLORS_color_id` integer,
  PRIMARY KEY (`EPISODE_COLORS_color_id`, `COLORS_color_id`)
);

ALTER TABLE `EPISODE_COLORS_COLORS` ADD FOREIGN KEY (`EPISODE_COLORS_color_id`) REFERENCES `EPISODE_COLORS` (`color_id`);

ALTER TABLE `EPISODE_COLORS_COLORS` ADD FOREIGN KEY (`COLORS_color_id`) REFERENCES `COLORS` (`color_id`);


CREATE TABLE `EPISODE_SUBJECT_SUBJECTS` (
  `EPISODE_SUBJECT_subject_id` interger,
  `SUBJECTS_subject_id` integer,
  PRIMARY KEY (`EPISODE_SUBJECT_subject_id`, `SUBJECTS_subject_id`)
);

ALTER TABLE `EPISODE_SUBJECT_SUBJECTS` ADD FOREIGN KEY (`EPISODE_SUBJECT_subject_id`) REFERENCES `EPISODE_SUBJECT` (`subject_id`);

ALTER TABLE `EPISODE_SUBJECT_SUBJECTS` ADD FOREIGN KEY (`SUBJECTS_subject_id`) REFERENCES `SUBJECTS` (`subject_id`);


ALTER TABLE `EPISODE_AIR_DATE` ADD FOREIGN KEY (`month`) REFERENCES `EPISODES` (`month`);
