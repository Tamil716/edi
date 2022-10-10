from py_scripts import query


data= {'env': 'base_tech6', 'bi_id': 1000, 'edi_ref': 3944000480, 'claim': '1000', 'customer': '1000001', 'start_date': '2022-09-28', 'end_date': '2022-09-28', 'total': '1000', 'submitted': '1000', 'approved': '1000'}
query.generate_query(data)