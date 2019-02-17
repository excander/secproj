BEGIN;
--
-- Create model User
--
CREATE TABLE "users" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	"login" varchar(200) NOT NULL, 
	"money_amount" integer NOT NULL, 
	"card_number" varchar(16) NOT NULL, 
	"status" bool NOT NULL
	);
--
-- Create model User_data
--
CREATE TABLE "firsql_user_data" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	"pwd" varchar(200) NOT NULL, 
	"user_id_id" integer NOT NULL REFERENCES "users" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE INDEX "firsql_user_data_user_id_id_f31ec673" ON "firsql_user_data" ("user_id_id");
COMMIT;
