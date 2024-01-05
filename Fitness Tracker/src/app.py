from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__, template_folder="templates")

exercises = []

#home page
@app.route("/")
def index():
    return render_template("index.html", exercises=exercises)

#adding exercise
@app.route("/add_exercise", methods=["POST"])
def add_exercise():
    exercise = request.form['exercise']
    exercises.append({"movement": exercise, "rep-range": "0", "done": False, "sets": {}, "RPE": 0})
    return redirect(url_for("index"))

#adding rep range
@app.route("/add_rep/<int:index>", methods=["GET", "POST"])
def add_rep(index):
    exercise = exercises[index]
    if request.method == "POST": 
        exercise["rep-range"] = request.form["rep_range"]
        return redirect(url_for("index"))
    else:
        return render_template("rep.html", exercise=exercise, index=index)

#adding sets 
@app.route("/add_set/<int:index>", methods=["GET", "POST"])
def add_set(index):
    exercise = exercises[index]
    if request.method == "POST":
        attempt = request.form['set']
        exercise["sets"][len(exercise["sets"]) + 1] = attempt
        return redirect(url_for("index"))
    else: 
        return render_template("set.html", exercise=exercise, index=index)

#adding RPE 
@app.route("/add_rpe/<int:index>", methods=["GET", "POST"])
def add_rpe(index):
    exercise = exercises[index]
    if request.method == "POST":
        exercise["RPE"] = request.form["rpe"]
        return redirect(url_for("index"))
    else:
        return render_template("rpe.html", exercise=exercise, index=index)

#editing exercise
@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    exercise = exercises[index]
    if request.method == "POST":
        exercise['movement'] = request.form['exercise']
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", exercise=exercise, index=index)

#delete exercise
@app.route("/delete/<int:index>")
def delete(index):
    del exercises[index]
    return redirect(url_for("index"))

#check box 
@app.route("/check/<int:index>")
def check(index):
    exercises[index]["done"] = not exercises[index]["done"]
    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(debug=True)