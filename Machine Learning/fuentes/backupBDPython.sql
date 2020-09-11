--
-- PostgreSQL database dump
--

-- Dumped from database version 11.2
-- Dumped by pg_dump version 11.1

-- Started on 2020-01-24 01:23:26

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 196 (class 1259 OID 16556)
-- Name: empleados; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.empleados (
    id integer NOT NULL,
    nombres character varying(80) NOT NULL
);


ALTER TABLE public.empleados OWNER TO postgres;

--
-- TOC entry 197 (class 1259 OID 16559)
-- Name: vehculos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vehculos (
    id integer NOT NULL,
    "Tipo" character varying(10) NOT NULL,
    "Marca" character varying(30) NOT NULL,
    "Color" character varying(15) NOT NULL
);


ALTER TABLE public.vehculos OWNER TO postgres;

--
-- TOC entry 2808 (class 0 OID 16556)
-- Dependencies: 196
-- Data for Name: empleados; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.empleados (id, nombres) FROM stdin;
1	Jorge Salcedo Veracruz
2	Ernesto Gutierrez
3	Alejandro Londoño
4	Maria Sepulveda
5	Sergio Londoño
\.


--
-- TOC entry 2809 (class 0 OID 16559)
-- Dependencies: 197
-- Data for Name: vehculos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vehculos (id, "Tipo", "Marca", "Color") FROM stdin;
1	Moto	Yamaha	Azul
2	Moto	Suzuki	Negra
3	Moto	Honda	Gris
4	Carro	Mazsa	Rojo
5	Carro	Toyota	blanca
6	Moto	AKT	Negra
7	Carro	Renault	abano
8	Carro	Chevrolet	azul
\.


-- Completed on 2020-01-24 01:23:27

--
-- PostgreSQL database dump complete
--

