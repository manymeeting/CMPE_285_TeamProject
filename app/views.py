from app.PickStrategies import get_stock_list_all, get_strategy_stock_info, get_historical_strategy_stock_value
from flask import render_template, flash, redirect, request
from app import app
from .forms import InvestForm
from pprint import pprint
import json


@app.route('/invest', methods=['GET', 'POST'])
def invest():
    form = InvestForm(request.form)
    # try:
    #
    # except:
    #     return render_template('error.html')
    if request.method =='POST':
        amount = float(request.form['amount'])
        if amount < 5000:
            return render_template('error.html')
        print(amount)
        choices = request.form.getlist('strategies')
        if len(choices) <= 0 or len(choices) > 2:
            return render_template('error.html')
        pprint(choices)
        testArray = ['Ethical']
        stocklist = get_stock_list_all(testArray)
        details = get_strategy_stock_info(stocklist, amount)
        pprint(stocklist)
        history = get_historical_strategy_stock_value(stocklist, amount)
        pprint(history)
        return render_template("result.html", details=details, history=history)
        # return render_template("result.html", details=details, data=map(json.dumps, details))

    return render_template('new_index.html')

