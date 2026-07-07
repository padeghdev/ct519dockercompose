--
-- PostgreSQL database cluster dump
--

-- Started on 2026-07-07 09:24:59 UTC

\restrict Z7JKelhPXDKvAGgXXhazsAtn5Ggq8vO0Lm76NRkIr91mKdeDJeIVlDwDyv4wJdE

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Roles
--

CREATE ROLE myuser;
ALTER ROLE myuser WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'SCRAM-SHA-256$4096:TKHyscwlFyvHn6NAdq7jbg==$e+fj1YjoTZZzc/l3CQ1OxPm6cTJ/gQnbr06KtjLPtq4=:ou70KU/IOzJ7fulrf+kzLzXBE3e/ZryptjnGtl342rY=';

--
-- User Configurations
--








\unrestrict Z7JKelhPXDKvAGgXXhazsAtn5Ggq8vO0Lm76NRkIr91mKdeDJeIVlDwDyv4wJdE

--
-- Databases
--

--
-- Database "template1" dump
--

\connect template1

--
-- PostgreSQL database dump
--

\restrict UohlgacHzj36cWZ3pSKoeyHL4c0m4yp62vT0erIXMwR4zV4wTi6a70VajeEN4nr

-- Dumped from database version 15.18 (Debian 15.18-1.pgdg13+1)
-- Dumped by pg_dump version 15.18

-- Started on 2026-07-07 09:24:59 UTC

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

-- Completed on 2026-07-07 09:25:00 UTC

--
-- PostgreSQL database dump complete
--

\unrestrict UohlgacHzj36cWZ3pSKoeyHL4c0m4yp62vT0erIXMwR4zV4wTi6a70VajeEN4nr

--
-- Database "mydatabase" dump
--

--
-- PostgreSQL database dump
--

\restrict 1CvCuFl72xHa0Xp6MWL0pJZ0iDLgZS0yP6PG7j3ca9jaPGc1jYbeybNslTKcF1l

-- Dumped from database version 15.18 (Debian 15.18-1.pgdg13+1)
-- Dumped by pg_dump version 15.18

-- Started on 2026-07-07 09:25:00 UTC

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3414 (class 1262 OID 16384)
-- Name: mydatabase; Type: DATABASE; Schema: -; Owner: myuser
--

CREATE DATABASE mydatabase WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';


ALTER DATABASE mydatabase OWNER TO myuser;

\unrestrict 1CvCuFl72xHa0Xp6MWL0pJZ0iDLgZS0yP6PG7j3ca9jaPGc1jYbeybNslTKcF1l
\connect mydatabase
\restrict 1CvCuFl72xHa0Xp6MWL0pJZ0iDLgZS0yP6PG7j3ca9jaPGc1jYbeybNslTKcF1l

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 16390)
-- Name: custom; Type: TABLE; Schema: public; Owner: myuser
--

CREATE TABLE public.custom (
    cid bigint NOT NULL,
    cname text,
    address text
);


ALTER TABLE public.custom OWNER TO myuser;

--
-- TOC entry 214 (class 1259 OID 16389)
-- Name: custom_cid_seq; Type: SEQUENCE; Schema: public; Owner: myuser
--

ALTER TABLE public.custom ALTER COLUMN cid ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.custom_cid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 3408 (class 0 OID 16390)
-- Dependencies: 215
-- Data for Name: custom; Type: TABLE DATA; Schema: public; Owner: myuser
--

COPY public.custom (cid, cname, address) FROM stdin;
1	AAA	123  wireless rd 10100
2	BBB	345  wireless rd 10100
\.


--
-- TOC entry 3415 (class 0 OID 0)
-- Dependencies: 214
-- Name: custom_cid_seq; Type: SEQUENCE SET; Schema: public; Owner: myuser
--

SELECT pg_catalog.setval('public.custom_cid_seq', 2, true);


--
-- TOC entry 3264 (class 2606 OID 16394)
-- Name: custom custom_pkey; Type: CONSTRAINT; Schema: public; Owner: myuser
--

ALTER TABLE ONLY public.custom
    ADD CONSTRAINT custom_pkey PRIMARY KEY (cid);


-- Completed on 2026-07-07 09:25:00 UTC

--
-- PostgreSQL database dump complete
--

\unrestrict 1CvCuFl72xHa0Xp6MWL0pJZ0iDLgZS0yP6PG7j3ca9jaPGc1jYbeybNslTKcF1l

--
-- Database "postgres" dump
--

\connect postgres

--
-- PostgreSQL database dump
--

\restrict gIEFQuj2ybdeLM5s7KDU7r7Ob6MwsTnRW02edyfdpe7pOHnZgThPZvbAbL4E0Zz

-- Dumped from database version 15.18 (Debian 15.18-1.pgdg13+1)
-- Dumped by pg_dump version 15.18

-- Started on 2026-07-07 09:25:00 UTC

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

-- Completed on 2026-07-07 09:25:00 UTC

--
-- PostgreSQL database dump complete
--

\unrestrict gIEFQuj2ybdeLM5s7KDU7r7Ob6MwsTnRW02edyfdpe7pOHnZgThPZvbAbL4E0Zz

-- Completed on 2026-07-07 09:25:00 UTC

--
-- PostgreSQL database cluster dump complete
--

