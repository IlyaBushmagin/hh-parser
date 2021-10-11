import HHdatabase
import HHparser

db = 'hh.db'
keyword = 'Python программист'

main_fields = ['id', 'name', 'published_at', 'archived']

opt_fields = ['area', 'type', 'employer', 'schedule']
opt_subfields = ['id', 'name']

add_fields = ['address']
add_subfields = ['id', 'raw']

sal_fields = ['salary']
sal_subfields = ['from', 'to', 'currency', 'gross']

found, pages = HHparser.get_meta(keyword)
print('found:', found, 'pages:', pages)

HHdatabase.create_db(db)

for page in range(pages):
    items = HHparser.get_items(page, keyword)
    for item in items:
        vacancy = {}
        vacancy.update(HHparser.get_fields(main_fields, item))
        vacancy.update(HHparser.get_subfields(opt_fields, opt_subfields, item))
        vacancy.update(HHparser.get_subfields(add_fields, add_subfields, item))
        vacancy.update(HHparser.get_subfields(sal_fields, sal_subfields, item))
        vacancy.update(HHparser.get_description(item['id']))
        HHdatabase.add_vacancy(db, vacancy)
        print('vacancy id:', vacancy['id'])