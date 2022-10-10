DROP TABLE manufactures;
DROP TABLE desks;
DROP TABLE djequips;
DROP TABLE mics;

CREATE TABLE mics (
    id SERIAL PRIMARY KEY,
    manufacture VARCHAR(255), 
    model VARCHAR(255),
    description TEXT,
    stock_count INT,
    trade_price FLOAT,
    sale_price FLOAT
);

CREATE TABLE desks (
    id SERIAL PRIMARY KEY,
    manufacture VARCHAR(255), 
    model VARCHAR(255),
    description TEXT,
    stock_count INT,
    trade_price FLOAT,
    sale_price FLOAT
);

CREATE TABLE djequips (
    id SERIAL PRIMARY KEY,
    manufacture VARCHAR(255), 
    model VARCHAR(255),
    description TEXT,
    stock_count INT,
    trade_price FLOAT,
    sale_price FLOAT
);

CREATE TABLE manufactures (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    mic_id INT REFERENCES mics(id) ON DELETE CASCADE,
    djequip_id INT REFERENCES djequips(id) ON DELETE CASCADE,
    desk_id INT REFERENCES desks(id) ON DELETE CASCADE
)