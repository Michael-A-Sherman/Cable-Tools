from flask import request, render_template, redirect, flash, make_response
from cabletools import app
from cabletools.cable_calc import get_loss
from cabletools.forms import CalcForm, PathTrakForm
from cabletools.pathtrak import pathtrak_search, spectrum_view


@app.route("/", methods=["POST", "GET"])
@app.route("/index", methods=["POST", "GET"])
def michigan():
    mich_base_link = "https://nept01.chartercom.com/pathtrak/"
    form = PathTrakForm(request.form)
    if request.method == "POST":
        info = pathtrak_search(mich_base_link, request.form["node"].upper().rstrip())
        link = spectrum_view(mich_base_link, info)
        if form.validate():
            if len(info) == 1:
                return redirect(link, code=302)
            elif len(info) == 0:
                flash("Node Not Found, Try Again")
            else:
                return render_template("results.html", form=form, link=link)
        else:
            flash("All the form fields are required. ")
    return render_template("index.html", form=form)


@app.route("/calculator", methods=["POST", "GET"])
def calculator():
    form = CalcForm(request.form)
    if request.method == "POST":
        footage = request.form["footage"]
        cable = request.form["cable"]
        if form.validate():
            results = get_loss(int(footage), cable)
            flash("55 MHz -  " + "{:2.2f}".format(results[0]) + " dB")
            flash("750 MHz -  " + "{:2.2f}".format(results[1]) + " dB")
            flash("865 MHz -  " + "{:2.2f}".format(results[2]) + " dB")
            flash("1 GHz -  " + "{:2.2f}".format(results[3]) + " dB")
        else:
            flash("Enter a valid cable footage")
    return render_template("calculator.html", form=form)


@app.route("/<node>", methods=["POST", "GET"])
def direct_link(node):
    form = PathTrakForm(request.form)
    info = search_pathtrak_api(node.upper().rstrip())
    link = search(info)
    if len(info) == 1:
        return redirect(link, code=302)
    elif len(info) == 0:
        flash("Node Not Found, Try Again")
    elif request.method == "POST":
        if form.validate():
            if len(info) == 1:
                return redirect(link, code=302)
            elif len(info) == 0:
                flash("Node Not Found, Try Again")
            else:
                return render_template("results.html", form=form, link=link)
    else:
        return render_template("results.html", form=form, link=link)
    return render_template("index.html", form=form)


@app.route('/', subdomain ='test', methods=["POST", "GET"]) 
def canton():
    base_link = "https://nept01.chartercom.com/pathtrak/"
    form = PathTrakForm(request.form)
    if request.method == "POST":
        info = pathtrak_search(base_link, request.form["node"].upper().rstrip())
        link = spectrum_view(base_link, info)
        if form.validate():
            if len(info) == 1:
                return redirect(link, code=302)
            elif len(info) == 0:
                flash("Node Not Found, Try Again")
            else:
                return render_template("results.html", form=form, link=link)
        else:
            flash("All the form fields are required. ")
    return render_template("index.html", form=form)

