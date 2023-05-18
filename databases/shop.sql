CREATE TABLE items (
    id INTEGER NOT NULL AUTO_INCREMENT,
    phone_name VARCHAR(100) CHARACTER SET utf16 NOT NULL ,
    price DECIMAL(10, 2) NOT NULL,
    ram_size INT NOT NULL,
    benchmark_score INT NOT NULL,
    battery_size INT NOT NULL,
    image_path VARCHAR(100) CHARACTER SET utf8,
    PRIMARY KEY (id)
);

--
-- CREATE TABLE users (
--     user_id INTEGER NOT NULL AUTO_INCREMENT
-- );
--
-- CREATE TABLE user_cart (
--     entry_id INTEGER NOT NULL AUTO_INCREMENT,
--     user_id INTEGER NOT NULL,
--     phone_id INTEGER NOT NULL,
--     PRIMARY KEY (id),
--     FOREIGN KEY (phone_id) REFERENCES items (phone_id),
--     FOREIGN KEY (user_id) REFERENCES users (user_id),
-- );

INSERT INTO items (phone_name, price, ram_size, benchmark_score, battery_size, image_path)
VALUES ROW('iPhone 11', 1000, 4, 3000, 3000, 'iphone11.jpg'),
       ROW('iPhone 12', 1500, 5, 5000, 3200, 'iphone12.jpg'),
       ROW('iPhone 13', 2000, 6, 7000, 3400, 'iphone13.jpeg');
