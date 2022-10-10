from py_scripts import test
from Dashboard import models


def get_id(query, connection):
    result = test.execute(query, connection);
    if result[1][0][0] == None:
        if "EDI" in query:
            id = 3944000480;
        else:
            id = 1001
    else:
        id = result[1][0][0]
    return id

def execute_query(query, config):
    connection = test.connect(config);
    result=test.execute(query,connection);
    print(result)
    return result;

def generate_query(data, config):
    print(data.get('bi_id'))
    bi_id_query='';
    edi_ref_query='';
    bili_id_query='';
    bill_cust_id_query='';
    bill_interface_query='';
    query_set=models.Query_set.objects.all();
    for query in query_set:
        if query.table_name=='bi_id':
            bi_id_query=query.query;
        elif query.table_name=='edi_ref':
            edi_ref_query=query.query;
        elif query.table_name=='bili_id':
            bili_id_query=query.query;
        elif query.table_name=='bill_cust_id':
            bill_cust_id_query=query.query;
        elif query.table_name=='bill_interface':
            bill_interface_query=query.query;
    connection = test.connect(config);
    bi_id = get_id(bi_id_query, connection);
    edi_ref = get_id(edi_ref_query, connection);
    bili_id = get_id(bili_id_query, connection);
    bill_cust_id = get_id(bill_cust_id_query, connection);
    result = []
    bill_interface = """Insert into PCMP.BILL_INTERFACE (BI_ID,BI_CLAIM_NO,BI_BILL_NO,BI_EDI_REF_NO_PRI,BI_EDI_REF_NO_SECD,BI_CNV_NO,BI_EDI_SRC_TYP_CD,BI_PTCP_PAY_IND,BI_NOTE_IND,BI_OPN_DT,BI_COMP_DT,BI_REOPN_DT,BI_RECOMP_DT,BI_LST_TRAN_DT,BI_FRMT_TYP_CD,BI_SRC_TYP_CD,BI_MEDA_TYP_CD,BI_SERV_EFF_DT,BI_SERV_END_DT,BI_RECV_DT,BI_NOTE_ATTCH_IND,BI_FEE_SCH_OVRRD_IND,BI_FEE_SCH_OVRRD_RSN_TYP_CD,BI_FAST_TRK_ACTN_TYP_CD,BI_BFTART_CD,BI_CHR_TOT_AMT,BI_CST_CNTR_TYP_CD,BI_PAY_TYP_CD,BI_SUM_SBM_AMT,BI_SUM_APRV_AMT,BI_SUM_PD_AMT,BI_REF_NO,BI_MED_REC_NO,BI_ADMIT_DTM,BI_DISC_DTM,BI_LNGTH_OF_STAY_DD,BI_DRG_CD,BI_DRG_DESC,BI_DRG_VRFD_IND,BI_ADJ_DRG_CD,BI_ADJ_DRG_DESC,BI_ADJ_DRG_VRFD_IND,BI_UB92_TYP_CD,BI_UB92_TYP_DESC,BI_UB92_TYP_VRFD_IND,BI_ICD_SBM_ADMIT_CD,BI_ICD_SBM_ADMIT_DESC,BI_ICD_ADMIT_CD,BI_ICD_ADMIT_DESC,BI_ICD_ADMIT_VRFD_IND,BI_ICD_VER_CD,BI_PAY_REQS_ID,BI_STS_TYP_CD,BI_STS_EFF_DT,BI_STT_TYP_CD,BI_STS_STT_EFF_DT,BI_TRANS_RSN_TYP_CD,BI_STS_COMT,AUDIT_USER_ID_CREA,AUDIT_USER_CREA_DTM,AUDIT_USER_ID_UPDT,AUDIT_USER_UPDT_DTM,BI_PPY_TYP_CD,BI_PHY_LIC_NO,BI_ADMIS_TYP_CD,BI_SCH_TYP_CD,BI_OP_PHYS_LIC_NO,BI_SPL_PROC_TYP_CD,BI_SPL_PROC_AMT,BI_DO_NOT_RPT_IND,BI_DO_NOT_RPT_RSN_TYP_CD,BI_PRCS_DTM,BI_PAY_IND,BI_PAY_DTM,BI_NET_WK_SERV_IND) 
            values (""" + str(bi_id) + """,""" + \
                     data.get('claim') + """,null ,""" + str(edi_ref) + """,null,null,'brkst','n','n',
              to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'cms1500','prov','edi',to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'end_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'n','n',null,'pay','reqsserv',""" + data.get(
        'total') + """,null,'med',""" + data.get('submitted') + """,""" + data.get(
        'approved') + """,0,null,null,null,null,null,null,null,null,null,null,null,null,null,null,'354.0',null,'354.0',null,'y','9',null,'rlse',to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'opn',to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'aprv',null,0,to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),null,null,null,null,null,null,null,null,null,null,null,null,null,null,'n')
        """
    line_item = """    Insert into PCMP.BILL_INTERFACE_LINE_ITEM  (BILI_ID,BI_ID,BILI_EDI_REF_NO,BILI_SERV_EFF_DT,BILI_SERV_END_DT,BILI_TYP_CD,BILI_CD_TYP_CD_PRI,BILI_CST_CNTR_TYP_CD,BILI_PAY_TYP_CD,BILI_SBM_PRI_CD,BILI_SBM_PRI_DESC,BILI_PRI_CD,BILI_PRI_DESC,BILI_PRI_VRFD_IND,BILI_SUB_VRFD_IND,BILI_STR_TIME,BILI_END_TIME,BILI_UNT,BILI_MIN,BILI_CD_TYP_CD_SECD,BILI_SECD_CD,BILI_SECD_DESC,BILI_SECD_VRFD_IND,BILI_SERV_PLC_CD,BILI_SERV_PLC_DESC,BILI_SERV_PLC_VRFD_IND,BILI_SERV_TYP_CD,BILI_SERV_TYP_DESC,BILI_SERV_TYP_VRFD_IND,BILI_EMRG_TYP_CD,BILI_EMRG_TYP_DESC,BILI_EMRG_TYP_VRFD_IND,BILI_RX_NO,BILI_RX_SUPP_DD,BILI_RX_PROV_NM,BILI_RX_PROV_ID,BILI_PROV_ID_TYP_CD,BILI_RX_DT,BILI_TOOTH_CD,BILI_TOOTH_DESC,BILI_TOOTH_VRFD_IND,BILI_TOOTH_SRF_CD,BILI_TOOTH_SRF_DESC,BILI_TOOTH_SRF_VRFD_IND,BILI_TRVL_FR,BILI_TRVL_TO,BILI_TRVL_TYP_CD,BILI_TRVL_DST,BILI_TRVL_NET,BILI_TRVL_EXCL,BILI_TRVL_RT,BILI_TRVL_REMB,BILI_COMT,BILI_SBM_AMT,BILI_PAY_SBM_IND,BILI_APRV_AMT,BILI_PD_AMT,BILI_TAX_AMT,BILI_PENL_AMT,BILI_PRVS_PD_AMT,AUDIT_USER_ID_CREA,AUDIT_USER_CREA_DTM,AUDIT_USER_ID_UPDT,AUDIT_USER_UPDT_DTM,BILI_DISD_AS_WRTN_TYP_CD,BILI_NEW_REFL_TYP_CD,BILI_DME_OWNSHP_TYP_CD,BILI_OVRRD_FLG_IND,VOID_IND) 
        values (""" + str(bili_id) + """,""" + str(bi_id) + """,""" + str(edi_ref) + """,to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'h','hcpc','021','med','99070','SPECIAL SUPPLIES','99070','SPECIAL SUPPLIES','y','n',to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),30,null,null,null,null,'n','11','OFFICE','y',null,null,'n','n',null,'y',null,null,null,null,null,null,null,null,'n',null,null,null,null,null,null,null,null,0,null,null,null,""" + data.get(
        'submitted') + """,'n',""" + data.get('approved') + """,null,null,null,null,0,to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),null,null,null,null,'p','n','n')"""

    customer = """  Insert into PCMP.BILL_INTERFACE_CUSTOMER (BILL_INTFC_CUST_ID,BI_ID,BILL_INTFC_CUST_TYP_CD,BILL_INTFC_CUST_NM_FST,BILL_INTFC_CUST_NM_LST,BILL_INTFC_CUST_NM_MID,BILL_INTFC_CUST_PHN_NO,BILL_INTFC_CUST_PHN_EXT,BILL_INTFC_CUST_DOB,BILL_INTFC_CUST_GNDR_TYP_CD,BILL_INTFC_CUST_MAR_STS_TYP_CD,BILL_INTFC_CUST_TAX_ID_TYP_CD,BILL_INTFC_CUST_TAX_ID_NO,BILL_INTFC_CUST_ADDR_TYP_CD,BILL_INTFC_CUST_ADDR1,BILL_INTFC_CUST_ADDR2,BILL_INTFC_CUST_STT_ID,BILL_INTFC_CUST_CITY_NM,BILL_INTFC_CUST_POST_CD,BILL_INTFC_CUST_CNTRY_ID,BILL_INTFC_CUST_BILL_PROV_IND,BILL_INTFC_CUST_BILL_SERV_IND,BILL_INTFC_CUST_BILL_FACIL_IND,BILL_INTFC_CUST_NO,AUDIT_USER_ID_CREA,AUDIT_USER_CREA_DTM,AUDIT_USER_ID_UPDT,AUDIT_USER_UPDT_DTM,VOID_IND) 
        values (""" + str(bill_cust_id) + """,""" + str(
        bi_id) + """,'busn',null,'INDUSTRIAL PHARMACY MANAGEMENT LLC',null,null,null,null,null,null,'fein','100605677','mail','PO BOX 512518',null,2,'Los Angeles','90051',1,'y','n','n',""" + data.get(
        'customer') + """,0,to_timestamp('20-SEP-22 12.00.00.000000000 AM','DD-MON-RR HH.MI.SSXFF AM'),null,null,'n')
     """

    #print(bill_interface)
    #bill_interface_result="error";
    bill_interface_result = test.insert(bill_interface, connection);
    if "successfully" in bill_interface_result:
        line_item_result = test.insert(line_item, connection);
        customer_result = test.insert(customer, connection);
    result.append(bill_interface_result);
    result.append(bi_id);
    result.append(edi_ref);
    test.close(connection);
    return result


def generate_multiple_edi(data, config):
    #print('Count: ',data.get('count'))
    connection = test.connect(config);
    bi_id = get_id('select max(bi_id) from pcmp.bill_interface', connection);
    edi_ref = get_id("select max(BI_EDI_REF_NO_PRI) from pcmp.bill_interface", connection);
    bili_id = get_id('select max(BILI_ID) from pcmp.BILL_INTERFACE_LINE_ITEM', connection);
    bill_cust_id = get_id('select max(BILL_INTFC_CUST_ID) from pcmp.BILL_INTERFACE_CUSTOMER', connection);
    result = []
    count=bi_id+ int(data.get('count'));
    query = """DECLARE
    l_counter NUMBER := """+str(bi_id)+""";
    bili_id NUMBER := """+str(bili_id)+""";
    bill_cust_id NUMBER := """+str(bill_cust_id)+""";
    ref_no NUMBER := """+str(edi_ref)+""";
    BEGIN
      LOOP
        IF l_counter >= """+str(count)+""" THEN
          EXIT;
        END IF;
        Insert into PCMP.BILL_INTERFACE (BI_ID,BI_CLAIM_NO,BI_BILL_NO,BI_EDI_REF_NO_PRI,BI_EDI_REF_NO_SECD,BI_CNV_NO,BI_EDI_SRC_TYP_CD,BI_PTCP_PAY_IND,BI_NOTE_IND,BI_OPN_DT,BI_COMP_DT,BI_REOPN_DT,BI_RECOMP_DT,BI_LST_TRAN_DT,BI_FRMT_TYP_CD,BI_SRC_TYP_CD,BI_MEDA_TYP_CD,BI_SERV_EFF_DT,BI_SERV_END_DT,BI_RECV_DT,BI_NOTE_ATTCH_IND,BI_FEE_SCH_OVRRD_IND,BI_FEE_SCH_OVRRD_RSN_TYP_CD,BI_FAST_TRK_ACTN_TYP_CD,BI_BFTART_CD,BI_CHR_TOT_AMT,BI_CST_CNTR_TYP_CD,BI_PAY_TYP_CD,BI_SUM_SBM_AMT,BI_SUM_APRV_AMT,BI_SUM_PD_AMT,BI_REF_NO,BI_MED_REC_NO,BI_ADMIT_DTM,BI_DISC_DTM,BI_LNGTH_OF_STAY_DD,BI_DRG_CD,BI_DRG_DESC,BI_DRG_VRFD_IND,BI_ADJ_DRG_CD,BI_ADJ_DRG_DESC,BI_ADJ_DRG_VRFD_IND,BI_UB92_TYP_CD,BI_UB92_TYP_DESC,BI_UB92_TYP_VRFD_IND,BI_ICD_SBM_ADMIT_CD,BI_ICD_SBM_ADMIT_DESC,BI_ICD_ADMIT_CD,BI_ICD_ADMIT_DESC,BI_ICD_ADMIT_VRFD_IND,BI_ICD_VER_CD,BI_PAY_REQS_ID,BI_STS_TYP_CD,BI_STS_EFF_DT,BI_STT_TYP_CD,BI_STS_STT_EFF_DT,BI_TRANS_RSN_TYP_CD,BI_STS_COMT,AUDIT_USER_ID_CREA,AUDIT_USER_CREA_DTM,AUDIT_USER_ID_UPDT,AUDIT_USER_UPDT_DTM,BI_PPY_TYP_CD,BI_PHY_LIC_NO,BI_ADMIS_TYP_CD,BI_SCH_TYP_CD,BI_OP_PHYS_LIC_NO,BI_SPL_PROC_TYP_CD,BI_SPL_PROC_AMT,BI_DO_NOT_RPT_IND,BI_DO_NOT_RPT_RSN_TYP_CD,BI_PRCS_DTM,BI_PAY_IND,BI_PAY_DTM,BI_NET_WK_SERV_IND) 
                values (l_counter,""" + \
                data.get('claim') + """,null ,ref_no,null,null,'brkst','n','n',
                  to_timestamp('""" + data.get(
            'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
            'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
            'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
            'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
            'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'cms1500','prov','edi',to_timestamp('""" + data.get(
            'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
            'end_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
            'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'n','n',null,'pay','reqsserv',""" + data.get(
            'total') + """,null,'med',""" + data.get('submitted') + """,""" + data.get(
            'approved') + """,0,null,null,null,null,null,null,null,null,null,null,null,null,null,null,'354.0',null,'354.0',null,'y','9',null,'rlse',to_timestamp('""" + data.get(
            'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'opn',to_timestamp('""" + data.get(
            'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'aprv',null,0,to_timestamp('""" + data.get(
            'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),null,null,null,null,null,null,null,null,null,null,null,null,null,null,'n');
           
        
        Insert into PCMP.BILL_INTERFACE_LINE_ITEM  (BILI_ID,BI_ID,BILI_EDI_REF_NO,BILI_SERV_EFF_DT,BILI_SERV_END_DT,BILI_TYP_CD,BILI_CD_TYP_CD_PRI,BILI_CST_CNTR_TYP_CD,BILI_PAY_TYP_CD,BILI_SBM_PRI_CD,BILI_SBM_PRI_DESC,BILI_PRI_CD,BILI_PRI_DESC,BILI_PRI_VRFD_IND,BILI_SUB_VRFD_IND,BILI_STR_TIME,BILI_END_TIME,BILI_UNT,BILI_MIN,BILI_CD_TYP_CD_SECD,BILI_SECD_CD,BILI_SECD_DESC,BILI_SECD_VRFD_IND,BILI_SERV_PLC_CD,BILI_SERV_PLC_DESC,BILI_SERV_PLC_VRFD_IND,BILI_SERV_TYP_CD,BILI_SERV_TYP_DESC,BILI_SERV_TYP_VRFD_IND,BILI_EMRG_TYP_CD,BILI_EMRG_TYP_DESC,BILI_EMRG_TYP_VRFD_IND,BILI_RX_NO,BILI_RX_SUPP_DD,BILI_RX_PROV_NM,BILI_RX_PROV_ID,BILI_PROV_ID_TYP_CD,BILI_RX_DT,BILI_TOOTH_CD,BILI_TOOTH_DESC,BILI_TOOTH_VRFD_IND,BILI_TOOTH_SRF_CD,BILI_TOOTH_SRF_DESC,BILI_TOOTH_SRF_VRFD_IND,BILI_TRVL_FR,BILI_TRVL_TO,BILI_TRVL_TYP_CD,BILI_TRVL_DST,BILI_TRVL_NET,BILI_TRVL_EXCL,BILI_TRVL_RT,BILI_TRVL_REMB,BILI_COMT,BILI_SBM_AMT,BILI_PAY_SBM_IND,BILI_APRV_AMT,BILI_PD_AMT,BILI_TAX_AMT,BILI_PENL_AMT,BILI_PRVS_PD_AMT,AUDIT_USER_ID_CREA,AUDIT_USER_CREA_DTM,AUDIT_USER_ID_UPDT,AUDIT_USER_UPDT_DTM,BILI_DISD_AS_WRTN_TYP_CD,BILI_NEW_REFL_TYP_CD,BILI_DME_OWNSHP_TYP_CD,BILI_OVRRD_FLG_IND,VOID_IND) 
            values (bili_id,l_counter,ref_no,to_timestamp('""" + data.get(
            'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
            'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'h','hcpc','021','med','99070','SPECIAL SUPPLIES','99070','SPECIAL SUPPLIES','y','n',to_timestamp('""" + data.get(
            'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
            'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),30,null,null,null,null,'n','11','OFFICE','y',null,null,'n','n',null,'y',null,null,null,null,null,null,null,null,'n',null,null,null,null,null,null,null,null,0,null,null,null,""" + data.get(
            'submitted') + """,'n',""" + data.get('approved') + """,null,null,null,null,0,to_timestamp('""" + data.get(
            'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),null,null,null,null,'p','n','n');
        
        Insert into PCMP.BILL_INTERFACE_CUSTOMER (BILL_INTFC_CUST_ID,BI_ID,BILL_INTFC_CUST_TYP_CD,BILL_INTFC_CUST_NM_FST,BILL_INTFC_CUST_NM_LST,BILL_INTFC_CUST_NM_MID,BILL_INTFC_CUST_PHN_NO,BILL_INTFC_CUST_PHN_EXT,BILL_INTFC_CUST_DOB,BILL_INTFC_CUST_GNDR_TYP_CD,BILL_INTFC_CUST_MAR_STS_TYP_CD,BILL_INTFC_CUST_TAX_ID_TYP_CD,BILL_INTFC_CUST_TAX_ID_NO,BILL_INTFC_CUST_ADDR_TYP_CD,BILL_INTFC_CUST_ADDR1,BILL_INTFC_CUST_ADDR2,BILL_INTFC_CUST_STT_ID,BILL_INTFC_CUST_CITY_NM,BILL_INTFC_CUST_POST_CD,BILL_INTFC_CUST_CNTRY_ID,BILL_INTFC_CUST_BILL_PROV_IND,BILL_INTFC_CUST_BILL_SERV_IND,BILL_INTFC_CUST_BILL_FACIL_IND,BILL_INTFC_CUST_NO,AUDIT_USER_ID_CREA,AUDIT_USER_CREA_DTM,AUDIT_USER_ID_UPDT,AUDIT_USER_UPDT_DTM,VOID_IND) 
            values (bill_cust_id,l_counter,'busn',null,'INDUSTRIAL PHARMACY MANAGEMENT LLC',null,null,null,null,null,null,'fein','100605677','mail','PO BOX 512518',null,2,'Los Angeles','90051',1,'y','n','n',""" + data.get(
            'customer') + """,0,to_timestamp('20-SEP-22 12.00.00.000000000 AM','DD-MON-RR HH.MI.SSXFF AM'),null,null,'n');
        
        l_counter := l_counter + 1;
        bili_id := bili_id + 1;
        bill_cust_id := bill_cust_id + 1;
        ref_no :=ref_no+1;
      END LOOP;
    
    END;
    """

    loop_edi = test.insert(query, connection);
    test.close(connection);
    result.append(loop_edi);
    return result


def generate_multiple_edi_eob(data, config):
    # print('Count: ',data.get('count'))
    connection = test.connect(config);
    bi_id = get_id('select max(bi_id) from pcmp.bill_interface', connection);
    edi_ref = get_id("select max(BI_EDI_REF_NO_PRI) from pcmp.bill_interface", connection);
    bili_id = get_id('select max(BILI_ID) from pcmp.BILL_INTERFACE_LINE_ITEM', connection);
    bill_cust_id = get_id('select max(BILL_INTFC_CUST_ID) from pcmp.BILL_INTERFACE_CUSTOMER', connection);
    bilie_id = get_id('select max(BILIE_ID) from pcmp.BILL_INTERFACE_LINE_ITEM_EOB', connection);
    result = []
    count = bi_id + int(data.get('count'));
    query = """DECLARE
    l_counter NUMBER := """ + str(bi_id) + """;
    bili_id NUMBER := """ + str(bili_id) + """;
    bill_cust_id NUMBER := """ + str(bill_cust_id) + """;
    bilie_id NUMBER := """ + str(bilie_id) + """;
    ref_no NUMBER := """ + str(edi_ref) + """;
    BEGIN
      LOOP
        IF l_counter >= """ + str(count) + """ THEN
          EXIT;
        END IF;
        Insert into PCMP.BILL_INTERFACE (BI_ID,BI_CLAIM_NO,BI_BILL_NO,BI_EDI_REF_NO_PRI,BI_EDI_REF_NO_SECD,BI_CNV_NO,BI_EDI_SRC_TYP_CD,BI_PTCP_PAY_IND,BI_NOTE_IND,BI_OPN_DT,BI_COMP_DT,BI_REOPN_DT,BI_RECOMP_DT,BI_LST_TRAN_DT,BI_FRMT_TYP_CD,BI_SRC_TYP_CD,BI_MEDA_TYP_CD,BI_SERV_EFF_DT,BI_SERV_END_DT,BI_RECV_DT,BI_NOTE_ATTCH_IND,BI_FEE_SCH_OVRRD_IND,BI_FEE_SCH_OVRRD_RSN_TYP_CD,BI_FAST_TRK_ACTN_TYP_CD,BI_BFTART_CD,BI_CHR_TOT_AMT,BI_CST_CNTR_TYP_CD,BI_PAY_TYP_CD,BI_SUM_SBM_AMT,BI_SUM_APRV_AMT,BI_SUM_PD_AMT,BI_REF_NO,BI_MED_REC_NO,BI_ADMIT_DTM,BI_DISC_DTM,BI_LNGTH_OF_STAY_DD,BI_DRG_CD,BI_DRG_DESC,BI_DRG_VRFD_IND,BI_ADJ_DRG_CD,BI_ADJ_DRG_DESC,BI_ADJ_DRG_VRFD_IND,BI_UB92_TYP_CD,BI_UB92_TYP_DESC,BI_UB92_TYP_VRFD_IND,BI_ICD_SBM_ADMIT_CD,BI_ICD_SBM_ADMIT_DESC,BI_ICD_ADMIT_CD,BI_ICD_ADMIT_DESC,BI_ICD_ADMIT_VRFD_IND,BI_ICD_VER_CD,BI_PAY_REQS_ID,BI_STS_TYP_CD,BI_STS_EFF_DT,BI_STT_TYP_CD,BI_STS_STT_EFF_DT,BI_TRANS_RSN_TYP_CD,BI_STS_COMT,AUDIT_USER_ID_CREA,AUDIT_USER_CREA_DTM,AUDIT_USER_ID_UPDT,AUDIT_USER_UPDT_DTM,BI_PPY_TYP_CD,BI_PHY_LIC_NO,BI_ADMIS_TYP_CD,BI_SCH_TYP_CD,BI_OP_PHYS_LIC_NO,BI_SPL_PROC_TYP_CD,BI_SPL_PROC_AMT,BI_DO_NOT_RPT_IND,BI_DO_NOT_RPT_RSN_TYP_CD,BI_PRCS_DTM,BI_PAY_IND,BI_PAY_DTM,BI_NET_WK_SERV_IND) 
                values (l_counter,""" + \
            data.get('claim') + """,null ,ref_no,null,null,'brkst','n','n',
                  to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'cms1500','prov','edi',to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'end_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'n','n',null,'pay','reqsserv',""" + data.get(
        'total') + """,null,'med',""" + data.get('submitted') + """,""" + data.get(
        'approved') + """,0,null,null,null,null,null,null,null,null,null,null,null,null,null,null,'354.0',null,'354.0',null,'y','9',null,'rlse',to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'opn',to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'aprv',null,0,to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),null,null,null,null,null,null,null,null,null,null,null,null,null,null,'n');


        Insert into PCMP.BILL_INTERFACE_LINE_ITEM  (BILI_ID,BI_ID,BILI_EDI_REF_NO,BILI_SERV_EFF_DT,BILI_SERV_END_DT,BILI_TYP_CD,BILI_CD_TYP_CD_PRI,BILI_CST_CNTR_TYP_CD,BILI_PAY_TYP_CD,BILI_SBM_PRI_CD,BILI_SBM_PRI_DESC,BILI_PRI_CD,BILI_PRI_DESC,BILI_PRI_VRFD_IND,BILI_SUB_VRFD_IND,BILI_STR_TIME,BILI_END_TIME,BILI_UNT,BILI_MIN,BILI_CD_TYP_CD_SECD,BILI_SECD_CD,BILI_SECD_DESC,BILI_SECD_VRFD_IND,BILI_SERV_PLC_CD,BILI_SERV_PLC_DESC,BILI_SERV_PLC_VRFD_IND,BILI_SERV_TYP_CD,BILI_SERV_TYP_DESC,BILI_SERV_TYP_VRFD_IND,BILI_EMRG_TYP_CD,BILI_EMRG_TYP_DESC,BILI_EMRG_TYP_VRFD_IND,BILI_RX_NO,BILI_RX_SUPP_DD,BILI_RX_PROV_NM,BILI_RX_PROV_ID,BILI_PROV_ID_TYP_CD,BILI_RX_DT,BILI_TOOTH_CD,BILI_TOOTH_DESC,BILI_TOOTH_VRFD_IND,BILI_TOOTH_SRF_CD,BILI_TOOTH_SRF_DESC,BILI_TOOTH_SRF_VRFD_IND,BILI_TRVL_FR,BILI_TRVL_TO,BILI_TRVL_TYP_CD,BILI_TRVL_DST,BILI_TRVL_NET,BILI_TRVL_EXCL,BILI_TRVL_RT,BILI_TRVL_REMB,BILI_COMT,BILI_SBM_AMT,BILI_PAY_SBM_IND,BILI_APRV_AMT,BILI_PD_AMT,BILI_TAX_AMT,BILI_PENL_AMT,BILI_PRVS_PD_AMT,AUDIT_USER_ID_CREA,AUDIT_USER_CREA_DTM,AUDIT_USER_ID_UPDT,AUDIT_USER_UPDT_DTM,BILI_DISD_AS_WRTN_TYP_CD,BILI_NEW_REFL_TYP_CD,BILI_DME_OWNSHP_TYP_CD,BILI_OVRRD_FLG_IND,VOID_IND) 
            values (bili_id,l_counter,ref_no,to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'h','hcpc','021','med','99070','SPECIAL SUPPLIES','99070','SPECIAL SUPPLIES','y','n',to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),30,null,null,null,null,'n','11','OFFICE','y',null,null,'n','n',null,'y',null,null,null,null,null,null,null,null,'n',null,null,null,null,null,null,null,null,0,null,null,null,""" + data.get(
        'submitted') + """,'n',""" + data.get('approved') + """,null,null,null,null,0,to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),null,null,null,null,'p','n','n');
        
        Insert into PCMP.BILL_INTERFACE_LINE_ITEM_EOB (BILIE_ID,BILI_ID,BILIE_GRP_TYP_CD,BILIE_CD,BILIE_DESC,BILIE_APLD_IND,BILIE_AMT,BILIE_APRV_AMT,BILIE_APRV_PCT,AUDIT_USER_ID_CREA,AUDIT_USER_CREA_DTM,AUDIT_USER_ID_UPDT,AUDIT_USER_UPDT_DTM,VOID_IND) 
	    values (bilie_id,bili_id,'misc','555','Refer to Brickstreet medical review system','y',""" + data.get('eob') + """,null,null,0,to_timestamp('""" + data.get( 'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),null,null,'n');

        Insert into PCMP.BILL_INTERFACE_CUSTOMER (BILL_INTFC_CUST_ID,BI_ID,BILL_INTFC_CUST_TYP_CD,BILL_INTFC_CUST_NM_FST,BILL_INTFC_CUST_NM_LST,BILL_INTFC_CUST_NM_MID,BILL_INTFC_CUST_PHN_NO,BILL_INTFC_CUST_PHN_EXT,BILL_INTFC_CUST_DOB,BILL_INTFC_CUST_GNDR_TYP_CD,BILL_INTFC_CUST_MAR_STS_TYP_CD,BILL_INTFC_CUST_TAX_ID_TYP_CD,BILL_INTFC_CUST_TAX_ID_NO,BILL_INTFC_CUST_ADDR_TYP_CD,BILL_INTFC_CUST_ADDR1,BILL_INTFC_CUST_ADDR2,BILL_INTFC_CUST_STT_ID,BILL_INTFC_CUST_CITY_NM,BILL_INTFC_CUST_POST_CD,BILL_INTFC_CUST_CNTRY_ID,BILL_INTFC_CUST_BILL_PROV_IND,BILL_INTFC_CUST_BILL_SERV_IND,BILL_INTFC_CUST_BILL_FACIL_IND,BILL_INTFC_CUST_NO,AUDIT_USER_ID_CREA,AUDIT_USER_CREA_DTM,AUDIT_USER_ID_UPDT,AUDIT_USER_UPDT_DTM,VOID_IND) 
            values (bill_cust_id,l_counter,'busn',null,'INDUSTRIAL PHARMACY MANAGEMENT LLC',null,null,null,null,null,null,'fein','100605677','mail','PO BOX 512518',null,2,'Los Angeles','90051',1,'y','n','n',""" + data.get(
        'customer') + """,0,to_timestamp('20-SEP-22 12.00.00.000000000 AM','DD-MON-RR HH.MI.SSXFF AM'),null,null,'n');

        l_counter := l_counter + 1;
        bili_id := bili_id + 1;
        bill_cust_id := bill_cust_id + 1;
        bilie_id := bilie_id + 1;
        ref_no :=ref_no+1;
      END LOOP;

    END;
    """

    #print(query)
    loop_edi_eob = test.insert(query, connection);
    test.close(connection);
    result.append(loop_edi_eob);
    return result


def generate_multiple_line_item(data, config):
    # print('Count: ',data.get('count'))
    bi_id_query = '';
    edi_ref_query = '';
    bili_id_query = '';
    bill_cust_id_query = '';
    bill_interface_query = '';
    query_set = models.Query_set.objects.all();
    for query in query_set:
        if query.table_name == 'bi_id':
            bi_id_query = query.query;
        elif query.table_name == 'edi_ref':
            edi_ref_query = query.query;
        elif query.table_name == 'bili_id':
            bili_id_query = query.query;
        elif query.table_name == 'bill_cust_id':
            bill_cust_id_query = query.query;
    connection = test.connect(config);
    bi_id = get_id(bi_id_query, connection);
    edi_ref = get_id(edi_ref_query, connection);
    bili_id = get_id(bili_id_query, connection);
    bill_cust_id = get_id(bill_cust_id_query, connection);
    result = []
    count = bi_id + int(data.get('count'));
    bill_interface = """Insert into PCMP.BILL_INTERFACE (BI_ID,BI_CLAIM_NO,BI_BILL_NO,BI_EDI_REF_NO_PRI,BI_EDI_REF_NO_SECD,BI_CNV_NO,BI_EDI_SRC_TYP_CD,BI_PTCP_PAY_IND,BI_NOTE_IND,BI_OPN_DT,BI_COMP_DT,BI_REOPN_DT,BI_RECOMP_DT,BI_LST_TRAN_DT,BI_FRMT_TYP_CD,BI_SRC_TYP_CD,BI_MEDA_TYP_CD,BI_SERV_EFF_DT,BI_SERV_END_DT,BI_RECV_DT,BI_NOTE_ATTCH_IND,BI_FEE_SCH_OVRRD_IND,BI_FEE_SCH_OVRRD_RSN_TYP_CD,BI_FAST_TRK_ACTN_TYP_CD,BI_BFTART_CD,BI_CHR_TOT_AMT,BI_CST_CNTR_TYP_CD,BI_PAY_TYP_CD,BI_SUM_SBM_AMT,BI_SUM_APRV_AMT,BI_SUM_PD_AMT,BI_REF_NO,BI_MED_REC_NO,BI_ADMIT_DTM,BI_DISC_DTM,BI_LNGTH_OF_STAY_DD,BI_DRG_CD,BI_DRG_DESC,BI_DRG_VRFD_IND,BI_ADJ_DRG_CD,BI_ADJ_DRG_DESC,BI_ADJ_DRG_VRFD_IND,BI_UB92_TYP_CD,BI_UB92_TYP_DESC,BI_UB92_TYP_VRFD_IND,BI_ICD_SBM_ADMIT_CD,BI_ICD_SBM_ADMIT_DESC,BI_ICD_ADMIT_CD,BI_ICD_ADMIT_DESC,BI_ICD_ADMIT_VRFD_IND,BI_ICD_VER_CD,BI_PAY_REQS_ID,BI_STS_TYP_CD,BI_STS_EFF_DT,BI_STT_TYP_CD,BI_STS_STT_EFF_DT,BI_TRANS_RSN_TYP_CD,BI_STS_COMT,AUDIT_USER_ID_CREA,AUDIT_USER_CREA_DTM,AUDIT_USER_ID_UPDT,AUDIT_USER_UPDT_DTM,BI_PPY_TYP_CD,BI_PHY_LIC_NO,BI_ADMIS_TYP_CD,BI_SCH_TYP_CD,BI_OP_PHYS_LIC_NO,BI_SPL_PROC_TYP_CD,BI_SPL_PROC_AMT,BI_DO_NOT_RPT_IND,BI_DO_NOT_RPT_RSN_TYP_CD,BI_PRCS_DTM,BI_PAY_IND,BI_PAY_DTM,BI_NET_WK_SERV_IND) 
                values (""" + str(bi_id) + """,""" + data.get('claim') + """,null ,""" + str(edi_ref) + """,null,null,'brkst','n','n',
                  to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'cms1500','prov','edi',to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'end_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'n','n',null,'pay','reqsserv',""" + data.get(
        'total') + """,null,'med',""" + data.get('submitted') + """,""" + data.get(
        'approved') + """,0,null,null,null,null,null,null,null,null,null,null,null,null,null,null,'354.0',null,'354.0',null,'y','9',null,'rlse',to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'opn',to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'aprv',null,0,to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),null,null,null,null,null,null,null,null,null,null,null,null,null,null,'n')
            """

    customer = """  Insert into PCMP.BILL_INTERFACE_CUSTOMER (BILL_INTFC_CUST_ID,BI_ID,BILL_INTFC_CUST_TYP_CD,BILL_INTFC_CUST_NM_FST,BILL_INTFC_CUST_NM_LST,BILL_INTFC_CUST_NM_MID,BILL_INTFC_CUST_PHN_NO,BILL_INTFC_CUST_PHN_EXT,BILL_INTFC_CUST_DOB,BILL_INTFC_CUST_GNDR_TYP_CD,BILL_INTFC_CUST_MAR_STS_TYP_CD,BILL_INTFC_CUST_TAX_ID_TYP_CD,BILL_INTFC_CUST_TAX_ID_NO,BILL_INTFC_CUST_ADDR_TYP_CD,BILL_INTFC_CUST_ADDR1,BILL_INTFC_CUST_ADDR2,BILL_INTFC_CUST_STT_ID,BILL_INTFC_CUST_CITY_NM,BILL_INTFC_CUST_POST_CD,BILL_INTFC_CUST_CNTRY_ID,BILL_INTFC_CUST_BILL_PROV_IND,BILL_INTFC_CUST_BILL_SERV_IND,BILL_INTFC_CUST_BILL_FACIL_IND,BILL_INTFC_CUST_NO,AUDIT_USER_ID_CREA,AUDIT_USER_CREA_DTM,AUDIT_USER_ID_UPDT,AUDIT_USER_UPDT_DTM,VOID_IND) 
            values (""" + str(bill_cust_id) + """,""" + str(
        bi_id) + """,'busn',null,'INDUSTRIAL PHARMACY MANAGEMENT LLC',null,null,null,null,null,null,'fein','100605677','mail','PO BOX 512518',null,2,'Los Angeles','90051',1,'y','n','n',""" + data.get(
        'customer') + """,0,to_timestamp('20-SEP-22 12.00.00.000000000 AM','DD-MON-RR HH.MI.SSXFF AM'),null,null,'n')
         """

    submitted_amount=int(data.get('submitted'))/int(data.get('count'));
    approved_amount = int(data.get('approved')) / int(data.get('count'));
    query = """DECLARE
      l_counter NUMBER := """ + str(bili_id) + """;
    BEGIN
      LOOP
        IF l_counter >= """ + str(count) + """ THEN
          EXIT;
        END IF;
            Insert into PCMP.BILL_INTERFACE_LINE_ITEM  (BILI_ID,BI_ID,BILI_EDI_REF_NO,BILI_SERV_EFF_DT,BILI_SERV_END_DT,BILI_TYP_CD,BILI_CD_TYP_CD_PRI,BILI_CST_CNTR_TYP_CD,BILI_PAY_TYP_CD,BILI_SBM_PRI_CD,BILI_SBM_PRI_DESC,BILI_PRI_CD,BILI_PRI_DESC,BILI_PRI_VRFD_IND,BILI_SUB_VRFD_IND,BILI_STR_TIME,BILI_END_TIME,BILI_UNT,BILI_MIN,BILI_CD_TYP_CD_SECD,BILI_SECD_CD,BILI_SECD_DESC,BILI_SECD_VRFD_IND,BILI_SERV_PLC_CD,BILI_SERV_PLC_DESC,BILI_SERV_PLC_VRFD_IND,BILI_SERV_TYP_CD,BILI_SERV_TYP_DESC,BILI_SERV_TYP_VRFD_IND,BILI_EMRG_TYP_CD,BILI_EMRG_TYP_DESC,BILI_EMRG_TYP_VRFD_IND,BILI_RX_NO,BILI_RX_SUPP_DD,BILI_RX_PROV_NM,BILI_RX_PROV_ID,BILI_PROV_ID_TYP_CD,BILI_RX_DT,BILI_TOOTH_CD,BILI_TOOTH_DESC,BILI_TOOTH_VRFD_IND,BILI_TOOTH_SRF_CD,BILI_TOOTH_SRF_DESC,BILI_TOOTH_SRF_VRFD_IND,BILI_TRVL_FR,BILI_TRVL_TO,BILI_TRVL_TYP_CD,BILI_TRVL_DST,BILI_TRVL_NET,BILI_TRVL_EXCL,BILI_TRVL_RT,BILI_TRVL_REMB,BILI_COMT,BILI_SBM_AMT,BILI_PAY_SBM_IND,BILI_APRV_AMT,BILI_PD_AMT,BILI_TAX_AMT,BILI_PENL_AMT,BILI_PRVS_PD_AMT,AUDIT_USER_ID_CREA,AUDIT_USER_CREA_DTM,AUDIT_USER_ID_UPDT,AUDIT_USER_UPDT_DTM,BILI_DISD_AS_WRTN_TYP_CD,BILI_NEW_REFL_TYP_CD,BILI_DME_OWNSHP_TYP_CD,BILI_OVRRD_FLG_IND,VOID_IND) 
            values (l_counter,""" + str(bi_id) + """,""" + str(edi_ref) + """,to_timestamp('""" + data.get(
            'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
            'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'h','hcpc','021','med','99070','SPECIAL SUPPLIES','99070','SPECIAL SUPPLIES','y','n',to_timestamp('""" + data.get(
            'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
            'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),30,null,null,null,null,'n','11','OFFICE','y',null,null,'n','n',null,'y',null,null,null,null,null,null,null,null,'n',null,null,null,null,null,null,null,null,0,null,null,
            null,""" + str(submitted_amount) + """,'n',""" + str(approved_amount) + """,null,null,null,null,0,to_timestamp('""" + data.get(
            'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),null,null,null,null,'p','n','n');
            
            l_counter := l_counter + 1;
            
      END LOOP;
    
    END;
    """
    loop_line_item='Error';
    bill_interface_result = test.insert(bill_interface, connection);
    if "successfully" in bill_interface_result:
        customer_result = test.insert(customer, connection);
        loop_line_item = test.insert(query, connection);
    test.close(connection);
    result.append(loop_line_item);
    result.append(bi_id);
    return result


def generate_multiple_line_item_eob(data, config):
    # print('Count: ',data.get('count'))
    bi_id_query = '';
    edi_ref_query = '';
    bili_id_query = '';
    bill_cust_id_query = '';
    bilie_id_query='';
    query_set = models.Query_set.objects.all();
    for query in query_set:
        if query.table_name == 'bi_id':
            bi_id_query = query.query;
        elif query.table_name == 'edi_ref':
            edi_ref_query = query.query;
        elif query.table_name == 'bili_id':
            bili_id_query = query.query;
        elif query.table_name == 'bill_cust_id':
            bill_cust_id_query = query.query;
        elif query.table_name == 'bilie_id':
            bilie_id_query = query.query;
    connection = test.connect(config);
    bi_id = get_id(bi_id_query, connection);
    edi_ref = get_id(edi_ref_query, connection);
    bili_id = get_id(bili_id_query, connection);
    bill_cust_id = get_id(bill_cust_id_query, connection);
    bilie_id=get_id(bilie_id_query, connection);
    result = []
    count = bili_id + int(data.get('count'));
    bill_interface = """Insert into PCMP.BILL_INTERFACE (BI_ID,BI_CLAIM_NO,BI_BILL_NO,BI_EDI_REF_NO_PRI,BI_EDI_REF_NO_SECD,BI_CNV_NO,BI_EDI_SRC_TYP_CD,BI_PTCP_PAY_IND,BI_NOTE_IND,BI_OPN_DT,BI_COMP_DT,BI_REOPN_DT,BI_RECOMP_DT,BI_LST_TRAN_DT,BI_FRMT_TYP_CD,BI_SRC_TYP_CD,BI_MEDA_TYP_CD,BI_SERV_EFF_DT,BI_SERV_END_DT,BI_RECV_DT,BI_NOTE_ATTCH_IND,BI_FEE_SCH_OVRRD_IND,BI_FEE_SCH_OVRRD_RSN_TYP_CD,BI_FAST_TRK_ACTN_TYP_CD,BI_BFTART_CD,BI_CHR_TOT_AMT,BI_CST_CNTR_TYP_CD,BI_PAY_TYP_CD,BI_SUM_SBM_AMT,BI_SUM_APRV_AMT,BI_SUM_PD_AMT,BI_REF_NO,BI_MED_REC_NO,BI_ADMIT_DTM,BI_DISC_DTM,BI_LNGTH_OF_STAY_DD,BI_DRG_CD,BI_DRG_DESC,BI_DRG_VRFD_IND,BI_ADJ_DRG_CD,BI_ADJ_DRG_DESC,BI_ADJ_DRG_VRFD_IND,BI_UB92_TYP_CD,BI_UB92_TYP_DESC,BI_UB92_TYP_VRFD_IND,BI_ICD_SBM_ADMIT_CD,BI_ICD_SBM_ADMIT_DESC,BI_ICD_ADMIT_CD,BI_ICD_ADMIT_DESC,BI_ICD_ADMIT_VRFD_IND,BI_ICD_VER_CD,BI_PAY_REQS_ID,BI_STS_TYP_CD,BI_STS_EFF_DT,BI_STT_TYP_CD,BI_STS_STT_EFF_DT,BI_TRANS_RSN_TYP_CD,BI_STS_COMT,AUDIT_USER_ID_CREA,AUDIT_USER_CREA_DTM,AUDIT_USER_ID_UPDT,AUDIT_USER_UPDT_DTM,BI_PPY_TYP_CD,BI_PHY_LIC_NO,BI_ADMIS_TYP_CD,BI_SCH_TYP_CD,BI_OP_PHYS_LIC_NO,BI_SPL_PROC_TYP_CD,BI_SPL_PROC_AMT,BI_DO_NOT_RPT_IND,BI_DO_NOT_RPT_RSN_TYP_CD,BI_PRCS_DTM,BI_PAY_IND,BI_PAY_DTM,BI_NET_WK_SERV_IND) 
                values (""" + str(bi_id) + """,""" + data.get('claim') + """,null ,""" + str(edi_ref) + """,null,null,'brkst','n','n',
                  to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'cms1500','prov','edi',to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'end_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'n','n',null,'pay','reqsserv',""" + data.get(
        'total') + """,null,'med',""" + data.get('submitted') + """,""" + data.get(
        'approved') + """,0,null,null,null,null,null,null,null,null,null,null,null,null,null,null,'354.0',null,'354.0',null,'y','9',null,'rlse',to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'opn',to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'aprv',null,0,to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),null,null,null,null,null,null,null,null,null,null,null,null,null,null,'n')
            """

    customer = """  Insert into PCMP.BILL_INTERFACE_CUSTOMER (BILL_INTFC_CUST_ID,BI_ID,BILL_INTFC_CUST_TYP_CD,BILL_INTFC_CUST_NM_FST,BILL_INTFC_CUST_NM_LST,BILL_INTFC_CUST_NM_MID,BILL_INTFC_CUST_PHN_NO,BILL_INTFC_CUST_PHN_EXT,BILL_INTFC_CUST_DOB,BILL_INTFC_CUST_GNDR_TYP_CD,BILL_INTFC_CUST_MAR_STS_TYP_CD,BILL_INTFC_CUST_TAX_ID_TYP_CD,BILL_INTFC_CUST_TAX_ID_NO,BILL_INTFC_CUST_ADDR_TYP_CD,BILL_INTFC_CUST_ADDR1,BILL_INTFC_CUST_ADDR2,BILL_INTFC_CUST_STT_ID,BILL_INTFC_CUST_CITY_NM,BILL_INTFC_CUST_POST_CD,BILL_INTFC_CUST_CNTRY_ID,BILL_INTFC_CUST_BILL_PROV_IND,BILL_INTFC_CUST_BILL_SERV_IND,BILL_INTFC_CUST_BILL_FACIL_IND,BILL_INTFC_CUST_NO,AUDIT_USER_ID_CREA,AUDIT_USER_CREA_DTM,AUDIT_USER_ID_UPDT,AUDIT_USER_UPDT_DTM,VOID_IND) 
            values (""" + str(bill_cust_id) + """,""" + str(
        bi_id) + """,'busn',null,'INDUSTRIAL PHARMACY MANAGEMENT LLC',null,null,null,null,null,null,'fein','100605677','mail','PO BOX 512518',null,2,'Los Angeles','90051',1,'y','n','n',""" + data.get(
        'customer') + """,0,to_timestamp('20-SEP-22 12.00.00.000000000 AM','DD-MON-RR HH.MI.SSXFF AM'),null,null,'n')
         """

    submitted_amount = int(data.get('submitted')) / int(data.get('count'));
    approved_amount = int(data.get('approved')) / int(data.get('count'));
    eob_amount=submitted_amount-approved_amount;
    per_eob=eob_amount/5;
    eob_count = bilie_id + (int(data.get('count'))*5);
    query = """DECLARE
      l_counter NUMBER := """ + str(bili_id) + """;
    BEGIN
      LOOP
        IF l_counter >= """ + str(count) + """ THEN
          EXIT;
        END IF;
            Insert into PCMP.BILL_INTERFACE_LINE_ITEM  (BILI_ID,BI_ID,BILI_EDI_REF_NO,BILI_SERV_EFF_DT,BILI_SERV_END_DT,BILI_TYP_CD,BILI_CD_TYP_CD_PRI,BILI_CST_CNTR_TYP_CD,BILI_PAY_TYP_CD,BILI_SBM_PRI_CD,BILI_SBM_PRI_DESC,BILI_PRI_CD,BILI_PRI_DESC,BILI_PRI_VRFD_IND,BILI_SUB_VRFD_IND,BILI_STR_TIME,BILI_END_TIME,BILI_UNT,BILI_MIN,BILI_CD_TYP_CD_SECD,BILI_SECD_CD,BILI_SECD_DESC,BILI_SECD_VRFD_IND,BILI_SERV_PLC_CD,BILI_SERV_PLC_DESC,BILI_SERV_PLC_VRFD_IND,BILI_SERV_TYP_CD,BILI_SERV_TYP_DESC,BILI_SERV_TYP_VRFD_IND,BILI_EMRG_TYP_CD,BILI_EMRG_TYP_DESC,BILI_EMRG_TYP_VRFD_IND,BILI_RX_NO,BILI_RX_SUPP_DD,BILI_RX_PROV_NM,BILI_RX_PROV_ID,BILI_PROV_ID_TYP_CD,BILI_RX_DT,BILI_TOOTH_CD,BILI_TOOTH_DESC,BILI_TOOTH_VRFD_IND,BILI_TOOTH_SRF_CD,BILI_TOOTH_SRF_DESC,BILI_TOOTH_SRF_VRFD_IND,BILI_TRVL_FR,BILI_TRVL_TO,BILI_TRVL_TYP_CD,BILI_TRVL_DST,BILI_TRVL_NET,BILI_TRVL_EXCL,BILI_TRVL_RT,BILI_TRVL_REMB,BILI_COMT,BILI_SBM_AMT,BILI_PAY_SBM_IND,BILI_APRV_AMT,BILI_PD_AMT,BILI_TAX_AMT,BILI_PENL_AMT,BILI_PRVS_PD_AMT,AUDIT_USER_ID_CREA,AUDIT_USER_CREA_DTM,AUDIT_USER_ID_UPDT,AUDIT_USER_UPDT_DTM,BILI_DISD_AS_WRTN_TYP_CD,BILI_NEW_REFL_TYP_CD,BILI_DME_OWNSHP_TYP_CD,BILI_OVRRD_FLG_IND,VOID_IND) 
            values (l_counter,""" + str(bi_id) + """,""" + str(edi_ref) + """,to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),'h','hcpc','021','med','99070','SPECIAL SUPPLIES','99070','SPECIAL SUPPLIES','y','n',to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),30,null,null,null,null,'n','11','OFFICE','y',null,null,'n','n',null,'y',null,null,null,null,null,null,null,null,'n',null,null,null,null,null,null,null,null,0,null,null,
            null,""" + str(submitted_amount) + """,'n',""" + str(
        approved_amount) + """,null,null,null,null,0,to_timestamp('""" + data.get(
        'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),null,null,null,null,'p','n','n');
        l_counter := l_counter + 1;
      END LOOP;

    END;
    """

    eob="""DECLARE
      l_counter NUMBER := """ + str(bilie_id) + """;
      line_item NUMBER := """ + str(bili_id) + """;
    BEGIN
      LOOP
        IF l_counter >= """ + str(eob_count) + """ THEN
          EXIT;
        END IF;
        Insert into PCMP.BILL_INTERFACE_LINE_ITEM_EOB (BILIE_ID,BILI_ID,BILIE_GRP_TYP_CD,BILIE_CD,BILIE_DESC,BILIE_APLD_IND,BILIE_AMT,BILIE_APRV_AMT,BILIE_APRV_PCT,AUDIT_USER_ID_CREA,AUDIT_USER_CREA_DTM,AUDIT_USER_ID_UPDT,AUDIT_USER_UPDT_DTM,VOID_IND) 
        values (l_counter,line_item,'misc','555','Refer to Brickstreet medical review system','y',""" + str(per_eob) + """,null,null,0,to_timestamp('""" + data.get( 'start_date') + """ 12.00.00.000000000 AM','YYYY-MM-DD HH.MI.SSXFF AM'),null,null,'n');
        IF MOD(l_counter,5)=0 THEN
            line_item := line_item+1;
        END IF;
        l_counter := l_counter + 1;
      END LOOP;
    
    END;
    """
    loop_line_item = 'Error';
    #print(query);
    #print(eob);
    bill_interface_result = test.insert(bill_interface, connection);
    if "successfully" in bill_interface_result:
        customer_result = test.insert(customer, connection);
        loop_line_item = test.insert(query, connection);
        loop_eob=test.insert(eob, connection);
    test.close(connection);
    result.append(loop_line_item);
    result.append(bi_id);
    return result
