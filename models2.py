from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Country(db.Model):
    __tablename__ = "countries"
    iso3 = db.Column(db.String(3), primary_key=True)
    countryname=db.Column(db.String)
    who_region = db.Column(db.String)
    unicef_region = db.Column(db.String)

class Intervention(db.Model):
    __tablename__ = "interventions"
    id=db.Column(db.Integer,primary_key=True)
    intervention_name=db.Column(db.String)
    intervention_code=db.Column(db.String)
class Activity(db.Model):
    __tablename__="activity"
    id=db.Column(db.Integer,primary_key=True)
    iso3=db.Column(db.String(3),db.ForeignKey("countries.iso3"))
    phased=db.Column(db.Integer)
    phase_total=db.Column(db.Integer)
    comment=db.Column(db.String(1000))
    status=db.Column(db.String(50))

class Phase(db.Model)
    __tablename__="phase"
    id=db.Column(db.Integer,primary_key=True)
    activity_id=db.Column(db.Integer,db.ForeignKey("activity.id"))
    start_date=db.Column(db.Date)
    end_date=db.Column(db.Date)

class Geography(db.Model)
    __tablename__='geography'
    id=db.Column(db.Integer,primary_key=True)
    phase_id=db.Column(db.Integer,db.ForeignKey("phase.id"),nullable=False)
    geo_parent_id=db.Column(db.Integer)
    start_date=db.Column(db.Date)
    end_date=db.Column(db.Date)
    intervention_id=db.Column(db.Integer,db.ForeignKey("interventions.id"))
    area=db.Column(db.String(50))
    target_age_group=db.Column(db.String(20))
    #target_pop_discription=db.Column(db.String(100))
    #target_age_start=db.Column(db.Integer)
    #target_age_start_unit=db.Column(db.String(10))
    #target_age_end=db.Column(db.Integer)
    #target_age_end_unit=db.Column(db.String(10))
    target_population=db.Column(db.Integer)
    target_population_reached=db.Column(db.Integer)
    percent_reached=db.Column(db.Numeric(3,2))
    number_district_over95=db.Column(db.Integer)
    percent_district_over95=db.Column(db.Numeric(3,2))
    survey_done=db.Column(db.Boolean)
    survey_coverage=db.Column(db.Numeric(3,2))
    wastage_rate=db.Column(db.Numeric(3,2))
    number_AEFI=db.Column(db.Integer)
    number_AEFI_by_SIA=db.Column(db.Integer)
    

class SIASum(db.Model):
    __tablename__ ="siasum"
    id=db.Column(db.Integer,primary_key=True)
    iso3=db.Column(db.String(3),db.ForeignKey("countries.iso3"))
    start_date=db.Column(db.Date)
    end_date=db.Column(db.Date)
    status=db.Column(db.String(50))
    sia_type=db.Column(db.Integer)
    source=db.Column(db.String(500))
    comment=db.Column(db.String(500))
    details=db.relationship("SIADetail",backref='siasum')

    def addDetail(self,intervention_id):
        detail=SIADetail(intervention_id=intervention_id,siasum_id=self.id)
        db.session.add(detail)
        db.session.commit()


class SIADetail(db.Model):
    __tablename__='siadetail'
    id=db.Column(db.Integer,primary_key=True)
    siasum_id=db.Column(db.Integer,db.ForeignKey("siasum.id"),nullable=False)
    parent_id=db.Column(db.Integer)
    start_date=db.Column(db.Date)
    end_date=db.Column(db.Date)
    intervention_id=db.Column(db.Integer,db.ForeignKey("interventions.id"))
    #area=db.Column(db.String(50))
    target_age_group=db.Column(db.String(20))
    target_pop_discription=db.Column(db.String(100))
    target_age_start=db.Column(db.Integer)
    target_age_start_unit=db.Column(db.String(10))
    target_age_end=db.Column(db.Integer)
    target_age_end_unit=db.Column(db.String(10))
    target_population=db.Column(db.Integer)
    target_population_reached=db.Column(db.Integer)
    percent_reached=db.Column(db.Numeric(3,2))
    number_district_over95=db.Column(db.Integer)
    percent_district_over95=db.Column(db.Numeric(3,2))
    survey_done=db.Column(db.Boolean)
    survey_coverage=db.Column(db.Numeric(3,2))
    wastage_rate=db.Column(db.Numeric(3,2))
    number_AEFI=db.Column(db.Integer)
    number_AEFI_by_SIA=db.Column(db.Integer)
    funding_source=db.Column(db.String(255))
    comment=db.Column(db.String(500))
