from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from flask import *

app = Flask(__name__)

#this is MySQL in localhost
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root@localhost/xxx"

#this is mysql inside docker
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql://root:password@172.17.0.2:3306/xxx"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secret key"

db = SQLAlchemy(app)

'''
#if we return data from pre existing database use this pattern
student = db.Table("student",db.metadata,autoload=True,autoload_with=db.engine)


OR use following way bot are same
'''

#OR USE
Base  = automap_base()
Base.prepare(db.engine,reflect=True)

'''
  Bununla DB deki student tablosu Student' degiskenine MAP edilir.Yani arka planda
  bir Student objesi olusturulur
'''
Student = Base.classes.student   


@app.route("/test")
def test():
    return "test is OK"

@app.route("/")
def list_students():
      
      '''     Adding new Student 
      new_student = Student(name='McKenzie',age='55')
      db.session.add(new_student)
      db.session.commit() 
    '''
    
      #use following to retrieve data
      results = db.session.query(Student).all() 
      
      '''
      for r in results : 
          print(r.name)
      '''
         
      return render_template("list_student.html",students = results)
  
  
  
if __name__ == "__main__" :
    app.run(host='0.0.0.0')