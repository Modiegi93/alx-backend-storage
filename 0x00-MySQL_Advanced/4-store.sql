-- Creates a trigger to buy an item

CREATE TRIGGER DelQuantityConsult
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number
WHERE NEW.item_name = name;
