DROP TABLE IF EXISTS search_item;

DROP TABLE IF EXISTS search_content;

CREATE TABLE search_item (
	uid INT (4) PRIMARY KEY NOT NULL auto_increment,
	content VARCHAR (32) NOT NULL
);


CREATE TABLE search_content (
	id VARCHAR (32) ,
	NAME VARCHAR (256) ,
	url VARCHAR (256) ,
	type VARCHAR (32) ,
	time VARCHAR (32) ,
	file VARCHAR (32) ,
	hot VARCHAR (32) 
);

ALTER TABLE search_item CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
ALTER TABLE search_content CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
