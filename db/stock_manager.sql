DROP TABLE manufacture;
DROP TABLE desk;
DROP TABLE djequip;
DROP TABLE mic;

-- FOREIGN ID's STILL TO PLACE

CREATE TABLE mic (
    id SERIAL PRIMARY KEY,
    manufacture VARCHAR(255), 
    model VARCHAR(255),
    description TEXT,
    stock_count INT
    trade_price FLOAT,
    sale_price FLOAT
);

CREATE TABLE desk (
    id SERIAL PRIMARY KEY,
    manufacture VARCHAR(255), 
    model VARCHAR(255),
    description TEXT,
    stock_count INT
    trade_price FLOAT,
    sale_price FLOAT
);

CREATE TABLE djequip (
    id SERIAL PRIMARY KEY,
    manufacture VARCHAR(255), 
    model VARCHAR(255),
    description TEXT,
    stock_count INT
    trade_price FLOAT,
    sale_price FLOAT
);

CREATE TABLE manufacture (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    mic_id INT REFERENCES mic(id) ON DELETE CASCADE,
    djequip_id INT REFERENCES djqeuip(id) ON DELETE CASCADE,
    desk_id INT REFERENCES desk(id) ON DELETE CASCADE
);


