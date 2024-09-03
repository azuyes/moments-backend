CREATE TABLE public."MOMENT_USER"
(
id character varying NOT NULL,
username character varying NOT NULL,
phone_number character varying NOT NULL,
is_active boolean NOT NULL,
hashed_password character varying NOT NULL,
is_superuser boolean NOT NULL,
PRIMARY KEY (id)
);
ALTER TABLE IF EXISTS public."MOMENT_USER" OWNER to postgres;