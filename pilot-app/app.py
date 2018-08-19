from flask import Flask, render_template
import mlab
from mongoengine import *
from models.service import Service
from models.customer import Customer

app = Flask(__name__)
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<g>')
def search(g):
    all_service = Service.objects(
        gender=g, 
        address__icontains="Hà Nội")    
    return render_template(
        'search.html',
        all_service=all_service
        )

@app.route('/customer/')
def customer():
    all_customers = Customer.objects()
    return render_template('customer.html', all_customers=all_customers)

@app.route('/customer/male/notcontacted/first10')
def segment_10male_notcontacted():
    segment = Customer.objects[0:10]
    all_customers = segment(
        gender=1,
        contacted=False,
    )
    
    return render_template('customer.html', all_customers=all_customers)

if __name__ == '__main__':
  app.run(debug=True)

