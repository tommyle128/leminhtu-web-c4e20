from flask import *
import mlab
from mongoengine import *
from models.service import Service
from models.customer import Customer
from models.user import User
from models.order import Order
import datetime
from gmail import *

app = Flask(__name__)
app.secret_key = "a super super secret key"
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

@app.route('/update/<service_id>', methods=["GET", "POST"])
def update(service_id):
    service = Service.objects.with_id(service_id)
    
    if request.method == "GET":
        return render_template('update-service.html', service = service)
    elif request.method == "POST":
        form = request.form
        if form['name'] != service['name']:
            service.update(set__name=form['name'])
        if form['yob'] != service['yob']:
            service.update(set__yob=form['yob'])
        if form['height'] != service['height']:
            service.height(set__height=form['height'])
        if form['phone'] != service['phone']:
            service.update(set__phone=form['phone'])
        if form['address'] != service['address']:
            service.update(set__address=form['address'])
        

        return redirect (url_for('admin'))

@app.route('/sign-up/', methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template ('sign-up.html')
    elif request.method == "POST":
        signin_form = request.form
        name = signin_form['name']
        email = signin_form['email']
        username = signin_form['username']
        password = signin_form['password']
        
        new_user = User(
            name=name,
            email=email,
            username=username,
            password=password,

        )
        new_user.save()

        return redirect(url_for('login'))

@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template ('login.html')
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']

        all_users = User.objects()
        count = 0
        for i in range (len(all_users)):
            if username == all_users[i]['username'] and password == all_users[i]['password']:
                session['loggedin'] = True
                session['user_id'] = str(all_users[i].id)
                return redirect('detail-full')
            else:
                count += 1
    
        if count == len(all_users):
            return "Wrong username and password"

@app.route('/logout/')
def logout():   
    session['loggedin'] = False
    return redirect(url_for('index'))

@app.route('/detail-full/')
def detailfull():
    if "loggedin" in session:
        if session['loggedin'] == True:
            all_services = Service.objects()
            return render_template(
                'detail-full.html', 
                all_services=all_services
                )
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route("/order/<service_id>")
def order(service_id):
    new_order = Order(
        service_id = service_id,
        user_id = session['user_id'],
        date_time = datetime.datetime.now(),
        is_accepted = False
    )
    new_order.save()
    service = Service.objects.with_id(service_id)
    if service is not None:
        return "Đã gửi yêu cầu" 
    else:
        return "Service is not found!"

@app.route('/orders/')
def orders():
    all_orders = Order.objects()
    display_orders = []
    
    for i in range(len(all_orders)):        
        service = Service.objects.with_id(all_orders[i]['service_id'])
        user = User.objects.with_id(all_orders[i]['user_id'])
        display = {}
        display['is_accepted'] = all_orders[i]['is_accepted']
        display['name_service'] = service['name']
        display['name_user'] = user['name']
        display['date_time']=all_orders[i]['date_time']
        display['order_id']=str(all_orders[i].id)
        display_orders.append(display)

    return render_template(
        'orders.html',
        display_orders=display_orders
        )
   

@app.route('/sent-mess/<order_id>')
def sent_mess(order_id):
    order = Order.objects.with_id(order_id)
    order.update(set__is_accepted=True)
    order.reload()

    user = User.objects.with_id(order['user_id'])
    email = user['email']
    
    gmail = GMail('Mùa đông không lạnh<tulm.test@gmail.com>','congacon')
    html_content="""
    <p>Yêu cầu của bạn đã được xử lý, chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất.</p>
    <p>Cảm ơn bạn đã sử dụng dịch vụ của ‘Mùa Đông Không Lạnh’”</p>
    """
    msg = Message('Mùa đông không lạnh - Yêu cầu dịch vụ của bạn được chấp nhận',to=email, html=html_content)  
    gmail.send(msg)

    return redirect(url_for('orders')) 



if __name__ == '__main__':
  app.run(debug=True)

