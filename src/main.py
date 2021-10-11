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
    items = HHparser.get_items(page, keyword)
    for item in items:
        vacancy = {}
        HHparser.set_fields(vacancy, main_fields, item)
        HHparser.set_subfields(vacancy, opt_fields, opt_subfields, item)
        HHparser.set_subfields(vacancy, add_fields, add_subfields, item)
        HHparser.set_subfields(vacancy, sal_fields, sal_subfields, item)
        vacancy['description'] = HHparser.get_description(item['id'])
        HHdatabase.add_vacancy(db, vacancy)
        print('vacancy id:', vacancy['id'])