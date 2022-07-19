CREATE SCHEMA public;

CREATE TABLE public.test (
	id int8 NULL,
	order_num int4 NULL,
	cost_dollar float4 NULL,
	delivery_date date NULL,
	cost_rub float8 NULL,
	CONSTRAINT test_un UNIQUE (id)
);


ALTER TABLE public.test OWNER TO postgres;
GRANT ALL ON TABLE public.test TO postgres;