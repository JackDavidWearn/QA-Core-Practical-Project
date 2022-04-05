CREATE TABLE IF NOT EXISTS cards (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cards_value VARCHAR(20) NOT NULL,
    cards_suit VARCHAR(20) NOT NULL, 
    date_generated DATE NOT NULL
);