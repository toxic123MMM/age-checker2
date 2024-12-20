from datetime import date
def age(db):
    today=date.today()
    a=today.year-db.year-((today.month,today.day)<(db.month,db.day))
    return a
print(age(date(2000,2,3)))