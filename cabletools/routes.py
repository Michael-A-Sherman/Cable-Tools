from flask import request, render_template, redirect, flash, make_response
from cabletools import app
from cabletools.cable_calc import get_loss
from cabletools.forms import CalcForm, PathTrakForm
from cabletools.pathtrak import search_pathtrak_api, search, vpn_search


@app.route("/", methods=["POST", "GET"])
@app.route("/index", methods=["POST", "GET"])
def new_link_create():
    form = PathTrakForm(request.form)
    print(form.errors)
    if request.method == "POST":
        info = search_pathtrak_api(request.form["node"].upper().rstrip())
        link = vpn_search(info)
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
def hello():
    form = CalcForm(request.form)
    print(form.errors)
    if request.method == "POST":
        footage = request.form["footage"]
        cable = request.form["cable"]
        print(footage)
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


# @app.route("/vpn", methods=["POST", "GET"])
# def vpn_link_create():
#     form = PathTrakForm(request.form)
#     print(form.errors)
#     if request.method == "POST":
#         info = search_pathtrak_api(request.form["node"].upper().rstrip())
#         link = vpn_search(info)
#         if form.validate():
#             if len(info) == 1:
#                 return redirect(link, code=302)
#             elif len(info) == 0:
#                 flash("Node Not Found, Try Again")
#             else:
#                 return render_template("vpn_results.html", form=form, link=link)
#         else:
#             flash("All the form fields are required. ")
#     return render_template("index.html", form=form)
