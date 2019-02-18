BEGIN;
--
-- Create model User
--
CREATE TABLE IF NOT EXISTS "users" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"login" varchar(200) NOT NULL, 
	"money_amount" integer NOT NULL, 
	"card_number" varchar(16) NOT NULL, 
	"status" bool NOT NULL
	);
--
-- Create model User_data
--
CREATE TABLE IF NOT EXISTS "firsql_user_data" (
	"user_id" integer NOT NULL PRIMARY KEY REFERENCES "users" ("id") DEFERRABLE INITIALLY DEFERRED, 
	"pwd" varchar(200) NOT NULL
	);
COMMIT;

INSERT INTO "users" VALUES(1,'admin',100500,'4024007170060940',1);
INSERT INTO "firsql_user_data" VALUES(1,'B@d_Pa$$word');

INSERT INTO "users" VALUES(2,'valera',7,'4829425780454294',0);
INSERT INTO "firsql_user_data" VALUES(2,'s4bFU$e');

INSERT INTO "users" VALUES(3,'tolyan',55,'4024007114750481',1);
INSERT INTO "firsql_user_data" VALUES(3,'sheU*fh4');

INSERT INTO "users" VALUES(4,'mary',99,'4532059785042628',1);
INSERT INTO "firsql_user_data" VALUES(4,'mary12345');

INSERT INTO "users" VALUES(5,'sandra',555,'4539572904903739',0);
INSERT INTO "firsql_user_data" VALUES(5,'sdn*fdS11');

INSERT INTO "users" VALUES(6,'kevin',0,'4556166066186445',1);
INSERT INTO "firsql_user_data" VALUES(6,'glukozavr55');
