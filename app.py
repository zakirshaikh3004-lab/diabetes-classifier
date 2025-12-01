from flask import *
import joblib

model = joblib.load("model3.pkl")

app=Flask(__name__)
@app.route("/", methods=["POST","GET"])
def home():
	if request.method=="POST":
		age=float(request.form.get("age"))
		bmi=float(request.form.get("bmi"))
		fs=float(request.form.get("fs"))
		hb=float(request.form.get("hb"))
		d1=[age,bmi,fs,hb]

		ge=int(request.form.get("ge"))
		if ge==1:
			d2=[1,0]
		else:
			d2=[0,1]


		hy=int(request.form.get("hy"))
		if hy==1:
			d3=[1,0]
		else:
			d3=[0,1]

		fh=int(request.form.get("fh"))
		if fh==1:
			d4=[1,0]
		else:
			d4=[0,1]

		d=[d1+d2+d3+d4]
		result=model.predict(d)
		msg="Person is Non-Diabetics" if result[0] ==0 else "Person is Diabetic"
		return render_template("home.html",msg=msg)

	else:
		return render_template("home.html")
		







if __name__=="__main__":
	app.run(debug=True,use_reloader=True)






















