from flask import Flask, render_template, request

Flask_App = Flask(__name__) 

@Flask_App.route('/', methods=['GET'])
def index():
    
  return render_template('index.html')

@Flask_App.route('/operation_result/', methods=['POST'])
def operation_result():

    error = None
    result = None

    # request.form looks for:
    # html tags with matching "name= "
    capital_amount = request.form['CapitalAmount']  
    amount = request.form['Amount'] 
    roi = request.form['ROI']
    timeline = request.form['TimeLine']
    duration = request.form['Duration']

   # try:
    #    input1 = float(first_input)
     #   input2 = float(second_input)
    capital_amount=int(capital_amount)
    amount=int(amount)
    roi=int(roi)
    duration=int(duration)
    b=[]
    c=[]
    result=capital_amount

    if (capital_amount<0):

        return render_template(
            'result.html',
            capital_amount=capital_amount,
            amount=amount,
            duration=duration,
            timeline=timeline,
            error="Invalid Capital Amount",
            roi=roi,
            calculation_success=False,
        )
    elif (amount <=0):

        return render_template(
            'result.html',
            capital_amount=capital_amount,
            amount=amount,
            duration=duration,
            timeline=timeline,
            error="Invalid Amount",
            roi=roi,
            calculation_success=False,
        )
    elif (roi <=0):

        return render_template(
            'result.html',
            capital_amount=capital_amount,
            amount=amount,
            duration=duration,
            timeline=timeline,
            error="Invalid rate of Interest",
            roi=roi,
            calculation_success=False,
        )
    elif (duration <=0):

        return render_template(
            'result.html',
            capital_amount=capital_amount,
            amount=amount,
            duration=duration,
            timeline=timeline,
            error="Invalid duration",
            roi=roi,
            calculation_success=False,
        )
    else:

        if timeline == "years":
            for i in range(0,duration):
                result = amount+result
                c.append(result)
            for i in range(0,duration):
                result=capital_amount*(1+(roi/100))
                capital_amount=amount+result
                b.append(result+100)
        else:
            for i in range(0,duration):
                result = amount+result
                c.append(result)
            for i in range(0,duration):
                result=capital_amount*(1+(roi/100*12))
                capital_amount=amount+result
                b.append(result+amount)

            
        return render_template(
            'result.html',
            duration=duration,
            timeline=timeline,
            first=c[-1],
            second=b[-1],
            roi=roi,
            calculation_success=True,
        )
        

if __name__ == '__main__':
    Flask_App.debug = True
    Flask_App.run()