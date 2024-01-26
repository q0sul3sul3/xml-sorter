from collections import OrderedDict

import xmltodict

with open('data.xml', 'r') as xml_file:
    xml_data = xml_file.read()

data = xmltodict.parse(xml_data, dict_constructor=OrderedDict)

sorted_recs = sorted(data['RECS']['REC'], key=lambda x: x['MB']['MB1']['M03'])
for rec in sorted_recs:
    if 'MB2' in rec['MB'] and isinstance(rec['MB']['MB2'], list):
        rec['MB']['MB2'] = sorted(rec['MB']['MB2'], key=lambda x: x['D06'])

sorted_dict = OrderedDict()
sorted_dict['RECS'] = OrderedDict()
sorted_dict['RECS']['REC'] = sorted_recs

with open('data_sorted.xml', 'w', encoding='Big5') as sorted_xml_file:
    sorted_xml_file.write(xmltodict.unparse(sorted_dict, pretty=True, encoding='Big5'))
