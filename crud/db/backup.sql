PGDMP  *                    |            crud_finanzas    16.3    16.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                        0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16411    crud_finanzas    DATABASE     �   CREATE DATABASE crud_finanzas WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Argentina.1252';
    DROP DATABASE crud_finanzas;
                postgres    false            �            1259    16497    gastos    TABLE     �   CREATE TABLE public.gastos (
    id integer NOT NULL,
    usuario_id integer,
    fecha date NOT NULL,
    monto numeric(10,2) NOT NULL,
    categoria character varying(50) NOT NULL,
    descripcion text
);
    DROP TABLE public.gastos;
       public         heap    postgres    false            �            1259    16496    gastos_id_seq    SEQUENCE     �   CREATE SEQUENCE public.gastos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.gastos_id_seq;
       public          postgres    false    220                       0    0    gastos_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.gastos_id_seq OWNED BY public.gastos.id;
          public          postgres    false    219            �            1259    16483    ingresos    TABLE     �   CREATE TABLE public.ingresos (
    id integer NOT NULL,
    usuario_id integer,
    fecha date NOT NULL,
    monto numeric(10,2) NOT NULL,
    categoria character varying(50) NOT NULL,
    descripcion text
);
    DROP TABLE public.ingresos;
       public         heap    postgres    false            �            1259    16482    ingresos_id_seq    SEQUENCE     �   CREATE SEQUENCE public.ingresos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.ingresos_id_seq;
       public          postgres    false    218                       0    0    ingresos_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.ingresos_id_seq OWNED BY public.ingresos.id;
          public          postgres    false    217            �            1259    16472    usuarios    TABLE     �   CREATE TABLE public.usuarios (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL,
    apellido character varying(100) NOT NULL,
    email character varying(255) NOT NULL,
    password character varying(255) NOT NULL
);
    DROP TABLE public.usuarios;
       public         heap    postgres    false            �            1259    16471    usuarios_id_seq    SEQUENCE     �   CREATE SEQUENCE public.usuarios_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.usuarios_id_seq;
       public          postgres    false    216                       0    0    usuarios_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.usuarios_id_seq OWNED BY public.usuarios.id;
          public          postgres    false    215            \           2604    16500 	   gastos id    DEFAULT     f   ALTER TABLE ONLY public.gastos ALTER COLUMN id SET DEFAULT nextval('public.gastos_id_seq'::regclass);
 8   ALTER TABLE public.gastos ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    220    219    220            [           2604    16486    ingresos id    DEFAULT     j   ALTER TABLE ONLY public.ingresos ALTER COLUMN id SET DEFAULT nextval('public.ingresos_id_seq'::regclass);
 :   ALTER TABLE public.ingresos ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    218    218            Z           2604    16475    usuarios id    DEFAULT     j   ALTER TABLE ONLY public.usuarios ALTER COLUMN id SET DEFAULT nextval('public.usuarios_id_seq'::regclass);
 :   ALTER TABLE public.usuarios ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    216    216            �          0    16497    gastos 
   TABLE DATA           V   COPY public.gastos (id, usuario_id, fecha, monto, categoria, descripcion) FROM stdin;
    public          postgres    false    220   �       �          0    16483    ingresos 
   TABLE DATA           X   COPY public.ingresos (id, usuario_id, fecha, monto, categoria, descripcion) FROM stdin;
    public          postgres    false    218   �       �          0    16472    usuarios 
   TABLE DATA           I   COPY public.usuarios (id, nombre, apellido, email, password) FROM stdin;
    public          postgres    false    216   �                  0    0    gastos_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.gastos_id_seq', 1, true);
          public          postgres    false    219                       0    0    ingresos_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.ingresos_id_seq', 7, true);
          public          postgres    false    217                       0    0    usuarios_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.usuarios_id_seq', 8, true);
          public          postgres    false    215            d           2606    16504    gastos gastos_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.gastos
    ADD CONSTRAINT gastos_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.gastos DROP CONSTRAINT gastos_pkey;
       public            postgres    false    220            b           2606    16490    ingresos ingresos_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.ingresos
    ADD CONSTRAINT ingresos_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.ingresos DROP CONSTRAINT ingresos_pkey;
       public            postgres    false    218            ^           2606    16481    usuarios usuarios_email_key 
   CONSTRAINT     W   ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_email_key UNIQUE (email);
 E   ALTER TABLE ONLY public.usuarios DROP CONSTRAINT usuarios_email_key;
       public            postgres    false    216            `           2606    16479    usuarios usuarios_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.usuarios DROP CONSTRAINT usuarios_pkey;
       public            postgres    false    216            f           2606    16505    gastos gastos_usuario_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.gastos
    ADD CONSTRAINT gastos_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id);
 G   ALTER TABLE ONLY public.gastos DROP CONSTRAINT gastos_usuario_id_fkey;
       public          postgres    false    4704    216    220            e           2606    16491 !   ingresos ingresos_usuario_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.ingresos
    ADD CONSTRAINT ingresos_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id);
 K   ALTER TABLE ONLY public.ingresos DROP CONSTRAINT ingresos_usuario_id_fkey;
       public          postgres    false    216    4704    218            �   8   x�3�4�4202�50�54�0�30���-(M-.�/�����/)�L*-������ ��      �   �   x���A
�0����@J�6�2n��P"1#����^�R��.�}><�o����7v0�omc-����PG��|e}��8���ax�δZ���W�9S�3��ha��;�7���V��D�>�aI\�� ��DVá��:�3��5e=r*�N_��]���h��E�����W;      �   �  x�}�;o[1�g�wx$Q�HOA��6(Ѕ���6~վ6Z���힅8��ǃ���i������!�_�:m�l�]����0�!�5������뤗×�l��+�AC�.���ACČX�	F��� P#�w-7U�7��JϽKl�z&lЬB�f��	tC�`�!!��Q�[��{��a�^����-7���a�<?\f���������%q� EJq
��Y� !��"�ͱ�`�\�bk�+;��)��M=Yʃ�k�޲Ak.5�Hf(-�S������0�Џ��O�u�+~{~�����'�L+�Fj� rɹ0{)����4!�ٔ�rN@%W���,LR�+
I��ɺ2�(9���2sժ܉-��W��hQXi@/��-�˿]8��     