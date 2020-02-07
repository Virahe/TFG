USE dev; -- USE test;

INSERT INTO `logscope_environment` (server, ip_address) VALUES
	('localhost', '127.0.0.1');
INSERT INTO `logscope_app` (name, description, server) VALUES
	('VPN', 'Virtual Private Network', NULL),
    ('Windows', 'Windows OS', 'localhost');
INSERT INTO `logscope_eventtype` (type, description) VALUES
	('log in', 'go through the procedures to begin use of an app'),
    ('log out', 'go through the procedures to conclude use of an app');
INSERT INTO `logscope_itemtype` (type, model) VALUES
	('Computer', 'Asus');
INSERT INTO `logscope_item` (ip_address, mac_address, item_type) VALUES
	('192.168.1.34', '91-C2-35-71-86-2B', 'Computer');
INSERT INTO `logscope_person` (name, login) VALUES
	('Adrián Pineda Miñón', 'Adrian'),
    ('Usuario Desconocido', 'Usuario');

-- Primary keys for this table may change, check actual values
-- INSERT INTO `logscope_personitems` (person_id, item_id) VALUES
	-- (1,1),
	-- (2,1);