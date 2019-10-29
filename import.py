import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#engine = create_engine('postgresql://vacadmin:admin@localhost/vacregister')
engine = create_engine("postgresql://postgres:0908#Gourd@localhost/vacregister")

db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("countries.csv")
    reader = csv.reader(f)
    for iso3, countryname, who_region in reader:
        db.execute("INSERT INTO countries (iso3, countryname, who_region) VALUES (:iso3, :countryname, :who_region)",
                    {"iso3": iso3, "countryname": countryname, "who_region": who_region})
    db.commit()

if __name__ == "__main__":
    main()
