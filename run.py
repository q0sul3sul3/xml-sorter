from collections import OrderedDict

import xmltodict


def sort_xml(xml_file_path):
    with open(xml_file_path, 'r') as xml_file:
        xml_data = xml_file.read()

    data = xmltodict.parse(xml_data, dict_constructor=OrderedDict)

    sorted_recs = sorted(data['RECS']['REC'], key=lambda x: x['MB']['MB1']['M03'])
    for rec in sorted_recs:
        if 'MB2' in rec['MB'] and isinstance(rec['MB']['MB2'], list):
            rec['MB']['MB2'] = sorted(rec['MB']['MB2'], key=lambda x: x['D06'])

    sorted_dict = OrderedDict()
    sorted_dict['RECS'] = OrderedDict()
    sorted_dict['RECS']['REC'] = sorted_recs

    sorted_file_path = xml_file_path.replace('.xml', '_sorted.xml')
    with open(sorted_file_path, 'w', encoding='Big5') as sorted_xml_file:
        sorted_xml_file.write(
            xmltodict.unparse(sorted_dict, pretty=True, encoding='Big5')
        )


if __name__ == '__main__':
    xml_file_path = 'data.xml'
    sort_xml(xml_file_path)
