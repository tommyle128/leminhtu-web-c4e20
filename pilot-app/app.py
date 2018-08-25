from flask import *
import mlab
from mongoengine import *
from models.service import Service
from models.customer import Customer

app = Flask(__name__)
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/search/<g>')
# def search(g):
#     all_service = Service.objects(
#         gender=g, 
#         address__icontains="Hà Nội")    
#     return render_template(
#         'search.html',
#         all_service=all_service
#         )

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

@app.route('/admin/')
def admin():
    all_service = Service.objects()
    return render_template(
        'admin.html',
        all_service = all_service
        )

@app.route('/delete/<service_id>')
def delete(service_id):
    deleted_id = Service.objects.with_id(service_id)
    if deleted_id is not None:
        deleted_id.delete()
        return redirect(url_for('admin'))
    else:
        return "Not found"

@app.route('/new-service', methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template('new-service.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        if form['gender'] == 'male':
            gender = 1
        else:
            gender = 0

        new_service = Service(
            name = name,
            yob = yob,
            phone = phone,
            gender = gender
        )
        new_service.save()

        return redirect (url_for('admin'))

@app.route('/search/')
def search():
    all_service = Service.objects()    
    return render_template(
        'search.html',
        all_service=all_service
        )

@app.route('/detail/<service_id>')
def detail(service_id):
    service = Service.objects.with_id(service_id)    
    return render_template(
        'detail.html',
        service=service
        )

@app.route('/update/<service_id>', methods=["GET", "POST"])
def update(service_id):
    service = Service.objects.with_id(service_id)

    if request.method == "GET":
        return render_template('update-service.html', service = service)
    elif request.method == "POST":
        form = request.form
        if form['name'] != None:
            name = form['name']
            service.update(set__name = name)
        if form['yob'] != None:
            yob = form['yob']
            service.update(set__yob = yob)
        if form['height'] != None:
            height = form['height']
            service.update(set__height = height)
        if form['phone'] != None:
            phone = form['phone']
            service.update(set__phone = phone)
        if form['address'] != None:
            address = form['address']
            service.update(set__address = address)

        return redirect (url_for('admin'))


if __name__ == '__main__':
  app.run(debug=True)

