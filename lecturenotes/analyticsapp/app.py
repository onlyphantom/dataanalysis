from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to Algoritma Insights app service!"


@app.route("/dashboard")
def analytics():
    import pandas as pd

    dat = pd.read_csv(
        "https://raw.githubusercontent.com/onlyphantom/dataanalysis/master/data_input/techcrunch.csv"
    )

    cond1 = dat["company"] == "Tesla Motors"
    result = (
        dat.loc[cond1, ["company", "round", "raisedCurrency", "raisedAmt"]]
        .sort_values(["round", "raisedAmt"])
        .to_html()
    )

    return render_template("analytics.html", result=result)


@app.route("/api")
def api():
    import pandas as pd

    dat = pd.read_csv(
        "https://raw.githubusercontent.com/onlyphantom/dataanalysis/master/data_input/techcrunch.csv"
    )

    cond1 = dat["company"] == "Tesla Motors"
    result = (
        dat.loc[cond1, ["company", "round", "raisedCurrency", "raisedAmt"]]
        .sort_values(["round", "raisedAmt"])
        .to_json()
    )

    return result


if __name__ == "__main__":
    app.run()
