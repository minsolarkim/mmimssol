BEGIN TRANSACTION;
CREATE TABLE PhoneBook (Name text, PhoneNum test);
INSERT INTO "PhoneBook" VALUES('derick','010-111');
INSERT INTO "PhoneBook" VALUES('ona','010-999');
INSERT INTO "PhoneBook" VALUES('tom','010-123');
INSERT INTO "PhoneBook" VALUES('dsp','010-567');
COMMIT;
