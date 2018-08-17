from flask import Flask, render_template
app = Flask(__name__)

# Without render_template:
@app.route('/bmi/<int:weight>/<int:height>')
def bmi_calc(weight, height):
    bmi = weight / ((height/100)**2)  
    
    if bmi < 16:
        return 'Severely underweight'
    elif 16 <= bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal'
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

# With render_template:
kpis = {}
@app.route('/bmi2/<int:weight2>/<int:height2>')
def bmi_calc2(weight2, height2):
    bmi2 = weight2 / ((height2/100)**2)  
    kpis['w'] = weight2
    kpis['h'] = height2
    kpis['bmi'] = bmi2

    return render_template('bmi.html', kpis = kpis)

    

if __name__ == '__main__': 
  app.run(debug=True) 