-- postgres=# \d datasets
--                    Table "public.datasets"
--  Column |       Type        | Collation | Nullable | Default 
-- --------+-------------------+-----------+----------+---------
--  id     | character varying |           | not null | 
--  name   | character varying |           |          | 
-- Indexes:
--     "datasets_pkey" PRIMARY KEY, btree (id)


-- postgres=# \d entries
--                      Table "public.entries"
--    Column   |       Type        | Collation | Nullable | Default 
-- ------------+-------------------+-----------+----------+---------
--  id         | character varying |           | not null | 
--  label      | character varying |           |          | 
--  status     | character varying |           |          | 
--  dataset_id | character varying |           |          | 
-- Indexes:
--     "entries_pkey" PRIMARY KEY, btree (id)


-- populate the two tables with dummy data

INSERT INTO datasets (id, name) VALUES ('1', 'dataset1');
INSERT INTO datasets (id, name) VALUES ('2', 'dataset2');
INSERT INTO datasets (id, name) VALUES ('3', 'dataset3');
INSERT INTO datasets (id, name) VALUES ('4', 'dataset4');

INSERT INTO entries (id, label, status, dataset_id) VALUES ('1', 'entry1', 'active', '1');
INSERT INTO entries (id, label, status, dataset_id) VALUES ('2', 'entry2', 'active', '1');
INSERT INTO entries (id, label, status, dataset_id) VALUES ('3', 'entry3', 'active', '1');
INSERT INTO entries (id, label, status, dataset_id) VALUES ('4', 'entry4', 'active', '1');
INSERT INTO entries (id, label, status, dataset_id) VALUES ('5', 'entry5', 'active', '2');
INSERT INTO entries (id, label, status, dataset_id) VALUES ('6', 'entry6', 'active', '2');
