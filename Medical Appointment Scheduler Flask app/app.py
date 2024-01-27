from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

appointments = []

@app.route("/")
def index():
    return render_template("index.html", appointments=appointments)

@app.route("/schedule", methods=["POST"])
def schedule():
    patient_name = request.form.get("patient_name")
    appointment_date = request.form.get("appointment_date")
    appointment_time = request.form.get("appointment_time")

    appointment = {
        "patient_name": patient_name,
        "appointment_date": appointment_date,
        "appointment_time": appointment_time
    }

    appointments.append(appointment)

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
