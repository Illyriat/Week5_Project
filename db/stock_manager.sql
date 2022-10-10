DROP TABLE manufactures;
DROP TABLE products;
DROP TABLE types;

CREATE TABLE types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE manufactures (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    model VARCHAR(255),
    description TEXT,
    stock_count INT,
    trade_price FLOAT,
    sale_price FLOAT,
    manufactures_id INT REFERENCES manufactures(id) ON DELETE CASCADE,
    types_id INT REFERENCES types(id) ON DELETE CASCADE
);