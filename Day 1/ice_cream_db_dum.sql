BEGIN TRANSACTION;
CREATE TABLE ice_cream_flavors (
        id INTEGER PRIMARY KEY,
        flavor TEXT,
        rating INTEGER
        );
INSERT INTO "ice_cream_flavors" VALUES(1,'chocolate',10);
INSERT INTO "ice_cream_flavors" VALUES(2,'strawberry',9);
INSERT INTO "ice_cream_flavors" VALUES(3,'pistachio',7.3);
INSERT INTO "ice_cream_flavors" VALUES(4,'hazelnut',7.5);
INSERT INTO "ice_cream_flavors" VALUES(5,'mocha',6);
INSERT INTO "ice_cream_flavors" VALUES(6,'Cherry',4);
INSERT INTO "ice_cream_flavors" VALUES(7,'Banana',7);
INSERT INTO "ice_cream_flavors" VALUES(8,'vanilla',7);
INSERT INTO "ice_cream_flavors" VALUES(9,'mint',2);
INSERT INTO "ice_cream_flavors" VALUES(10,'caramel',7);
CREATE TABLE toppings (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
INSERT INTO "toppings" VALUES(1,'sprinkles');
INSERT INTO "toppings" VALUES(2,'choco sauce');
INSERT INTO "toppings" VALUES(3,'nuts');
COMMIT;
