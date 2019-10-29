import sqlalchemy
from sqlalchemy import create_engine
engine=create_engine("postgresql://postgres:0908#Gourd@localhost/vacregister",echo=True)
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()
#from sqlalchemy import Column,Integer,String,Date,Numeric
#from sqlalchemy.orm import sessionmaker

#Session=sessionmaker(bind=engine)
#session=Session()

#from sqlalchemy import ForeignKey
#from sqlalchemy.orm import relationship

#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()

#Base.metadata.create_all(engine)


from sqlalchemy import create_engine

engine=create_engine("postgresql://postgres:0908#Gourd@localhost/vacregister",echo=True)

db.Model.metadata.create_all(engine)


@app.route('/a')
def a():
    session['my_var'] = 'my_value'
    return redirect(url_for('b'))

@app.route('/b')
def b():
    my_var = session.get('my_var', None)
    return my_var