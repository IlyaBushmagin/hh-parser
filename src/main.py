import HHdatabase
import HHparser

db = 'hh.db'
keyword = 'Python программист'

main_fields = ['id', 'name', 'published_at', 'archived']
opt_fields = ['area', 'type', 'employer', 'schedule']
add_fields = ['address']
sal_fields = ['salary']
opt_subfields = ['id', 'name']
add_subfields = ['id', 'raw']
sal_subfields = ['from', 'to', 'currency', 'gross']

found, pages = HHparser.get_meta(keyword)
print('found:', found, 'pages:', pages)

HHdatabase.create_db(db)

for page in range(pages):
    data = HHparser.get_data(page, keyword)
    items = len(data)
    for item in range(items):
        vacancy = {}
        HHparser.get_fields(vacancy, main_fields, data[item])
        HHparser.get_fields_with_subs(vacancy, opt_fields, opt_subfields, data[item])
        HHparser.get_fields_with_subs(vacancy, add_fields, add_subfields, data[item])
        HHparser.get_fields_with_subs(vacancy, sal_fields, sal_subfields, data[item])
        vacancy['description'] = HHparser.get_description(data[item]['id'])
        HHdatabase.add_vacancy(db, vacancy)
        print('vacancy id:', vacancy['id'])