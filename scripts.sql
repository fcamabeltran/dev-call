
CREATE TABLE desa_risk_ratios_hoy (
    raho_cod_riesgo smallint NOT NULL,
    raho_cod_dato smallint NOT NULL,
    raho_fec_riesgo date,
    raho_cat_dato character(6) NOT NULL,
    raho_dia_llamadas integer,
    raho_dia_minutos numeric,
    raho_ind_umb_llamadas numeric,
    raho_ind_umb_minutos numeric,
    raho_aye_llamadas integer,
    raho_aye_minutos numeric,
    raho_ind_aye_llamadas numeric,
    raho_ind_aye_minutos numeric,
    raho_avg_xda_llamadas numeric,
    raho_avg_xda_minutos numeric,
    raho_ind_avg_xda_llamadas numeric,
    raho_ind_avg_xda_minutos numeric,
    raho_avg_xdp_llamadas numeric,
    raho_avg_xdp_minutos numeric,
    raho_ind_avg_xdp_llamadas numeric,
    raho_ind_avg_xdp_minutos numeric,
    raho_dst_xda_llamadas numeric,
    raho_dst_xda_minutos numeric,
    raho_ind_dst_xda_llamadas numeric,
    raho_ind_dst_xda_minutos numeric,
    raho_dst_xdp_llamadas numeric,
    raho_dst_xdp_minutos numeric,
    raho_ind_dst_xdp_llamadas numeric,
    raho_ind_dst_xdp_minutos numeric DEFAULT 0,
    raho_where_coho character varying(250),
    raho_where_codi character(250),
    raho_where_tasa character(250)
);


ALTER TABLE public.desa_risk_ratios_hoy OWNER TO postgres;

--
-- TOC entry 165 (class 1259 OID 135322)
-- Dependencies: 1948 6
-- Name: desa_risk_trafico_cab; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE desa_risk_trafico_cab (
    trca_proceso integer NOT NULL,
    trca_cod_riesgo smallint NOT NULL,
    trca_cod_dato smallint NOT NULL,
    trca_fec_riesgo date,
    trca_cat_dato character(6) NOT NULL,
    trca_dia_llamadas integer,
    trca_dia_minutos numeric,
    trca_ind_umb_llamadas numeric,
    trca_ind_umb_minutos numeric,
    trca_aye_llamadas integer,
    trca_aye_minutos numeric,
    trca_ind_aye_llamadas numeric,
    trca_ind_aye_minutos numeric,
    trca_avg_xda_llamadas numeric,
    trca_avg_xda_minutos numeric,
    trca_ind_avg_xda_llamadas numeric,
    trca_ind_avg_xda_minutos numeric,
    trca_avg_xdp_llamadas numeric,
    trca_avg_xdp_minutos numeric,
    trca_ind_avg_xdp_llamadas numeric,
    trca_ind_avg_xdp_minutos numeric,
    trca_dst_xda_llamadas numeric,
    trca_dst_xda_minutos numeric,
    trca_ind_dst_xda_llamadas numeric,
    trca_ind_dst_xda_minutos numeric,
    trca_dst_xdp_llamadas numeric,
    trca_dst_xdp_minutos numeric,
    trca_ind_dst_xdp_llamadas numeric,
    trca_ind_dst_xdp_minutos numeric DEFAULT 0,
    trca_where_coho character varying(250),
    trca_where_codi character(250),
    trca_where_tasa character(250)
);


ALTER TABLE public.desa_risk_trafico_cab OWNER TO postgres;


--
-- TOC entry 138 (class 1259 OID 84376)
-- Dependencies: 6
-- Name: ldsg_menu_perfil; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE ldsg_menu_perfil (
    num_perfil integer NOT NULL,
    cod_menu character(10) NOT NULL,
    tip_acceso character(1) NOT NULL
);


ALTER TABLE public.ldsg_menu_perfil OWNER TO postgres;

--
-- TOC entry 136 (class 1259 OID 84368)
-- Dependencies: 6
-- Name: ldsg_menus; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE ldsg_menus (
    cod_menu character(10) NOT NULL,
    nom_menu character(50) NOT NULL,
    des_menu character(60)
);


ALTER TABLE public.ldsg_menus OWNER TO postgres;

--
-- TOC entry 137 (class 1259 OID 84372)
-- Dependencies: 6
-- Name: ldsg_perfiles; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE ldsg_perfiles (
    num_perfil integer NOT NULL,
    des_perfil character(30) NOT NULL,
    cod_perfil character(5)
);


ALTER TABLE public.ldsg_perfiles OWNER TO postgres;

--
-- TOC entry 139 (class 1259 OID 84385)
-- Dependencies: 6
-- Name: ldsg_usua_perfil; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE ldsg_usua_perfil (
    num_perfil integer NOT NULL,
    cod_usuario character(10) NOT NULL,
    cod_perfil character(5)
);


ALTER TABLE public.ldsg_usua_perfil OWNER TO postgres;

--
-- TOC entry 135 (class 1259 OID 84364)
-- Dependencies: 6
-- Name: ldsg_usuarios; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE ldsg_usuarios (
    cod_usuario character(10) NOT NULL,
    nom_usuario character(80) NOT NULL,
    psw_usuario character(10) NOT NULL,
    fec_inicio date NOT NULL,
    fec_fin date NOT NULL,
    hor_inicio character(5) NOT NULL,
    hor_fin character(5) NOT NULL,
    est_usuario character(1) NOT NULL,
    est_supervisor character(1) NOT NULL,
    fec_ult_acceso date,
    fec_ult_chg_pwd date,
    flg_bloqueo character(1),
    pwd_01 character(10),
    pwd_02 character(10),
    pwd_03 character(10),
    pwd_04 character(10),
    pwd_05 character(10),
    des_email character varying(100)
);


ALTER TABLE public.ldsg_usuarios OWNER TO postgres;

--
-- TOC entry 183 (class 1259 OID 149382)
-- Dependencies: 6
-- Name: seq_anomalia; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE seq_anomalia
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.seq_anomalia OWNER TO postgres;

SET default_tablespace = '';

--
-- TOC entry 246 (class 1259 OID 403027)
-- Dependencies: 6
-- Name: ssee_consolidado_hoy; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ssee_consolidado_hoy (
    nuor_pais character(5),
    nuor_ciud character(10),
    nude_pais character(5),
    nude_ciud character(10),
    ruen_oper character(5),
    ruen_pais character(5),
    rusa_oper character(10),
    rusa_pais character(5),
    tota_llam bigint,
    tota_segu bigint
);


ALTER TABLE public.ssee_consolidado_hoy OWNER TO postgres;



--
-- TOC entry 250 (class 1259 OID 410925)
-- Dependencies: 6
-- Name: temp_destinos; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE temp_destinos (
    dest_codigo character(10) NOT NULL,
    dest_descripcion character(50),
    dest_pais character(5),
    dest_observacion character(50)
);


ALTER TABLE public.temp_destinos OWNER TO postgres;

SET default_tablespace = '';

--
-- TOC entry 201 (class 1259 OID 296243)
-- Dependencies: 6
-- Name: temp_servicioespecial; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE temp_servicioespecial (
    temp_acceso_tgsol character(20) NOT NULL,
    temp_origen character(70),
    temp_proveedor character(70),
    temp_etis_proveedor character(5),
    temp_destino character(70),
    temp_acceso_origen character(20),
    temp_rn_saliente character(20),
    temp_cliente character(70),
    temp_ruta_saliente character(70),
    temp_etis_ruta_saliente character(20),
    temp_carrier_terminal character(30),
    temp_tipo_acceso character(10),
    temp_band_subex character(70),
    temp_fecha_alta character(10) NOT NULL,
    temp_fecha_baja character(10),
    temp_activo character(2),
    temp_comentario character(200),
    carr_origen character(5),
    pais_destino character(5),
    fecha_alta date,
    fecha_baja date
);


ALTER TABLE public.temp_servicioespecial OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 386111)
-- Dependencies: 6
-- Name: temp_servicioespecial_tmp; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE temp_servicioespecial_tmp (
    temp_acceso_tgsol character(20) NOT NULL,
    temp_origen character(70),
    temp_proveedor character(70),
    temp_etis_proveedor character(8),
    temp_destino character(70),
    temp_acceso_origen character(20),
    temp_rn_saliente character(20),
    temp_ruta_saliente character(70),
    temp_etis_ruta_saliente character(20),
    temp_carrier_terminal character(30),
    temp_fecha_alta character(10) NOT NULL,
    temp_fecha_baja character(10),
    temp_activo character(2),
    temp_comentario character(500),
    temp_cliente character varying(70),
    temp_tipo_acceso character varying(10),
    temp_band_subex character varying(70),
    pais_destino character varying(5),
    fecha_alta date,
    fecha_baja date,
    carr_terminal character varying(5),
    carr_origen character varying(5)
);


ALTER TABLE public.temp_servicioespecial_tmp OWNER TO postgres;


--
-- TOC entry 245 (class 1259 OID 401839)
-- Dependencies: 2023 2024 2025 2026 2027 2028 6
-- Name: tiws_alarmas_numeros; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_alarmas_numeros (
    anum_cab_nume_proceso integer NOT NULL,
    anum_cab_fecha date NOT NULL,
    anum_cab_tipo character(1) NOT NULL,
    anum_cab_telefono character(20) NOT NULL,
    anum_cab_tot_llamadas integer,
    anum_cab_tot_minutos numeric,
    anum_cab_tot_dis_carrier smallint,
    anum_cab_tot_dis_pais smallint,
    anum_cab_tot_dis_numero smallint,
    anum_cab_rsk_llamadas integer,
    anum_cab_rsk_minutos numeric,
    anum_cab_rsk_dis_carrier smallint,
    anum_cab_rsk_dis_pais smallint,
    anum_cab_rsk_dis_numero smallint,
    anum_cab_bla_llamadas integer,
    anum_cab_bla_minutos numeric,
    anum_cab_bla_dis_carrier smallint,
    anum_cab_bla_dis_pais smallint,
    anum_cab_bla_dis_numero smallint,
    anum_cab_max_minutos integer,
    anum_cab_ult_hora timestamp without time zone,
    anum_cab_min_minutos integer,
    anum_cab_niv_alarma smallint,
    anum_cab_bgn character(1),
    anum_cab_carrier character(5),
    anum_env_fechahora timestamp without time zone DEFAULT ('now'::text)::date,
    anum_env_responsable character(10) DEFAULT ''::bpchar,
    anum_fra_indicador smallint DEFAULT 0,
    anum_fra_responsable character(10) DEFAULT ''::bpchar,
    anum_fra_fechahora timestamp without time zone DEFAULT ('now'::text)::date,
    anum_fra_tipo smallint DEFAULT 0
);


ALTER TABLE public.tiws_alarmas_numeros OWNER TO postgres;

SET default_tablespace = '';

--
-- TOC entry 202 (class 1259 OID 298731)
-- Dependencies: 1978 1979 6
-- Name: tiws_alarmas_ocarr_cab; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_alarmas_ocarr_cab (
    aocc_num_proceso integer NOT NULL,
    aocc_cod_riesgo smallint NOT NULL,
    aocc_fec_riesgo date NOT NULL,
    aocc_prd_llamadas integer,
    aocc_prd_minutos numeric,
    aocc_env_fechahora timestamp without time zone,
    aocc_env_responsable character(10),
    aocc_fra_indicador smallint DEFAULT 0,
    aocc_fra_responsable character(10),
    aocc_fra_fechahora timestamp without time zone,
    aocc_fra_tipo smallint DEFAULT 0
);


ALTER TABLE public.tiws_alarmas_ocarr_cab OWNER TO postgres;


--
-- TOC entry 142 (class 1259 OID 93537)
-- Dependencies: 6
-- Name: tiws_backup_cab; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_backup_cab (
    bcab_tabla character(30) NOT NULL,
    bcab_base character(20) NOT NULL,
    bcab_rutaoutput character(100),
    bcab_prefijooutput character(30),
    bcab_campoclave character(30),
    bcab_diasreten_bd smallint,
    bcab_diasreten_fs smallint,
    bcab_claveminimaactual date,
    bcab_flg_backup boolean,
    bcab_maxdiasbackup smallint,
    bcab_ultimodiabackup date,
    bcab_flg_delete boolean,
    bcab_maxdiasdelete smallint,
    bcab_ultimodiadelete date,
    bcab_procedure character(30),
    bcab_flg_estado boolean
);


ALTER TABLE public.tiws_backup_cab OWNER TO postgres;

SET default_tablespace = '';

--
-- TOC entry 143 (class 1259 OID 93541)
-- Dependencies: 6
-- Name: tiws_backup_det; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_backup_det (
    bmov_tabla character(30) NOT NULL,
    bmov_base character(20) NOT NULL,
    bmov_tipoproceso character(6),
    bmov_fecini_clave date,
    bmov_fecfin_clave date,
    bmov_fecini_proceso timestamp without time zone,
    bmov_fecfin_proceso timestamp without time zone,
    bmov_totregistros bigint,
    bmov_nombrearchivo character(200),
    bmov_estado boolean
);


ALTER TABLE public.tiws_backup_det OWNER TO postgres;


--
-- TOC entry 184 (class 1259 OID 149384)
-- Dependencies: 1969 6
-- Name: tiws_cab_anomalias; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_cab_anomalias (
    cano_nume_anomalia integer NOT NULL,
    cano_fecha_data date NOT NULL,
    cano_fecha_proceso timestamp without time zone NOT NULL,
    cano_tipo_anomalia character(10) NOT NULL,
    cano_codi_destinoriesgo smallint,
    cano_orig_pais character(5),
    cano_orig_area character(10),
    cano_dest_pais character(5),
    cano_dest_area character(10),
    cano_ruta_entrada character(10),
    cano_ruen_carrier character(5),
    cano_ruen_pais character(5),
    cano_ruen_servicio character(10),
    cano_ruta_salida character(10),
    cano_rusa_carrier character(5),
    cano_rusa_pais character(5),
    cano_rusa_servicio character(10),
    cano_nume_origen character(20),
    cano_nume_destino character(20),
    cano_suma_llamadas integer,
    cano_suma_minutos numeric DEFAULT 0
);


ALTER TABLE public.tiws_cab_anomalias OWNER TO postgres;

SET default_tablespace = '';

--
-- TOC entry 189 (class 1259 OID 149757)
-- Dependencies: 6
-- Name: tiws_cab_indicadores; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_cab_indicadores (
    cind_codigo integer NOT NULL,
    cind_sigla character(10),
    cind_descripcion character varying(50) NOT NULL,
    cind_umbrales smallint,
    clis_estado boolean
);


ALTER TABLE public.tiws_cab_indicadores OWNER TO postgres;

--
-- TOC entry 188 (class 1259 OID 149755)
-- Dependencies: 6 189
-- Name: tiws_cab_indicadores_cind_codigo_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE tiws_cab_indicadores_cind_codigo_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.tiws_cab_indicadores_cind_codigo_seq OWNER TO postgres;

--
-- TOC entry 2366 (class 0 OID 0)
-- Dependencies: 188
-- Name: tiws_cab_indicadores_cind_codigo_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE tiws_cab_indicadores_cind_codigo_seq OWNED BY tiws_cab_indicadores.cind_codigo;


--
-- TOC entry 186 (class 1259 OID 149689)
-- Dependencies: 6
-- Name: tiws_cab_listas; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_cab_listas (
    clis_codigo integer NOT NULL,
    clis_descripcion character varying(50) NOT NULL,
    clis_estado boolean
);


ALTER TABLE public.tiws_cab_listas OWNER TO postgres;

--
-- TOC entry 185 (class 1259 OID 149687)
-- Dependencies: 6 186
-- Name: tiws_cab_listas_clis_codigo_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE tiws_cab_listas_clis_codigo_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.tiws_cab_listas_clis_codigo_seq OWNER TO postgres;

--
-- TOC entry 2368 (class 0 OID 0)
-- Dependencies: 185
-- Name: tiws_cab_listas_clis_codigo_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE tiws_cab_listas_clis_codigo_seq OWNED BY tiws_cab_listas.clis_codigo;



--
-- TOC entry 115 (class 1259 OID 72765)
-- Dependencies: 6
-- Name: tiws_carrier; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_carrier (
    carr_codigo character(5) NOT NULL,
    carr_descripcion character(50),
    carr_pais character(5),
    carr_observacion character(60)
);


ALTER TABLE public.tiws_carrier OWNER TO postgres;

--
-- TOC entry 121 (class 1259 OID 74114)
-- Dependencies: 1890 6
-- Name: tiws_central; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_central (
    cent_codigo integer NOT NULL,
    cent_sigla character(6),
    cent_descripcion character(20),
    cent_ubicacion character(30),
    cent_personacontacto character(20),
    cent_telefonocontacto character(18),
    cent_rutarecepcion character(100),
    cent_rutaprocesado character(100),
    cent_rutabackup character(100),
    cent_prefijo character(20),
    cent_sufijo character(20),
    cent_inisecuencia integer,
    cent_finsecuencia integer,
    cent_usrcreacion integer,
    cent_feccreacion date,
    cent_usrmodifica integer,
    cent_fecmodifica date,
    cent_estado character(1) DEFAULT 'A'::bpchar,
    cent_grupocentral character(20)
);


ALTER TABLE public.tiws_central OWNER TO postgres;

--
-- TOC entry 244 (class 1259 OID 398872)
-- Dependencies: 6
-- Name: tiws_chkfon_cab_hoy; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_chkfon_cab_hoy (
    cfoh_cab_nume_proceso integer NOT NULL,
    cfoh_cab_fecha date NOT NULL,
    cfoh_cab_tipo character(1) NOT NULL,
    cfoh_cab_telefono character(20) NOT NULL,
    cfoh_cab_tot_llamadas integer,
    cfoh_cab_tot_minutos numeric,
    cfoh_cab_tot_dis_carrier smallint,
    cfoh_cab_tot_dis_pais smallint,
    cfoh_cab_tot_dis_numero integer,
    cfoh_cab_rsk_llamadas integer,
    cfoh_cab_rsk_minutos numeric,
    cfoh_cab_rsk_dis_carrier smallint,
    cfoh_cab_rsk_dis_pais smallint,
    cfoh_cab_rsk_dis_numero smallint,
    cfoh_cab_bla_llamadas integer,
    cfoh_cab_bla_minutos numeric,
    cfoh_cab_bla_dis_carrier smallint,
    cfoh_cab_bla_dis_pais smallint,
    cfoh_cab_bla_dis_numero smallint,
    cfoh_cab_max_minutos integer,
    cfoh_cab_ult_hora timestamp without time zone,
    cfoh_cab_min_minutos integer,
    cfoh_cab_niv_alarma smallint,
    cfoh_cab_bgn character(1),
    cfoh_cab_carrier character(5)
);


ALTER TABLE public.tiws_chkfon_cab_hoy OWNER TO postgres;

--
-- TOC entry 259 (class 1259 OID 421703)
-- Dependencies: 6
-- Name: tiws_chkfon_det_pacpac_dia; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_chkfon_det_pacpac_dia (
    chod_pac_proceso integer NOT NULL,
    chod_pac_fecha date NOT NULL,
    chod_pac_tipo character(5) NOT NULL,
    chod_pac_telefono character(20) NOT NULL,
    chod_pac_orig_pais character(5) NOT NULL,
    chod_pac_orig_area character(10) NOT NULL,
    chod_pac_ruen_carrier character(5) NOT NULL,
    chod_pac_dest_pais character(5) NOT NULL,
    chod_pac_dest_area character(10) NOT NULL,
    chod_pac_rusa_carrier character(5) NOT NULL,
    chod_pac_llamadas integer,
    chod_pac_minutos numeric,
    chod_pac_niv_alarma smallint,
    chod_pac_flag_conservar smallint,
    chod_pac_fechahora timestamp without time zone NOT NULL
);


ALTER TABLE public.tiws_chkfon_det_pacpac_dia OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 395887)
-- Dependencies: 6
-- Name: tiws_chkfon_det_pacpac_hoy; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_chkfon_det_pacpac_hoy (
    choh_pac_proceso integer NOT NULL,
    choh_pac_fecha date NOT NULL,
    choh_pac_tipo character(5) NOT NULL,
    choh_pac_telefono character(20) NOT NULL,
    choh_pac_orig_pais character(5) NOT NULL,
    choh_pac_orig_area character(10) NOT NULL,
    choh_pac_ruen_carrier character(5) NOT NULL,
    choh_pac_dest_pais character(5) NOT NULL,
    choh_pac_dest_area character(10) NOT NULL,
    choh_pac_rusa_carrier character(5) NOT NULL,
    choh_pac_llamadas integer,
    choh_pac_minutos numeric,
    choh_pac_niv_alarma smallint,
    choh_pac_flag_conservar smallint,
    choh_pac_fechahora timestamp without time zone NOT NULL
);


ALTER TABLE public.tiws_chkfon_det_pacpac_hoy OWNER TO postgres;

SET default_tablespace = '';

--
-- TOC entry 260 (class 1259 OID 421714)
-- Dependencies: 6
-- Name: tiws_chkfon_det_pareto_dia; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_chkfon_det_pareto_dia (
    chod_det_proceso integer NOT NULL,
    chod_det_fec_riesgo date NOT NULL,
    chod_det_tipo character(5) NOT NULL,
    chod_det_telefono character(20) NOT NULL,
    chod_det_tip_analisis character(10) NOT NULL,
    chod_det_cod_dato character(20) NOT NULL,
    chod_det_des_dato character(60) NOT NULL,
    chod_det_tip_valor character(10) NOT NULL,
    chod_det_cantidad integer,
    chod_det_llamadas integer,
    chod_det_minutos numeric,
    chod_det_porcentaje numeric,
    chod_det_fechahora timestamp without time zone NOT NULL
);


ALTER TABLE public.tiws_chkfon_det_pareto_dia OWNER TO postgres;

--
-- TOC entry 243 (class 1259 OID 398866)
-- Dependencies: 6
-- Name: tiws_chkfon_det_pareto_hoy; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_chkfon_det_pareto_hoy (
    choh_det_proceso integer NOT NULL,
    choh_det_fec_riesgo date NOT NULL,
    choh_det_tipo character(5) NOT NULL,
    choh_det_telefono character(20) NOT NULL,
    choh_det_tip_analisis character(10) NOT NULL,
    choh_det_cod_dato character(20) NOT NULL,
    choh_det_des_dato character(60) NOT NULL,
    choh_det_tip_valor character(10) NOT NULL,
    choh_det_cantidad integer,
    choh_det_llamadas integer,
    choh_det_minutos numeric,
    choh_det_porcentaje numeric,
    choh_det_fechahora timestamp without time zone NOT NULL
);


ALTER TABLE public.tiws_chkfon_det_pareto_hoy OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 394648)
-- Dependencies: 1986 6
-- Name: tiws_chkfon_ratio_hoy; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_chkfon_ratio_hoy (
    rcfh_fec_riesgo date NOT NULL,
    rcfh_tip_telefono character(1) NOT NULL,
    rcfh_telefono character(30) NOT NULL,
    rcfh_dia_llamadas integer,
    rcfh_dia_minutos numeric,
    rcfh_ind_umb_llamadas numeric,
    rcfh_ind_umb_minutos numeric,
    rcfh_aye_llamadas integer,
    rcfh_aye_minutos numeric,
    rcfh_ind_aye_llamadas numeric,
    rcfh_ind_aye_minutos numeric,
    rcfh_avg_xda_llamadas numeric,
    rcfh_avg_xda_minutos numeric,
    rcfh_ind_avg_xda_llamadas numeric,
    rcfh_ind_avg_xda_minutos numeric,
    rcfh_avg_xdp_llamadas numeric,
    rcfh_avg_xdp_minutos numeric,
    rcfh_ind_avg_xdp_llamadas numeric,
    rcfh_ind_avg_xdp_minutos numeric,
    rcfh_dst_xda_llamadas numeric,
    rcfh_dst_xda_minutos numeric,
    rcfh_ind_dst_xda_llamadas numeric,
    rcfh_ind_dst_xda_minutos numeric,
    rcfh_dst_xdp_llamadas numeric,
    rcfh_dst_xdp_minutos numeric,
    rcfh_ind_dst_xdp_llamadas numeric,
    rcfh_ind_dst_xdp_minutos numeric DEFAULT 0,
    rcfh_max_hora smallint
);


ALTER TABLE public.tiws_chkfon_ratio_hoy OWNER TO postgres;


--
-- TOC entry 205 (class 1259 OID 352657)
-- Dependencies: 1980 1981 6
-- Name: tiws_cons_destinosderiesgo; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_cons_destinosderiesgo (
    codr_fecha date NOT NULL,
    codr_cod_destino smallint NOT NULL,
    codr_dest_pais character(5) NOT NULL,
    codr_orig_carrier character(5) NOT NULL,
    codr_llamadas integer,
    codr_minutos numeric DEFAULT 0,
    codr_minxllam numeric(5,2) DEFAULT 0
);


ALTER TABLE public.tiws_cons_destinosderiesgo OWNER TO postgres;

--
-- TOC entry 132 (class 1259 OID 78967)
-- Dependencies: 1895 6
-- Name: tiws_consolidado_dia; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia (
    codi_fecha date NOT NULL,
    codi_orig_pais character(5) NOT NULL,
    codi_orig_area character(10) NOT NULL,
    codi_dest_pais character(5) NOT NULL,
    codi_dest_area character(10) NOT NULL,
    codi_ruta_entrada character(10) NOT NULL,
    codi_ruen_carrier character(5) NOT NULL,
    codi_ruen_pais character(5) NOT NULL,
    codi_ruen_servicio character(10) NOT NULL,
    codi_ruta_salida character(10) NOT NULL,
    codi_rusa_carrier character(5) NOT NULL,
    codi_rusa_pais character(5) NOT NULL,
    codi_rusa_servicio character(10) NOT NULL,
    codi_suma_llamadas integer,
    codi_suma_segundos integer,
    codi_clave character(50),
    codi_suma_minutos numeric DEFAULT 0
);


ALTER TABLE public.tiws_consolidado_dia OWNER TO postgres;

--
-- TOC entry 152 (class 1259 OID 127390)
-- Dependencies: 1924 6 132
-- Name: tiws_consolidado_dia_201501; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia_201501 (CONSTRAINT tiws_consolidado_dia_201501_codi_fecha_check CHECK (((codi_fecha >= '2015-01-01'::date) AND (codi_fecha < '2015-02-01'::date)))
)
INHERITS (tiws_consolidado_dia);


ALTER TABLE public.tiws_consolidado_dia_201501 OWNER TO postgres;

--
-- TOC entry 163 (class 1259 OID 127443)
-- Dependencies: 1946 6 132
-- Name: tiws_consolidado_dia_201502; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia_201502 (CONSTRAINT tiws_consolidado_dia_201502_codi_fecha_check CHECK (((codi_fecha >= '2015-02-01'::date) AND (codi_fecha < '2015-03-01'::date)))
)
INHERITS (tiws_consolidado_dia);


ALTER TABLE public.tiws_consolidado_dia_201502 OWNER TO postgres;

--
-- TOC entry 153 (class 1259 OID 127394)
-- Dependencies: 1926 6 132
-- Name: tiws_consolidado_dia_201503; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia_201503 (CONSTRAINT tiws_consolidado_dia_201503_codi_fecha_check CHECK (((codi_fecha >= '2015-03-01'::date) AND (codi_fecha < '2015-04-01'::date)))
)
INHERITS (tiws_consolidado_dia);


ALTER TABLE public.tiws_consolidado_dia_201503 OWNER TO postgres;

--
-- TOC entry 154 (class 1259 OID 127398)
-- Dependencies: 1928 6 132
-- Name: tiws_consolidado_dia_201504; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia_201504 (CONSTRAINT tiws_consolidado_dia_201504_codi_fecha_check CHECK (((codi_fecha >= '2015-04-01'::date) AND (codi_fecha < '2015-05-01'::date)))
)
INHERITS (tiws_consolidado_dia);


ALTER TABLE public.tiws_consolidado_dia_201504 OWNER TO postgres;

--
-- TOC entry 155 (class 1259 OID 127402)
-- Dependencies: 1930 6 132
-- Name: tiws_consolidado_dia_201505; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia_201505 (CONSTRAINT tiws_consolidado_dia_201505_codi_fecha_check CHECK (((codi_fecha >= '2015-05-01'::date) AND (codi_fecha < '2015-06-01'::date)))
)
INHERITS (tiws_consolidado_dia);


ALTER TABLE public.tiws_consolidado_dia_201505 OWNER TO postgres;

--
-- TOC entry 156 (class 1259 OID 127406)
-- Dependencies: 1932 6 132
-- Name: tiws_consolidado_dia_201506; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia_201506 (CONSTRAINT tiws_consolidado_dia_201506_codi_fecha_check CHECK (((codi_fecha >= '2015-06-01'::date) AND (codi_fecha < '2015-07-01'::date)))
)
INHERITS (tiws_consolidado_dia);


ALTER TABLE public.tiws_consolidado_dia_201506 OWNER TO postgres;

--
-- TOC entry 157 (class 1259 OID 127410)
-- Dependencies: 1934 6 132
-- Name: tiws_consolidado_dia_201507; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia_201507 (CONSTRAINT tiws_consolidado_dia_201507_codi_fecha_check CHECK (((codi_fecha >= '2015-07-01'::date) AND (codi_fecha < '2015-08-01'::date)))
)
INHERITS (tiws_consolidado_dia);


ALTER TABLE public.tiws_consolidado_dia_201507 OWNER TO postgres;

--
-- TOC entry 158 (class 1259 OID 127414)
-- Dependencies: 1936 6 132
-- Name: tiws_consolidado_dia_201508; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia_201508 (CONSTRAINT tiws_consolidado_dia_201508_codi_fecha_check CHECK (((codi_fecha >= '2015-08-01'::date) AND (codi_fecha < '2015-09-01'::date)))
)
INHERITS (tiws_consolidado_dia);


ALTER TABLE public.tiws_consolidado_dia_201508 OWNER TO postgres;

--
-- TOC entry 159 (class 1259 OID 127418)
-- Dependencies: 1938 6 132
-- Name: tiws_consolidado_dia_201509; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia_201509 (CONSTRAINT tiws_consolidado_dia_201509_codi_fecha_check CHECK (((codi_fecha >= '2015-09-01'::date) AND (codi_fecha < '2015-10-01'::date)))
)
INHERITS (tiws_consolidado_dia);


ALTER TABLE public.tiws_consolidado_dia_201509 OWNER TO postgres;

--
-- TOC entry 160 (class 1259 OID 127422)
-- Dependencies: 1940 6 132
-- Name: tiws_consolidado_dia_201510; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia_201510 (CONSTRAINT tiws_consolidado_dia_201510_codi_fecha_check CHECK (((codi_fecha >= '2015-10-01'::date) AND (codi_fecha < '2015-11-01'::date)))
)
INHERITS (tiws_consolidado_dia);


ALTER TABLE public.tiws_consolidado_dia_201510 OWNER TO postgres;

--
-- TOC entry 161 (class 1259 OID 127426)
-- Dependencies: 1942 6 132
-- Name: tiws_consolidado_dia_201511; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia_201511 (CONSTRAINT tiws_consolidado_dia_201511_codi_fecha_check CHECK (((codi_fecha >= '2015-11-01'::date) AND (codi_fecha < '2015-12-01'::date)))
)
INHERITS (tiws_consolidado_dia);


ALTER TABLE public.tiws_consolidado_dia_201511 OWNER TO postgres;

--
-- TOC entry 162 (class 1259 OID 127430)
-- Dependencies: 1944 6 132
-- Name: tiws_consolidado_dia_201512; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia_201512 (CONSTRAINT tiws_consolidado_dia_201512_codi_fecha_check CHECK (((codi_fecha >= '2015-12-01'::date) AND (codi_fecha < '2016-01-01'::date)))
)
INHERITS (tiws_consolidado_dia);


ALTER TABLE public.tiws_consolidado_dia_201512 OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 397206)
-- Dependencies: 1988 6 132
-- Name: tiws_consolidado_dia_201601; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia_201601 (CONSTRAINT tiws_consolidado_dia_201601_codi_fecha_check CHECK (((codi_fecha >= '2016-01-01'::date) AND (codi_fecha < '2016-02-01'::date)))
)
INHERITS (tiws_consolidado_dia);


ALTER TABLE public.tiws_consolidado_dia_201601 OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 397214)
-- Dependencies: 1990 6 132
-- Name: tiws_consolidado_dia_201602; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia_201602 (CONSTRAINT tiws_consolidado_dia_201602_codi_fecha_check CHECK (((codi_fecha >= '2016-02-01'::date) AND (codi_fecha < '2016-03-01'::date)))
)
INHERITS (tiws_consolidado_dia);


ALTER TABLE public.tiws_consolidado_dia_201602 OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 397222)
-- Dependencies: 1992 6 132
-- Name: tiws_consolidado_dia_201603; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia_201603 (CONSTRAINT tiws_consolidado_dia_201603_codi_fecha_check CHECK (((codi_fecha >= '2016-03-01'::date) AND (codi_fecha < '2016-04-01'::date)))
)
INHERITS (tiws_consolidado_dia);


ALTER TABLE public.tiws_consolidado_dia_201603 OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 397230)
-- Dependencies: 1994 6 132
-- Name: tiws_consolidado_dia_201604; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia_201604 (CONSTRAINT tiws_consolidado_dia_201604_codi_fecha_check CHECK (((codi_fecha >= '2016-04-01'::date) AND (codi_fecha < '2016-05-01'::date)))
)
INHERITS (tiws_consolidado_dia);


ALTER TABLE public.tiws_consolidado_dia_201604 OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 397238)
-- Dependencies: 1996 6 132
-- Name: tiws_consolidado_dia_201605; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia_201605 (CONSTRAINT tiws_consolidado_dia_201605_codi_fecha_check CHECK (((codi_fecha >= '2016-05-01'::date) AND (codi_fecha < '2016-06-01'::date)))
)
INHERITS (tiws_consolidado_dia);


ALTER TABLE public.tiws_consolidado_dia_201605 OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 397246)
-- Dependencies: 1998 6 132
-- Name: tiws_consolidado_dia_201606; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia_201606 (CONSTRAINT tiws_consolidado_dia_201606_codi_fecha_check CHECK (((codi_fecha >= '2016-06-01'::date) AND (codi_fecha < '2016-07-01'::date)))
)
INHERITS (tiws_consolidado_dia);


ALTER TABLE public.tiws_consolidado_dia_201606 OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 397254)
-- Dependencies: 2000 6 132
-- Name: tiws_consolidado_dia_201607; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia_201607 (CONSTRAINT tiws_consolidado_dia_201607_codi_fecha_check CHECK (((codi_fecha >= '2016-07-01'::date) AND (codi_fecha < '2016-08-01'::date)))
)
INHERITS (tiws_consolidado_dia);


ALTER TABLE public.tiws_consolidado_dia_201607 OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 397262)
-- Dependencies: 2002 6 132
-- Name: tiws_consolidado_dia_201608; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia_201608 (CONSTRAINT tiws_consolidado_dia_201608_codi_fecha_check CHECK (((codi_fecha >= '2016-08-01'::date) AND (codi_fecha < '2016-09-01'::date)))
)
INHERITS (tiws_consolidado_dia);


ALTER TABLE public.tiws_consolidado_dia_201608 OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 397270)
-- Dependencies: 2004 6 132
-- Name: tiws_consolidado_dia_201609; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia_201609 (CONSTRAINT tiws_consolidado_dia_201609_codi_fecha_check CHECK (((codi_fecha >= '2016-09-01'::date) AND (codi_fecha < '2016-10-01'::date)))
)
INHERITS (tiws_consolidado_dia);


ALTER TABLE public.tiws_consolidado_dia_201609 OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 397278)
-- Dependencies: 2006 6 132
-- Name: tiws_consolidado_dia_201610; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia_201610 (CONSTRAINT tiws_consolidado_dia_201610_codi_fecha_check CHECK (((codi_fecha >= '2016-10-01'::date) AND (codi_fecha < '2016-11-01'::date)))
)
INHERITS (tiws_consolidado_dia);


ALTER TABLE public.tiws_consolidado_dia_201610 OWNER TO postgres;

--
-- TOC entry 229 (class 1259 OID 397286)
-- Dependencies: 2008 6 132
-- Name: tiws_consolidado_dia_201611; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia_201611 (CONSTRAINT tiws_consolidado_dia_201611_codi_fecha_check CHECK (((codi_fecha >= '2016-11-01'::date) AND (codi_fecha < '2016-12-01'::date)))
)
INHERITS (tiws_consolidado_dia);


ALTER TABLE public.tiws_consolidado_dia_201611 OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 397294)
-- Dependencies: 2010 6 132
-- Name: tiws_consolidado_dia_201612; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_dia_201612 (CONSTRAINT tiws_consolidado_dia_201612_codi_fecha_check CHECK (((codi_fecha >= '2016-12-01'::date) AND (codi_fecha < '2017-01-01'::date)))
)
INHERITS (tiws_consolidado_dia);


ALTER TABLE public.tiws_consolidado_dia_201612 OWNER TO postgres;

--
-- TOC entry 131 (class 1259 OID 78374)
-- Dependencies: 1894 6
-- Name: tiws_consolidado_hoy; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_consolidado_hoy (
    coho_proceso integer NOT NULL,
    coho_orig_pais character(5) NOT NULL,
    coho_orig_area character(10) NOT NULL,
    coho_dest_pais character(5) NOT NULL,
    coho_dest_area character(10) NOT NULL,
    coho_ruta_entrada character(10) NOT NULL,
    coho_ruen_carrier character(5) NOT NULL,
    coho_ruen_pais character(5) NOT NULL,
    coho_ruen_servicio character(10) NOT NULL,
    coho_ruta_salida character(10) NOT NULL,
    coho_rusa_carrier character(5) NOT NULL,
    coho_rusa_pais character(5) NOT NULL,
    coho_rusa_servicio character(10) NOT NULL,
    coho_suma_llamadas integer,
    coho_suma_segundos integer,
    coho_clave character(50),
    coho_suma_minutos numeric DEFAULT 0
);


ALTER TABLE public.tiws_consolidado_hoy OWNER TO postgres;

--
-- TOC entry 120 (class 1259 OID 74107)
-- Dependencies: 1887 1888 1889 6
-- Name: tiws_controlproceso; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_controlproceso (
    ctrp_central integer NOT NULL,
    ctrp_resecuencia integer NOT NULL,
    ctrp_secuencia integer NOT NULL,
    ctrp_secuenciaproceso bigint NOT NULL,
    ctrp_ttfilenombre character(50),
    ctrp_ttfiletotalregistros integer,
    ctrp_prisecregistro bigint,
    ctrp_ultsecregistro bigint,
    ctrp_priregfecha timestamp without time zone,
    ctrp_prireghora character(8),
    ctrp_ultregfecha timestamp without time zone,
    ctrp_ultreghora character(8),
    ctrp_proc_estado character(2),
    ctrp_proc_fechorini timestamp without time zone,
    ctrp_proc_fechorfin timestamp without time zone,
    ctrp_totaltasacion integer,
    ctrp_totalrechazos integer,
    ctrp_totalnacional integer,
    ctrp_totalintentos integer,
    ctrp_error integer,
    ctrp_totaldesbordes integer DEFAULT 0,
    ctrp_totalparciales integer DEFAULT 0,
    ctrp_totalinternacional integer DEFAULT 0,
    ctrp_totalrebotes integer
);


ALTER TABLE public.tiws_controlproceso OWNER TO postgres;

SET default_tablespace = '';

--
-- TOC entry 144 (class 1259 OID 102810)
-- Dependencies: 1898 1899 1900 1901 1902 1903 1904 1905 1906 1907 1908 1909 1910 1911 1912 1913 1914 1915 1916 1917 6
-- Name: tiws_cordinador; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_cordinador (
    cord_fecha date NOT NULL,
    cord_flg01 smallint DEFAULT 0,
    cord_flg02 smallint DEFAULT 0,
    cord_flg03 smallint DEFAULT 0,
    cord_flg04 smallint DEFAULT 0,
    cord_flg05 smallint DEFAULT 0,
    cord_flg06 smallint DEFAULT 0,
    cord_flg07 smallint DEFAULT 0,
    cord_flg08 smallint DEFAULT 0,
    cord_flg09 smallint DEFAULT 0,
    cord_flg10 smallint DEFAULT 0,
    cord_flg11 smallint DEFAULT 0,
    cord_flg12 smallint DEFAULT 0,
    cord_flg13 smallint DEFAULT 0,
    cord_flg14 smallint DEFAULT 0,
    cord_flg15 smallint DEFAULT 0,
    cord_flg16 smallint DEFAULT 0,
    cord_flg17 smallint DEFAULT 0,
    cord_flg18 smallint DEFAULT 0,
    cord_flg19 smallint DEFAULT 0,
    cord_flg20 smallint DEFAULT 0
);


ALTER TABLE public.tiws_cordinador OWNER TO postgres;


--
-- TOC entry 118 (class 1259 OID 72842)
-- Dependencies: 6
-- Name: tiws_destinos; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_destinos (
    dest_codigo character(10) NOT NULL,
    dest_descripcion character(50),
    dest_pais character(5),
    dest_observacion character(50)
);


ALTER TABLE public.tiws_destinos OWNER TO postgres;

SET default_tablespace = '';

--
-- TOC entry 146 (class 1259 OID 118891)
-- Dependencies: 1919 1920 1921 6
-- Name: tiws_destinosderiesgo; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_destinosderiesgo (
    drsk_codigo integer NOT NULL,
    drsk_descripcion character(50),
    drsk_largo character(100),
    drsk_pais character(5) DEFAULT '*'::bpchar,
    drsk_carrier character(5),
    drsk_area character(5),
    drsk_servicio character(5),
    drsk_nivelderiesgo smallint,
    drsk_pais_origen character(5),
    drsk_carrier_origen character(5),
    drsk_area_origen character(5),
    drsk_servicio_origen character(5),
    drsk_estado boolean DEFAULT true,
    drsk_grp_distribucion character(5) DEFAULT 'PROD'::bpchar,
    drsk_tipodestino character(5)
);


ALTER TABLE public.tiws_destinosderiesgo OWNER TO postgres;

--
-- TOC entry 145 (class 1259 OID 118889)
-- Dependencies: 6 146
-- Name: tiws_destinosderiesgo_drsk_codigo_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE tiws_destinosderiesgo_drsk_codigo_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.tiws_destinosderiesgo_drsk_codigo_seq OWNER TO postgres;

--
-- TOC entry 2408 (class 0 OID 0)
-- Dependencies: 145
-- Name: tiws_destinosderiesgo_drsk_codigo_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE tiws_destinosderiesgo_drsk_codigo_seq OWNED BY tiws_destinosderiesgo.drsk_codigo;




--
-- TOC entry 182 (class 1259 OID 149366)
-- Dependencies: 1966 1967 1968 6
-- Name: tiws_det_anomalias; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_det_anomalias (
    dano_nume_anomalia integer,
    dano_codi_destinoriesgo smallint,
    dano_tipo_analisis character(10),
    dano_codi_dato character(20),
    dano_desc_dato character(60),
    dano_tipo_valor character(10),
    dano_valor integer DEFAULT 0,
    dano_llamadas integer DEFAULT 0,
    dano_minutos numeric DEFAULT 0
);


ALTER TABLE public.tiws_det_anomalias OWNER TO postgres;

SET default_tablespace = '';

--
-- TOC entry 187 (class 1259 OID 149715)
-- Dependencies: 6
-- Name: tiws_det_listas; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_det_listas (
    dlis_codigo integer NOT NULL,
    dlis_dato_codigo character(15) NOT NULL,
    dlis_dato_descripcion character varying(50) NOT NULL,
    dlis_estado boolean
);


ALTER TABLE public.tiws_det_listas OWNER TO postgres;


--
-- TOC entry 125 (class 1259 OID 74144)
-- Dependencies: 6
-- Name: tiws_enproceso; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_enproceso (
    enpr_secuenciaproceso bigint NOT NULL,
    enpr_secuenciaregistro bigint NOT NULL,
    enpr_fechahora timestamp without time zone NOT NULL,
    enpr_numeroorigen character(20),
    enpr_numerodestino character(20),
    enpr_rutaentrada character(20),
    enpr_rutasalida character(20),
    enpr_ip_entrada character(15),
    enpr_ip_salida character(15),
    enpr_segundos smallint,
    enpr_salidaparcial integer,
    enpr_numregparcial integer,
    enpr_error smallint,
    enpr_observacion character(100),
    enpr_id_call character(20)
);


ALTER TABLE public.tiws_enproceso OWNER TO postgres;

SET default_tablespace = '';

--
-- TOC entry 253 (class 1259 OID 417673)
-- Dependencies: 6
-- Name: tiws_equivalencia; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_equivalencia (
    equi_externo character(10) NOT NULL,
    equi_exte_dato character(20) NOT NULL,
    equi_exte_codigo character(60) NOT NULL,
    equi_tiws_codigo character(60),
    equi_tiws_tabla character(20)
);


ALTER TABLE public.tiws_equivalencia OWNER TO postgres;


--
-- TOC entry 127 (class 1259 OID 74848)
-- Dependencies: 6
-- Name: tiws_errores; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_errores (
    erro_codigo integer NOT NULL,
    erro_descripcion character(60) NOT NULL,
    erro_modulo character(30),
    erro_usrcreacion integer,
    erro_feccreacion date,
    erro_usrmodifica integer,
    erro_fecmodifica date,
    erro_flgrecuperable inet
);


ALTER TABLE public.tiws_errores OWNER TO postgres;

SET default_tablespace = '';

--
-- TOC entry 249 (class 1259 OID 409394)
-- Dependencies: 6
-- Name: tiws_img_prueba; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_img_prueba (
    codigo character(5) NOT NULL,
    descripcion character(30),
    img bytea
);


ALTER TABLE public.tiws_img_prueba OWNER TO postgres;


--
-- TOC entry 140 (class 1259 OID 85807)
-- Dependencies: 6
-- Name: tiws_intento; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_intento (
    inte_secuenciaproceso bigint NOT NULL,
    inte_secuenciaregistro bigint NOT NULL,
    inte_secuenciareproceso bigint,
    inte_fechahora timestamp without time zone NOT NULL,
    inte_numeroorigen character(20) NOT NULL,
    inte_nuor_pais character(5),
    inte_nuor_operador character(10),
    inte_nuor_ciudad character(10),
    inte_nuor_servicio character(5),
    inte_numerodestino character(20) NOT NULL,
    inte_nude_pais character(5),
    inte_nude_operador character(10),
    inte_nude_ciudad character(10),
    inte_nude_servicio character(5),
    inte_numerossee character(20),
    inte_rutaentrada character(20) NOT NULL,
    inte_ruen_operador character(5),
    inte_ruen_pais character(5),
    inte_ruen_servicio character(5),
    inte_rutasalida character(20) NOT NULL,
    inte_rusa_operador character(10),
    inte_rusa_pais character(5),
    inte_rusa_servicio character(5),
    inte_prefijo character(8),
    inte_segundos integer NOT NULL,
    inte_modalidad character(5),
    inte_seor_serie character(20),
    inte_seor_operador character(10),
    inte_seor_servicio character(5),
    inte_seor_ciudad character(8),
    inte_sede_serie character(20),
    inte_sede_operador character(10),
    inte_sede_servicio character(5),
    inte_sede_ciudad character(8),
    inte_sse_flag character(1),
    inte_fuente smallint NOT NULL,
    inte_flagcruce smallint,
    inte_observacion character(100),
    inte_match_fechahora timestamp without time zone,
    inte_match_proceso bigint,
    inte_match_registro bigint
);


ALTER TABLE public.tiws_intento OWNER TO postgres;

--
-- TOC entry 122 (class 1259 OID 74119)
-- Dependencies: 6
-- Name: tiws_intentos; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_intentos (
    inte_secuenciaproceso bigint NOT NULL,
    inte_secuenciaregistro bigint NOT NULL,
    inte_fechahora timestamp without time zone NOT NULL,
    inte_numeroorigen character(20),
    inte_numerodestino character(20),
    inte_rutaentrada character(20),
    inte_rutasalida character(20),
    inte_ip_entrada character(15),
    inte_ip_salida character(15),
    inte_segundos smallint,
    inte_salidaparcial integer,
    inte_numregparcial integer,
    inte_error smallint,
    inte_observacion character(100),
    inte_id_call character(20)
);


ALTER TABLE public.tiws_intentos OWNER TO postgres;

--
-- TOC entry 256 (class 1259 OID 418619)
-- Dependencies: 6
-- Name: tiws_inter_seriesnumericas; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_inter_seriesnumericas (
    senu_numero character(20) NOT NULL,
    senu_pais character(5),
    senu_tipodestino character(10),
    senu_servicio character(5),
    senu_destino character(10),
    senu_area_operador character(40),
    senu_fechainicio date NOT NULL,
    senu_fechafinal date,
    senu_fechadeuso date,
    senu_fechaload timestamp without time zone,
    senu_fuente character(50),
    senu_observacion character(100)
);


ALTER TABLE public.tiws_inter_seriesnumericas OWNER TO postgres;

--
-- TOC entry 134 (class 1259 OID 83167)
-- Dependencies: 1896 6
-- Name: tiws_mensajes; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_mensajes (
    mens_usrdestino character(150) NOT NULL,
    mens_asunto character(100),
    mens_mensaje character varying(3000),
    mens_flgleido character(1) DEFAULT 'N'::bpchar,
    mens_fechor_recepcion timestamp without time zone NOT NULL,
    mens_fechor_envio timestamp without time zone,
    mens_fechor_lectura timestamp without time zone,
    mens_usrorigen character(50) NOT NULL,
    mens_secuencial integer NOT NULL,
    mens_attached character(150)
);


ALTER TABLE public.tiws_mensajes OWNER TO postgres;

--
-- TOC entry 133 (class 1259 OID 83165)
-- Dependencies: 6 134
-- Name: tiws_mensajes_mens_secuencial_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE tiws_mensajes_mens_secuencial_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.tiws_mensajes_mens_secuencial_seq OWNER TO postgres;

--
-- TOC entry 2418 (class 0 OID 0)
-- Dependencies: 133
-- Name: tiws_mensajes_mens_secuencial_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE tiws_mensajes_mens_secuencial_seq OWNED BY tiws_mensajes.mens_secuencial;


--
-- TOC entry 190 (class 1259 OID 149766)
-- Dependencies: 6
-- Name: tiws_msg_anomalias; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_msg_anomalias (
    mano_nume_anomalia integer,
    mano_codi_destinoriesgo smallint,
    mano_tipo_analisis character(10),
    mano_pare_lineas integer,
    mano_pare_llamadas integer,
    mano_pare_minutos numeric,
    mano_pare_porcentaje numeric
);


ALTER TABLE public.tiws_msg_anomalias OWNER TO postgres;

--
-- TOC entry 114 (class 1259 OID 72761)
-- Dependencies: 1886 6
-- Name: tiws_pais; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_pais (
    pais_codigo character(5) NOT NULL,
    pais_descripcion character(30),
    pais_imagen character(30),
    pais_discado character(10),
    pais_observacion character(60),
    pais_flg_tiws boolean,
    pais_cod_chart character(2),
    pais_grp_distribucion character(5) DEFAULT 'PROD'::bpchar
);


ALTER TABLE public.tiws_pais OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 325179)
-- Dependencies: 6
-- Name: tiws_pais_persona; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_pais_persona (
    pape_usuario character(10) NOT NULL,
    pape_pais character(5) NOT NULL,
    pape_carrier_local character(5) NOT NULL,
    pape_estado boolean,
    pape_alarma character(5) NOT NULL
);


ALTER TABLE public.tiws_pais_persona OWNER TO postgres;

SET default_tablespace = '';

--
-- TOC entry 248 (class 1259 OID 409384)
-- Dependencies: 2029 6
-- Name: tiws_pais_prueba; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_pais_prueba (
    pais_codigo character(5) NOT NULL,
    pais_descripcion character(30),
    pais_imagen character(30),
    pais_discado character(10),
    pais_observacion character(60),
    pais_flg_tiws boolean,
    pais_cod_chart character(2),
    pais_grp_distribucion character(5) DEFAULT 'PROD'::bpchar,
    pais_img bytea
);


ALTER TABLE public.tiws_pais_prueba OWNER TO postgres;

--
-- TOC entry 128 (class 1259 OID 77328)
-- Dependencies: 6
-- Name: tiws_parametros; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_parametros (
    para_dominio smallint NOT NULL,
    para_codigo smallint NOT NULL,
    para_descripcion character varying(50) NOT NULL,
    para_cadena1 character varying(50),
    para_cadena2 character varying(50),
    para_cadena3 character varying(50),
    para_valor1 smallint,
    para_valor2 integer,
    para_valor3 bigint,
    para_estado boolean
);


ALTER TABLE public.tiws_parametros OWNER TO postgres;


--
-- TOC entry 123 (class 1259 OID 74124)
-- Dependencies: 1891 1892 6
-- Name: tiws_parciales; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_parciales (
    parc_secuenciaproceso bigint NOT NULL,
    parc_secuenciaregistro bigint NOT NULL,
    parc_fechahora timestamp without time zone NOT NULL,
    parc_numeroorigen character(20),
    parc_numerodestino character(20),
    parc_rutaentrada character(20),
    parc_rutasalida character(20),
    parc_ip_entrada character(15),
    parc_ip_salida character(15),
    parc_segundos integer,
    parc_salidaparcial integer,
    parc_numregparcial integer,
    parc_error smallint,
    parc_observacion character(100),
    parc_id_call character(20),
    parc_secpro_final bigint DEFAULT 0,
    parc_secreg_final bigint DEFAULT 0
);


ALTER TABLE public.tiws_parciales OWNER TO postgres;

--
-- TOC entry 119 (class 1259 OID 74100)
-- Dependencies: 6
-- Name: tiws_prefijos; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_prefijos (
    pref_prefijo character(10) NOT NULL,
    pref_posicion smallint,
    pref_longitud smallint,
    pref_rutaentrada character(20) NOT NULL,
    pref_rutasalida character(20) NOT NULL,
    pref_estado character(1),
    pref_agregar character(5),
    pref_reemplazar character(5),
    pref_quitar character(10),
    pref_tipo character(4)
);


ALTER TABLE public.tiws_prefijos OWNER TO postgres;

--
-- TOC entry 130 (class 1259 OID 78369)
-- Dependencies: 6
-- Name: tiws_procesos; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_procesos (
    proc_codigo integer NOT NULL,
    proc_tipoproceso character(4),
    proc_fechainicio timestamp without time zone,
    proc_fechafin timestamp without time zone,
    proc_estado character(1),
    proc_fechadata date,
    proc_parametros character(60)
);


ALTER TABLE public.tiws_procesos OWNER TO postgres;

--
-- TOC entry 129 (class 1259 OID 78367)
-- Dependencies: 6 130
-- Name: tiws_procesos_proc_codigo_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE tiws_procesos_proc_codigo_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.tiws_procesos_proc_codigo_seq OWNER TO postgres;

--
-- TOC entry 2427 (class 0 OID 0)
-- Dependencies: 129
-- Name: tiws_procesos_proc_codigo_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE tiws_procesos_proc_codigo_seq OWNED BY tiws_procesos.proc_codigo;


--
-- TOC entry 124 (class 1259 OID 74133)
-- Dependencies: 6
-- Name: tiws_rechazos; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_rechazos (
    rech_secuenciaproceso bigint NOT NULL,
    rech_secuenciaregistro bigint NOT NULL,
    rech_fechahora timestamp without time zone NOT NULL,
    rech_numeroorigen character(20),
    rech_numerodestino character(20),
    rech_rutaentrada character(20),
    rech_rutasalida character(20),
    rech_ip_entrada character(15),
    rech_ip_salida character(15),
    rech_segundos integer,
    rech_salidaparcial integer,
    rech_numregparcial integer,
    rech_error smallint,
    rech_observacion character(100),
    rech_id_call character(20)
);


ALTER TABLE public.tiws_rechazos OWNER TO postgres;

SET default_tablespace = '';

--
-- TOC entry 148 (class 1259 OID 118909)
-- Dependencies: 6
-- Name: tiws_risk_catalogo; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_risk_catalogo (
    risk_codigo integer NOT NULL,
    risk_descripcion character(20),
    risk_largo character(100),
    risk_nivel smallint,
    risk_estado character(1),
    risk_funcion character(50),
    risk_tipo_funcion character(20)
);


ALTER TABLE public.tiws_risk_catalogo OWNER TO postgres;

--
-- TOC entry 147 (class 1259 OID 118907)
-- Dependencies: 6 148
-- Name: tiws_risk_catalogo_risk_codigo_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE tiws_risk_catalogo_risk_codigo_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.tiws_risk_catalogo_risk_codigo_seq OWNER TO postgres;

--
-- TOC entry 2430 (class 0 OID 0)
-- Dependencies: 147
-- Name: tiws_risk_catalogo_risk_codigo_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE tiws_risk_catalogo_risk_codigo_seq OWNED BY tiws_risk_catalogo.risk_codigo;


--
-- TOC entry 164 (class 1259 OID 127585)
-- Dependencies: 1947 6
-- Name: tiws_risk_ratios_hoy; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_risk_ratios_hoy (
    raho_cod_riesgo smallint NOT NULL,
    raho_cod_dato smallint NOT NULL,
    raho_fec_riesgo date,
    raho_cat_dato character(6) NOT NULL,
    raho_dia_llamadas integer,
    raho_dia_minutos numeric,
    raho_ind_umb_llamadas numeric,
    raho_ind_umb_minutos numeric,
    raho_aye_llamadas integer,
    raho_aye_minutos numeric,
    raho_ind_aye_llamadas numeric,
    raho_ind_aye_minutos numeric,
    raho_avg_xda_llamadas numeric,
    raho_avg_xda_minutos numeric,
    raho_ind_avg_xda_llamadas numeric,
    raho_ind_avg_xda_minutos numeric,
    raho_avg_xdp_llamadas numeric,
    raho_avg_xdp_minutos numeric,
    raho_ind_avg_xdp_llamadas numeric,
    raho_ind_avg_xdp_minutos numeric,
    raho_dst_xda_llamadas numeric,
    raho_dst_xda_minutos numeric,
    raho_ind_dst_xda_llamadas numeric,
    raho_ind_dst_xda_minutos numeric,
    raho_dst_xdp_llamadas numeric,
    raho_dst_xdp_minutos numeric,
    raho_ind_dst_xdp_llamadas numeric,
    raho_ind_dst_xdp_minutos numeric DEFAULT 0,
    raho_where_coho character varying(250),
    raho_where_codi character(250),
    raho_where_tasa character(250)
);


ALTER TABLE public.tiws_risk_ratios_hoy OWNER TO postgres;

--
-- TOC entry 167 (class 1259 OID 135362)
-- Dependencies: 1950 1951 1952 6
-- Name: tiws_risk_trafico_cab; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_risk_trafico_cab (
    trca_proceso integer NOT NULL,
    trca_cod_riesgo smallint NOT NULL,
    trca_cod_dato smallint NOT NULL,
    trca_fec_riesgo date,
    trca_cat_dato character(6) NOT NULL,
    trca_dia_llamadas integer,
    trca_dia_minutos numeric,
    trca_ind_umb_llamadas numeric,
    trca_ind_umb_minutos numeric,
    trca_aye_llamadas integer,
    trca_aye_minutos numeric,
    trca_ind_aye_llamadas numeric,
    trca_ind_aye_minutos numeric,
    trca_avg_xda_llamadas numeric,
    trca_avg_xda_minutos numeric,
    trca_ind_avg_xda_llamadas numeric,
    trca_ind_avg_xda_minutos numeric,
    trca_avg_xdp_llamadas numeric,
    trca_avg_xdp_minutos numeric,
    trca_ind_avg_xdp_llamadas numeric,
    trca_ind_avg_xdp_minutos numeric,
    trca_dst_xda_llamadas numeric,
    trca_dst_xda_minutos numeric,
    trca_ind_dst_xda_llamadas numeric,
    trca_ind_dst_xda_minutos numeric,
    trca_dst_xdp_llamadas numeric,
    trca_dst_xdp_minutos numeric,
    trca_ind_dst_xdp_llamadas numeric,
    trca_ind_dst_xdp_minutos numeric DEFAULT 0,
    trca_where_coho character varying(250),
    trca_where_codi character(250),
    trca_where_tasa character(250),
    trca_distinto_fonoa integer DEFAULT 0,
    trca_distinto_fonob integer DEFAULT 0,
    trca_ind_avg_hoy_llamadas numeric,
    trca_ind_avg_hoy_minutos numeric
);


ALTER TABLE public.tiws_risk_trafico_cab OWNER TO postgres;

--
-- TOC entry 198 (class 1259 OID 283151)
-- Dependencies: 1975 1976 1977 6
-- Name: tiws_risk_trafico_cab_dia; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_risk_trafico_cab_dia (
    trca_proceso integer NOT NULL,
    trca_cod_riesgo smallint NOT NULL,
    trca_cod_dato smallint NOT NULL,
    trca_fec_riesgo date NOT NULL,
    trca_cat_dato character(6) NOT NULL,
    trca_dia_llamadas integer,
    trca_dia_minutos numeric,
    trca_ind_umb_llamadas numeric,
    trca_ind_umb_minutos numeric,
    trca_aye_llamadas integer,
    trca_aye_minutos numeric,
    trca_ind_aye_llamadas numeric,
    trca_ind_aye_minutos numeric,
    trca_avg_xda_llamadas numeric,
    trca_avg_xda_minutos numeric,
    trca_ind_avg_xda_llamadas numeric,
    trca_ind_avg_xda_minutos numeric,
    trca_avg_xdp_llamadas numeric,
    trca_avg_xdp_minutos numeric,
    trca_ind_avg_xdp_llamadas numeric,
    trca_ind_avg_xdp_minutos numeric,
    trca_dst_xda_llamadas numeric,
    trca_dst_xda_minutos numeric,
    trca_ind_dst_xda_llamadas numeric,
    trca_ind_dst_xda_minutos numeric,
    trca_dst_xdp_llamadas numeric,
    trca_dst_xdp_minutos numeric,
    trca_ind_dst_xdp_llamadas numeric,
    trca_ind_dst_xdp_minutos numeric DEFAULT 0,
    trca_where_coho character varying(250),
    trca_where_codi character(250),
    trca_where_tasa character(250),
    trca_distinto_fonoa integer DEFAULT 0,
    trca_distinto_fonob integer DEFAULT 0,
    trca_ind_avg_hoy_llamadas numeric,
    trca_ind_avg_hoy_minutos numeric
);


ALTER TABLE public.tiws_risk_trafico_cab_dia OWNER TO postgres;

--
-- TOC entry 191 (class 1259 OID 155465)
-- Dependencies: 6
-- Name: tiws_risk_trafico_det; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_risk_trafico_det (
    trde_proceso integer NOT NULL,
    trde_cod_riesgo smallint NOT NULL,
    trde_tip_analisis character(10) NOT NULL,
    trde_cod_dato character(20) NOT NULL,
    trde_des_dato character(60) NOT NULL,
    trde_tip_valor character(10) NOT NULL,
    trde_fec_riesgo date NOT NULL,
    trde_dia_llamadas integer,
    trde_dia_minutos numeric,
    trde_dia_valor numeric
);


ALTER TABLE public.tiws_risk_trafico_det OWNER TO postgres;

--
-- TOC entry 199 (class 1259 OID 283161)
-- Dependencies: 6
-- Name: tiws_risk_trafico_det_dia; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_risk_trafico_det_dia (
    trde_proceso integer NOT NULL,
    trde_cod_riesgo smallint NOT NULL,
    trde_tip_analisis character(10) NOT NULL,
    trde_cod_dato character(20) NOT NULL,
    trde_des_dato character(60) NOT NULL,
    trde_tip_valor character(10) NOT NULL,
    trde_fec_riesgo date NOT NULL,
    trde_dia_llamadas integer,
    trde_dia_minutos numeric,
    trde_dia_valor numeric
);


ALTER TABLE public.tiws_risk_trafico_det_dia OWNER TO postgres;

--
-- TOC entry 180 (class 1259 OID 136111)
-- Dependencies: 6
-- Name: tiws_risk_trafico_diario; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_risk_trafico_diario (
    trdi_fecha date NOT NULL,
    trdi_cod_riesgo smallint NOT NULL,
    trdi_cod_destino smallint NOT NULL,
    trdi_dato_analisis character(10),
    trdi_dato_analisis_codigo character(10),
    trdi_dato_analisis_descripcion character(30),
    trde_dia_llamadas integer,
    trde_dia_minutos numeric,
    trde_dia_cantidad integer
);


ALTER TABLE public.tiws_risk_trafico_diario OWNER TO postgres;

--
-- TOC entry 151 (class 1259 OID 119020)
-- Dependencies: 6
-- Name: tiws_risk_umbrales; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_risk_umbrales (
    umbr_dominio smallint NOT NULL,
    umbr_nivel smallint NOT NULL,
    umbr_descripcion character(30),
    umbr_largo character(100),
    umbr_llamadas smallint,
    umbr_minutos smallint,
    umbr_cantidad smallint,
    umbr_rangoinicio numeric,
    umbr_rangofinal numeric,
    umbr_estado character(1),
    umbr_bajo_minutos numeric,
    umbr_medio_minutos numeric,
    umbr_alto_minutos numeric,
    umbr_muyalto_minutos numeric,
    umbr_extremo_minutos numeric
);


ALTER TABLE public.tiws_risk_umbrales OWNER TO postgres;


--
-- TOC entry 116 (class 1259 OID 72807)
-- Dependencies: 6
-- Name: tiws_ruta; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_ruta (
    ruta_codigo character(6) NOT NULL,
    ruta_descripcion character(50),
    ruta_switch smallint NOT NULL,
    ruta_tipotrafico character(5),
    ruta_fechainicio date NOT NULL,
    ruta_fechafinal date,
    ruta_grupo character(50),
    ruta_carrier character(5),
    ruta_observacion character(60)
);


ALTER TABLE public.tiws_ruta OWNER TO postgres;

--
-- TOC entry 141 (class 1259 OID 86304)
-- Dependencies: 6
-- Name: tiws_rutaenblanco; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_rutaenblanco (
    rubl_secuenciaproceso bigint NOT NULL,
    rubl_secuenciaregistro bigint NOT NULL,
    rubl_fechahora timestamp without time zone NOT NULL,
    rubl_numeroorigen character(20),
    rubl_numerodestino character(20),
    rubl_rutaentrada character(20),
    rubl_rutasalida character(20),
    rubl_ip_entrada character(15),
    rubl_ip_salida character(15),
    rubl_segundos integer,
    rubl_salidaparcial integer,
    rubl_numregparcial integer,
    rubl_error smallint,
    rubl_observacion character(100),
    rubl_id_call character(20)
);


ALTER TABLE public.tiws_rutaenblanco OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 375724)
-- Dependencies: 6
-- Name: tiws_seriesespeciales; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_seriesespeciales (
    ssee_numero character(20) NOT NULL,
    ssee_orig_carrier character(5),
    ssee_orig_numero character(20),
    ssee_orig_proveedor character(5),
    ssee_dest_numero character(20),
    ssee_dest_proveedor character(5),
    ssee_dest_carrier character(5),
    ssee_dest_pais character(5),
    ssee_dest_cliente character(70),
    ssee_tipo_acceso character(5),
    ssee_tipo_servicio character(5),
    ssee_fecha_alta date NOT NULL,
    ssee_fecha_baja date,
    ssee_banda_subex character(70),
    ssee_observacion character(150),
    ssee_orig_carrier_descr character(70),
    ssee_dest_proveedor_descr character(70),
    ssee_dest_carr_terminal character(40)
);


ALTER TABLE public.tiws_seriesespeciales OWNER TO postgres;

--
-- TOC entry 117 (class 1259 OID 72826)
-- Dependencies: 6
-- Name: tiws_seriesnumericas; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_seriesnumericas (
    senu_numero character(20) NOT NULL,
    senu_pais character(5),
    senu_tipodestino character(10),
    senu_servicio character(5),
    senu_destino character(10),
    senu_area_operador character(40),
    senu_fechainicio date NOT NULL,
    senu_fechafinal date,
    senu_fechadeuso date,
    senu_fechaload timestamp without time zone,
    senu_fuente character(50),
    senu_observacion character(100)
);


ALTER TABLE public.tiws_seriesnumericas OWNER TO postgres;

--
-- TOC entry 257 (class 1259 OID 418719)
-- Dependencies: 6
-- Name: tiws_seriesnumericas_bck; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_seriesnumericas_bck (
    senu_numero character(20) NOT NULL,
    senu_pais character(5),
    senu_tipodestino character(10),
    senu_servicio character(5),
    senu_destino character(10),
    senu_area_operador character(40),
    senu_fechainicio date NOT NULL,
    senu_fechafinal date,
    senu_fechadeuso date,
    senu_fechaload timestamp without time zone,
    senu_fuente character(50),
    senu_observacion character(100)
);


ALTER TABLE public.tiws_seriesnumericas_bck OWNER TO postgres;

--
-- TOC entry 113 (class 1259 OID 72757)
-- Dependencies: 6
-- Name: tiws_servicio; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_servicio (
    serv_codigo character(5) NOT NULL,
    serv_descripcion character(50),
    serv_sigla character(5),
    serv_tiposervicio character(5)
);


ALTER TABLE public.tiws_servicio OWNER TO postgres;

SET default_tablespace = '';

--
-- TOC entry 200 (class 1259 OID 296128)
-- Dependencies: 6
-- Name: tiws_servicioespecial; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_servicioespecial (
    ssee_acceso_tgsol character(20) NOT NULL,
    ssee_cod_oper_origen character(5),
    ssee_des_oper_origen character(30),
    ssee_cod_oper_proveedor character(5),
    ssee_des_oper_proveedor character(30),
    ssee_cod_pais_destino character(5),
    ssee_des_pais_destino character(30),
    ssee_acceso_origen character(20),
    ssee_acceso_saliente character(20),
    ssee_cod_rutasaliente character(5),
    ssee_des_rutasaliente character(30),
    ssee_fecha_alta date NOT NULL,
    ssee_fecha_baja date,
    ssee_activo smallint,
    ssee_comentario character(100),
    ssee_servicio character(5)
);


ALTER TABLE public.tiws_servicioespecial OWNER TO postgres;


--
-- TOC entry 197 (class 1259 OID 164186)
-- Dependencies: 6
-- Name: tiws_ssee; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_ssee (
    ssee_numero character(20) NOT NULL,
    ssee_pais character(5),
    ssee_tipodestino character(10),
    ssee_servicio character(5),
    ssee_destino character(10),
    ssee_operador character(5),
    ssee_fechainicio date NOT NULL,
    ssee_fechafinal date,
    ssee_fechadeuso date,
    ssee_fechaload timestamp without time zone,
    ssee_fuente character(50),
    ssee_observacion character(100)
);


ALTER TABLE public.tiws_ssee OWNER TO postgres;

--
-- TOC entry 195 (class 1259 OID 158164)
-- Dependencies: 1974 6
-- Name: tiws_sumbase_cab_xnumerodestino_hoy; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_sumbase_cab_xnumerodestino_hoy (
    sndh_cab_nume_proceso integer NOT NULL,
    sndh_cab_fecha date NOT NULL,
    sndh_cab_nume_destino character(20) NOT NULL,
    sndh_cab_dist_pais integer,
    sndh_cab_dist_carrier integer,
    sndh_cab_dist_numo integer,
    sndh_cab_dist_paisesrisk integer,
    sndh_cab_risk_llamadas integer,
    sndh_cab_risk_minutos numeric,
    sndh_cab_suma_llamadas integer,
    sndh_cab_suma_minutos numeric,
    sndh_cab_flag_conservar boolean DEFAULT false
);


ALTER TABLE public.tiws_sumbase_cab_xnumerodestino_hoy OWNER TO postgres;

--
-- TOC entry 194 (class 1259 OID 157475)
-- Dependencies: 1973 6
-- Name: tiws_sumbase_cab_xnumeroorigen_hoy; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_sumbase_cab_xnumeroorigen_hoy (
    snoh_cab_nume_proceso integer NOT NULL,
    snoh_cab_fecha date NOT NULL,
    snoh_cab_nume_origen character(20) NOT NULL,
    snoh_cab_dist_pais integer,
    snoh_cab_dist_carrier integer,
    snoh_cab_dist_numb integer,
    snoh_cab_dist_paisesrisk integer,
    snoh_cab_risk_llamadas integer,
    snoh_cab_risk_minutos numeric,
    snoh_cab_suma_llamadas integer,
    snoh_cab_suma_minutos numeric,
    snoh_cab_flag_conservar boolean DEFAULT false
);


ALTER TABLE public.tiws_sumbase_cab_xnumeroorigen_hoy OWNER TO postgres;

--
-- TOC entry 193 (class 1259 OID 157351)
-- Dependencies: 1972 6
-- Name: tiws_sumbase_det_xnumerodestino_hoy; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_sumbase_det_xnumerodestino_hoy (
    sndh_nume_proceso integer NOT NULL,
    sndh_fecha date NOT NULL,
    sndh_numerodestino character(20) NOT NULL,
    sndh_orig_pais character(5) NOT NULL,
    sndh_orig_area character(10) NOT NULL,
    sndh_ruen_carrier character(5) NOT NULL,
    sndh_ruen_pais character(5) NOT NULL,
    sndh_dest_pais character(5) NOT NULL,
    sndh_dest_area character(10) NOT NULL,
    sndh_rusa_carrier character(5) NOT NULL,
    sndh_rusa_pais character(5) NOT NULL,
    sndh_suma_llamadas integer,
    sndh_suma_minutos numeric,
    sndh_codi_riesgo smallint,
    sndh_clave character(50),
    sndh_flag_conservar boolean DEFAULT false
);


ALTER TABLE public.tiws_sumbase_det_xnumerodestino_hoy OWNER TO postgres;

--
-- TOC entry 181 (class 1259 OID 147366)
-- Dependencies: 1965 6
-- Name: tiws_sumbase_det_xnumeroorigen_hoy; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_sumbase_det_xnumeroorigen_hoy (
    snoh_nume_proceso integer NOT NULL,
    snoh_fecha date NOT NULL,
    snoh_numeroorigen character(20) NOT NULL,
    snoh_orig_pais character(5) NOT NULL,
    snoh_orig_area character(10) NOT NULL,
    snoh_ruen_carrier character(5) NOT NULL,
    snoh_ruen_pais character(5) NOT NULL,
    snoh_dest_pais character(5) NOT NULL,
    snoh_dest_area character(10) NOT NULL,
    snoh_rusa_carrier character(5) NOT NULL,
    snoh_rusa_pais character(5) NOT NULL,
    snoh_suma_llamadas integer,
    snoh_suma_minutos numeric,
    snoh_codi_riesgo smallint,
    snoh_clave character(50),
    snoh_flag_conservar boolean DEFAULT false
);


ALTER TABLE public.tiws_sumbase_det_xnumeroorigen_hoy OWNER TO postgres;

SET default_tablespace = '';

--
-- TOC entry 149 (class 1259 OID 118980)
-- Dependencies: 6
-- Name: tiws_tablas; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_tablas (
    tabl_codigo character(6) NOT NULL,
    tabl_descripcion character(30)
);


ALTER TABLE public.tiws_tablas OWNER TO postgres;

--
-- TOC entry 150 (class 1259 OID 118988)
-- Dependencies: 6
-- Name: tiws_tablas_campos; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiws_tablas_campos (
    camp_codigo character(6) NOT NULL,
    camp_tabla character(6) NOT NULL,
    camp_descripcion character(30)
);


ALTER TABLE public.tiws_tablas_campos OWNER TO postgres;


--
-- TOC entry 126 (class 1259 OID 74148)
-- Dependencies: 6
-- Name: tiws_tasacion; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_tasacion (
    tasa_secuenciaproceso bigint NOT NULL,
    tasa_secuenciaregistro bigint NOT NULL,
    tasa_secuenciareproceso bigint,
    tasa_fechahora timestamp without time zone NOT NULL,
    tasa_numeroorigen character(20) NOT NULL,
    tasa_nuor_pais character(5),
    tasa_nuor_operador character(10),
    tasa_nuor_ciudad character(10),
    tasa_nuor_servicio character(5),
    tasa_numerodestino character(20) NOT NULL,
    tasa_nude_pais character(5),
    tasa_nude_operador character(10),
    tasa_nude_ciudad character(10),
    tasa_nude_servicio character(5),
    tasa_numerossee character(20),
    tasa_rutaentrada character(20) NOT NULL,
    tasa_ruen_operador character(5),
    tasa_ruen_pais character(5),
    tasa_ruen_servicio character(5),
    tasa_rutasalida character(20) NOT NULL,
    tasa_rusa_operador character(10),
    tasa_rusa_pais character(5),
    tasa_rusa_servicio character(5),
    tasa_prefijo character(8),
    tasa_segundos integer NOT NULL,
    tasa_modalidad character(5),
    tasa_seor_serie character(20),
    tasa_seor_operador character(10),
    tasa_seor_servicio character(5),
    tasa_seor_ciudad character(8),
    tasa_sede_serie character(20),
    tasa_sede_operador character(10),
    tasa_sede_servicio character(5),
    tasa_sede_ciudad character(8),
    tasa_sse_flag character(1),
    tasa_fuente smallint NOT NULL,
    tasa_flagcruce smallint,
    tasa_observacion character(100),
    tasa_match_fecha date,
    tasa_match_hora character(2),
    tasa_match_xxxx smallint
);


ALTER TABLE public.tiws_tasacion OWNER TO postgres;

--
-- TOC entry 168 (class 1259 OID 135931)
-- Dependencies: 1953 6 126
-- Name: tiws_tasacion_201501; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_tasacion_201501 (CONSTRAINT tiws_tasacion_201501_tasa_match_fecha_check CHECK (((tasa_match_fecha >= '2015-01-01'::date) AND (tasa_match_fecha < '2015-02-01'::date)))
)
INHERITS (tiws_tasacion);


ALTER TABLE public.tiws_tasacion_201501 OWNER TO postgres;

--
-- TOC entry 169 (class 1259 OID 135939)
-- Dependencies: 1954 6 126
-- Name: tiws_tasacion_201502; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_tasacion_201502 (CONSTRAINT tiws_tasacion_201502_tasa_match_fecha_check CHECK (((tasa_match_fecha >= '2015-02-01'::date) AND (tasa_match_fecha < '2015-03-01'::date)))
)
INHERITS (tiws_tasacion);


ALTER TABLE public.tiws_tasacion_201502 OWNER TO postgres;

--
-- TOC entry 170 (class 1259 OID 135947)
-- Dependencies: 1955 6 126
-- Name: tiws_tasacion_201503; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_tasacion_201503 (CONSTRAINT tiws_tasacion_201503_tasa_match_fecha_check CHECK (((tasa_match_fecha >= '2015-03-01'::date) AND (tasa_match_fecha < '2015-04-01'::date)))
)
INHERITS (tiws_tasacion);


ALTER TABLE public.tiws_tasacion_201503 OWNER TO postgres;

--
-- TOC entry 171 (class 1259 OID 135955)
-- Dependencies: 1956 6 126
-- Name: tiws_tasacion_201504; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_tasacion_201504 (CONSTRAINT tiws_tasacion_201504_tasa_match_fecha_check CHECK (((tasa_match_fecha >= '2015-04-01'::date) AND (tasa_match_fecha < '2015-05-01'::date)))
)
INHERITS (tiws_tasacion);


ALTER TABLE public.tiws_tasacion_201504 OWNER TO postgres;

--
-- TOC entry 172 (class 1259 OID 135963)
-- Dependencies: 1957 6 126
-- Name: tiws_tasacion_201505; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_tasacion_201505 (CONSTRAINT tiws_tasacion_201505_tasa_match_fecha_check CHECK (((tasa_match_fecha >= '2015-05-01'::date) AND (tasa_match_fecha < '2015-06-01'::date)))
)
INHERITS (tiws_tasacion);


ALTER TABLE public.tiws_tasacion_201505 OWNER TO postgres;

--
-- TOC entry 173 (class 1259 OID 135971)
-- Dependencies: 1958 6 126
-- Name: tiws_tasacion_201506; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_tasacion_201506 (CONSTRAINT tiws_tasacion_201506_tasa_match_fecha_check CHECK (((tasa_match_fecha >= '2015-06-01'::date) AND (tasa_match_fecha < '2015-07-01'::date)))
)
INHERITS (tiws_tasacion);


ALTER TABLE public.tiws_tasacion_201506 OWNER TO postgres;

--
-- TOC entry 174 (class 1259 OID 135979)
-- Dependencies: 1959 6 126
-- Name: tiws_tasacion_201507; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_tasacion_201507 (CONSTRAINT tiws_tasacion_201507_tasa_match_fecha_check CHECK (((tasa_match_fecha >= '2015-07-01'::date) AND (tasa_match_fecha < '2015-08-01'::date)))
)
INHERITS (tiws_tasacion);


ALTER TABLE public.tiws_tasacion_201507 OWNER TO postgres;

--
-- TOC entry 175 (class 1259 OID 135987)
-- Dependencies: 1960 6 126
-- Name: tiws_tasacion_201508; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_tasacion_201508 (CONSTRAINT tiws_tasacion_201508_tasa_match_fecha_check CHECK (((tasa_match_fecha >= '2015-08-01'::date) AND (tasa_match_fecha < '2015-09-01'::date)))
)
INHERITS (tiws_tasacion);


ALTER TABLE public.tiws_tasacion_201508 OWNER TO postgres;

--
-- TOC entry 176 (class 1259 OID 135995)
-- Dependencies: 1961 6 126
-- Name: tiws_tasacion_201509; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_tasacion_201509 (CONSTRAINT tiws_tasacion_201509_tasa_match_fecha_check CHECK (((tasa_match_fecha >= '2015-09-01'::date) AND (tasa_match_fecha < '2015-10-01'::date)))
)
INHERITS (tiws_tasacion);


ALTER TABLE public.tiws_tasacion_201509 OWNER TO postgres;

--
-- TOC entry 177 (class 1259 OID 136003)
-- Dependencies: 1962 6 126
-- Name: tiws_tasacion_201510; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_tasacion_201510 (CONSTRAINT tiws_tasacion_201510_tasa_match_fecha_check CHECK (((tasa_match_fecha >= '2015-10-01'::date) AND (tasa_match_fecha < '2015-11-01'::date)))
)
INHERITS (tiws_tasacion);


ALTER TABLE public.tiws_tasacion_201510 OWNER TO postgres;

--
-- TOC entry 178 (class 1259 OID 136011)
-- Dependencies: 1963 6 126
-- Name: tiws_tasacion_201511; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_tasacion_201511 (CONSTRAINT tiws_tasacion_201511_tasa_match_fecha_check CHECK (((tasa_match_fecha >= '2015-11-01'::date) AND (tasa_match_fecha < '2015-12-01'::date)))
)
INHERITS (tiws_tasacion);


ALTER TABLE public.tiws_tasacion_201511 OWNER TO postgres;

--
-- TOC entry 179 (class 1259 OID 136019)
-- Dependencies: 1964 6 126
-- Name: tiws_tasacion_201512; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_tasacion_201512 (CONSTRAINT tiws_tasacion_201512_tasa_match_fecha_check CHECK (((tasa_match_fecha >= '2015-12-01'::date) AND (tasa_match_fecha < '2016-01-01'::date)))
)
INHERITS (tiws_tasacion);


ALTER TABLE public.tiws_tasacion_201512 OWNER TO postgres;

--
-- TOC entry 231 (class 1259 OID 397302)
-- Dependencies: 2011 6 126
-- Name: tiws_tasacion_201601; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_tasacion_201601 (CONSTRAINT tiws_tasacion_201601_tasa_match_fecha_check CHECK (((tasa_match_fecha >= '2016-01-01'::date) AND (tasa_match_fecha < '2016-02-01'::date)))
)
INHERITS (tiws_tasacion);


ALTER TABLE public.tiws_tasacion_201601 OWNER TO postgres;

--
-- TOC entry 232 (class 1259 OID 397309)
-- Dependencies: 2012 6 126
-- Name: tiws_tasacion_201602; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_tasacion_201602 (CONSTRAINT tiws_tasacion_201602_tasa_match_fecha_check CHECK (((tasa_match_fecha >= '2016-02-01'::date) AND (tasa_match_fecha < '2016-03-01'::date)))
)
INHERITS (tiws_tasacion);


ALTER TABLE public.tiws_tasacion_201602 OWNER TO postgres;

--
-- TOC entry 233 (class 1259 OID 397316)
-- Dependencies: 2013 6 126
-- Name: tiws_tasacion_201603; Type: TABLE; Schema: public; Owner: postgres; Tablespace: tasp_miami
--

CREATE TABLE tiws_tasacion_201603 (CONSTRAINT tiws_tasacion_201603_tasa_match_fecha_check CHECK (((tasa_match_fecha >= '2016-03-01'::date) AND (tasa_match_fecha < '2016-04-01'::date)))
)
INHERITS (tiws_tasacion);



CREATE TABLE tiws_tasacion_201604 (CONSTRAINT tiws_tasacion_201604_tasa_match_fecha_check CHECK (((tasa_match_fecha >= '2016-04-01'::date) AND (tasa_match_fecha < '2016-05-01'::date)))
)
INHERITS (tiws_tasacion);


CREATE TABLE tiws_tasacion_201605 (CONSTRAINT tiws_tasacion_201605_tasa_match_fecha_check CHECK (((tasa_match_fecha >= '2016-05-01'::date) AND (tasa_match_fecha < '2016-06-01'::date)))
)
INHERITS (tiws_tasacion);







CREATE TABLE tiws_tasacion_solohoy (
    tasa_secuenciaproceso bigint NOT NULL,
    tasa_secuenciaregistro bigint NOT NULL,
    tasa_secuenciareproceso bigint,
    tasa_fechahora timestamp without time zone NOT NULL,
    tasa_numeroorigen character(20) NOT NULL,
    tasa_nuor_pais character(5),
    tasa_nuor_operador character(10),
    tasa_nuor_ciudad character(10),
    tasa_nuor_servicio character(5),
    tasa_numerodestino character(20) NOT NULL,
    tasa_nude_pais character(5),
    tasa_nude_operador character(10),
    tasa_nude_ciudad character(10),
    tasa_nude_servicio character(5),
    tasa_numerossee character(20),
    tasa_rutaentrada character(20) NOT NULL,
    tasa_ruen_operador character(5),
    tasa_ruen_pais character(5),
    tasa_ruen_servicio character(5),
    tasa_rutasalida character(20) NOT NULL,
    tasa_rusa_operador character(10),
    tasa_rusa_pais character(5),
    tasa_rusa_servicio character(5),
    tasa_prefijo character(8),
    tasa_segundos integer NOT NULL,
    tasa_modalidad character(5),
    tasa_seor_serie character(20),
    tasa_seor_operador character(10),
    tasa_seor_servicio character(5),
    tasa_seor_ciudad character(8),
    tasa_sede_serie character(20),
    tasa_sede_operador character(10),
    tasa_sede_servicio character(5),
    tasa_sede_ciudad character(8),
    tasa_sse_flag character(1),
    tasa_fuente smallint NOT NULL,
    tasa_flagcruce smallint,
    tasa_observacion character(100),
    tasa_match_fecha date,
    tasa_match_hora character(2),
    tasa_match_xxxx smallint
);




CREATE TABLE tiws_tasacion_tuku (
    tasa_secuenciaproceso bigint NOT NULL,
    tasa_secuenciaregistro bigint NOT NULL,
    tasa_secuenciareproceso bigint,
    tasa_fechahora timestamp without time zone NOT NULL,
    tasa_numeroorigen character(20) NOT NULL,
    tasa_nuor_pais character(5),
    tasa_nuor_operador character(10),
    tasa_nuor_ciudad character(10),
    tasa_nuor_servicio character(5),
    tasa_numerodestino character(20) NOT NULL,
    tasa_nude_pais character(5),
    tasa_nude_operador character(10),
    tasa_nude_ciudad character(10),
    tasa_nude_servicio character(5),
    tasa_numerossee character(20),
    tasa_rutaentrada character(20) NOT NULL,
    tasa_ruen_operador character(5),
    tasa_ruen_pais character(5),
    tasa_ruen_servicio character(5),
    tasa_rutasalida character(20) NOT NULL,
    tasa_rusa_operador character(10),
    tasa_rusa_pais character(5),
    tasa_rusa_servicio character(5),
    tasa_prefijo character(8),
    tasa_segundos integer NOT NULL,
    tasa_modalidad character(5),
    tasa_seor_serie character(20),
    tasa_seor_operador character(10),
    tasa_seor_servicio character(5),
    tasa_seor_ciudad character(8),
    tasa_sede_serie character(20),
    tasa_sede_operador character(10),
    tasa_sede_servicio character(5),
    tasa_sede_ciudad character(8),
    tasa_sse_flag character(1),
    tasa_fuente smallint NOT NULL,
    tasa_flagcruce smallint,
    tasa_observacion character(100),
    tasa_match_fecha date,
    tasa_match_hora character(2),
    tasa_match_xxxx smallint
);



CREATE TABLE tiws_x_areas (
    grp character(10) NOT NULL,
    area character(100) NOT NULL,
    count smallint
);



CREATE TABLE tmp_david (
    c1 numeric,
    c2 numeric(6,2),
    c3 numeric(2,2),
    c4 numeric(10,2)
);



CREATE TABLE tmp_match_carr_terminal (
    temp_carrier_terminal character(30),
    carr_codigo character(5),
    carr_descripcion character(50),
    count bigint
);




CREATE TABLE tmp_match_origen (
    temp_origen character(70),
    carr_origen character varying(5),
    carr_descripcion character(50),
    count bigint
);




CREATE TABLE tmp_match_origen_tmp (
    temp_origen character(70),
    carr_origen character varying(5),
    carr_descripcion character(50),
    count bigint
);




CREATE TABLE tmp_match_proveedor (
    temp_proveedor character(70),
    temp_etis_proveedor character(8),
    carr_descripcion character(50),
    count bigint
);



CREATE TABLE tmp_nacho_analisis_1 (
    pais_local character(5),
    nume_local character(20),
    sali_dias smallint,
    entr_dias smallint,
    sali_llamadas integer DEFAULT 0,
    sali_minutos numeric DEFAULT 0,
    entr_llamadas integer DEFAULT 0,
    entr_minutos numeric DEFAULT 0,
    caso_estado character(10)
);



CREATE TABLE tmp_nacho_detalle (
    tipo_movi character(3),
    sali_fecha date,
    entr_fecha date,
    pais_local character(5),
    pais_extranjero character(5),
    nume_local character(20),
    sali_llamadas integer,
    sali_minutos numeric,
    entr_llamadas integer,
    entr_minutos numeric
);




CREATE TABLE tmp_nori_a (
    fecha date,
    nume_origen bpchar,
    long_nume_origen integer,
    total_llamadas bigint,
    total_minutos numeric
);




CREATE TABLE tmp_nori_b (
    "?column?" "unknown",
    fecha date,
    nume_origen bpchar,
    long_nume_origen integer,
    nuor_pais character(5),
    nuor_area character(10),
    ruen_oper character(5),
    ruen_pais character(5),
    total_llamadas bigint,
    total_minutos numeric
);



CREATE TABLE tmp_tablamedida (
    pais character(1000),
    estado character(1000),
    prefijo character(1000),
    areaoperador character(1000),
    grupo character(1000),
    tipo character(1000),
    servicio character(1000),
    fecha character varying(12),
    observaciones character(1000),
    date date
);




CREATE TABLE wi_existe_tmp (
    count bigint
);



CREATE TABLE x_servicios (
    servicio character(1000)
);



CREATE TABLE xpais (
    pais character(1000)
);



CREATE TABLE xpaisd (
    btrim text
);



CREATE TABLE xxxx_consolidado_hoy (
    nuor_pais character(5),
    nuor_ciud character(10),
    nude_pais character(5),
    nude_ciud character(10),
    ruen_oper character(5),
    ruen_pais character(5),
    rusa_oper character(10),
    rusa_pais character(5),
    tasa_sse_flag character(1),
    tota_llam bigint,
    tota_segu bigint
);



