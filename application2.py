import os,csv
from flask import Flask, flash, request, redirect, url_for,session
#from flask.ext.session import Session
from werkzeug.utils import secure_filename
from flask import render_template, request,flash,url_for,send_from_directory
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# SESSION_TYPE = 'redis'
# app.config.from_object(__name__)
# Session(app)
siasum_id=None

@app.route("/")
def activity():
    countries=Country.query.all()
    #interventions=Intervention.query.all()
    return render_template("activity.html",countries=countries)

@app.route("/activitycont",methods=['GET','POST'])
def activitycont():
    # dict=request.form
    # dict={k: v for k, v in dict.items() if v is not ''}
    # activity=Activity(iso3=dict.get('iso3'),start_date=dict.get('start_date'),end_date=dict.get('end_date'),status=dict.get('status'),sia_type=dict.get('sia_type'))
    # db.session.add(activity)
    # db.session.commit()

    return render_template("activitycont.html")

@app.route("/phase" ,methods=['GET','POST'])
def phase():
    total_phase=request.form.get("total_phase")

    return render_template("phase.html",total_phase=total_phase)

@app.route("/last",methods=['GET','POST'])
def last():
    return render_template("last.html")

@app.route("/save",methods=['GET','POST'])
def save():
    return render_template("save.html")

@app.route("/subnational")
def subnational():
    return render_template("subnational.html")











@app.route("/add_sia_sum",methods=["POST"])
def add_sia_sum():
    dict=request.form
    sia_type=request.form.get("sia_type")
    dict={k: v for k, v in dict.items() if v is not ''}
    siasum=SIASum(iso3=dict.get('iso3'),start_date=dict.get('start_date'),end_date=dict.get('end_date'),status=dict.get('status'),sia_type=dict.get('sia_type'),source=dict.get('source'),comment=dict.get('comment'))

    # if request.form['total_phase']:
    # sia_type=request.form.get("sia_type")
    # phases=[]
    # source=request.form.get("source")
    # siasum=SIASum(iso3=iso3,start_date=start_date,end_date=end_date,status=status,sia_type=sia_type,source=source,comment=comment)
    # status=request.form.get("status")
    total_phase=dict.get("total_phase")
    phases=[]
    if total_phase:
        total_phase=int(total_phase)
        phases=list(range(1,total_phase+1))

    # end_date=request.form.get("end_date")
    # start_date=request.form.get("start_date")
    # comment=request.form.get("comment")
    intervention_id=request.form.getlist("interventions")
    # iso3=request.form.get("iso3")

    db.session.add(siasum)
    db.session.commit()
    for i in intervention_id:
        siasum.addDetail(intervention_id=i)
    return render_template("siadetail2.html",siasum_id=siasum_id,total_phase=total_phase,phases=phases)

@app.route("/siadetail.html",methods=["POST"])
def siadetail(siasum_id):
    return "%s"%(siasum_id)


@app.route("/querySIA",methods=["POST"])
def querySIA():
    iso3=request.form.get('iso3')
    pastSIAs=db.session.query(SIASum).filter_by(iso3=iso3).all()
    if (pastSIA):
        return pastSIAs
    else:
        return []



UPLOAD_FOLDER = 'C:/Users/Xi Li/Desktop/upload'
ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'xls'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
        #     #flash('No file part')
             return "Please upload a file"
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            #flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # f = open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # reader = csv.reader(f)
            # for target_age_group,target_population in reader:
            #     row=SIADetail(target_age_group="test",target_population=30000)
            #     db.session.add(row)
            #     db.session.commit()
            return "success"
    return render_template("siadetail2.html")

    # if request.method=='POST':
    #   if 'file' not in request.files:
    #       return redirect(request.url)
    #   file=reqest.files['file']
    #   if file.filename=='':
    #       return redirect(request.url)
    #   if file and allowed_file(file.filename):
    #       filename=secure_filename(file.filename)
    #       return "success"

    # return "failure"

# UPLOAD_FOLDER = 'C:/Users/Xi Li/Desktop/upload'
# ALLOWED_EXTENSIONS = {'xlsx', 'csv', 'xls'}

# #app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit an empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('uploaded_file',
#                                     filename=filename))
#     return '''
#     <!doctype html>
#     <title>Upload new new File</title>
#     <h1>Upload new File</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file>
#       <input type=submit value=Upload>
#     </form>
#     '''


# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)
#     