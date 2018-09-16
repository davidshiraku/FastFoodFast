#!flask/bin/python
from flask import Flask, jsonify
import hashlib

app = Flask(__name__)

# Food category data structure
foodcategory = [
    {
        'id': 1,
        'title': u'Food category',
        'description': u'Soft drinks',
        'suspend': False,
        'reason': u''
    },
    {
        'id': 2,
        'title': u'Food category',
        'description': u'Food',
        'suspend': False,
        'reason': u''
    }
]
# End of food category data structure

# Food item data structure
fooditem = [
    {
        'id': 1,
        'title': u'Food item',
        'description': u'Coca cola',
        'category': 1,
        'price': 80,
        'suspend': False,
        'reason': u''
    },
    {
        'id': 2,
        'title': u'Food item',
        'description': u'Mango juice',
        'category': 1,
        'price': 100,
        'suspend': False,
        'reason': u''
    },
    {
        'id': 3,
        'title': u'Food item',
        'description': u'Lamb chops',
        'category': 2,
        'price': 150,
        'suspend': False,
        'reason': u''
    }
]
# End of food item data structure

# Food order data structure
foodorder = [
    {
        'id': 1,
        'title': u'Food order',
        'userid': u'sjames',
        'phone': u'0711443221',
        'physicaladdress': u'Moi avenue',
        'date': u'14/09/2018',
        'time': u'10:00',
        'status': u'Pending',
        'food': [3,2]
    },
    {
        'id': 2,
        'title': u'Food order',
        'userid': u'njane',
        'phone': u'0711333221',
        'physicaladdress': u'Kenyatta avenue',
        'date': u'14/09/2018',
        'time': u'10:00',
        'status': u'Pending',
        'food': [2]
    }
]
# End of order data structure

# User data structure

# Encrypt passwords
# Password 1
password = 'f@stf00d'
pw = hashlib.md5(password.encode())
passwd = pw.hexdigest()
# Password 2 may be added here
# End of encrypting passwords

user = [
    {
        'id': 1,
        'title': u'User',
        'description': u'Administrator',
        'login': u'ADMIN',
        'expiry': u'31/12/2022',
        'roleadmin': True,
        'rolegroup': False,
        'group': u'',
        'logincode': passwd,
        'suspend': False,
        'reason': u'',
        'accessright': []
    },
    {
        'id': 2,
        'title': u'User',
        'description': u'Guest',
        'login': u'GUEST',
        'expiry': u'31/12/2022',
        'roleadmin': False,
        'rolegroup': False,
        'group': u'',
        'logincode': u'',
        'suspend': False,
        'reason': u'',
        'accessright': [11]
    },
    {
        'id': 3,
        'title': u'User',
        'description': u'Client',
        'login': u'CLIENT',
        'expiry': u'31/12/2022',
        'roleadmin': False,
        'rolegroup': True,
        'group': u'',
        'logincode': u'',
        'suspend': False,
        'reason': u'',
        'accessright': [9,11]
    }
]
# End of food item data structure

# Food category manipulation start
# Obtain a particular food category with jsonified error handler
@app.route('/fastfoodfast/api/v1/foodcategory', methods=['GET'], endpoint='get_foodcategory')
def get_foodcategory():
    return jsonify({'foodcategory': foodcategory})

from flask import abort

@app.route('/fastfoodfast/api/v1/foodcategory/<int:task_id>', methods=['GET'], endpoint='get_task')
def get_task(task_id):
    task = [task for task in foodcategory if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


from flask import make_response

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# Add food category
from flask import request

@app.route('/fastfoodfast/api/v1/foodcategory', methods=['POST'], endpoint='create_task')
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    if not request.json or not 'description' in request.json:
        abort(400)
    task = {
        'id': foodcategory[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', "")
    }
    foodcategory.append(task)
    return jsonify({'task': task}), 201

# Update food category
@app.route('/fastfoodfast/api/v1/foodcategory/<int:task_id>', methods=['PUT'], endpoint='update_task')
def update_task(task_id):
    task = [task for task in foodcategory if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'suspend' in request.json and type(request.json['suspend']) is not bool:
        abort(400)
    if 'reason' in request.json and type(request.json['reason']) is not unicode:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['suspend'] = request.json.get('suspend', task[0]['suspend'])
    task[0]['reason'] = request.json.get('reason', task[0]['reason'])
    return jsonify({'task': task[0]})

# Delete food category
@app.route('/fastfoodfast/api/v1/foodcategory/<int:task_id>', methods=['DELETE'], endpoint='delete_task')
def delete_task(task_id):
    task = [task for task in foodcategory if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    foodcategory.remove(task[0])
    return jsonify({'result': True})

# End of food category manipulation

# Food item manipulation start
# Obtain a particular food item with jsonified error handler
@app.route('/fastfoodfast/api/v1/fooditem', methods=['GET'], endpoint='get_fooditem')
def get_fooditem():
    return jsonify({'fooditem': fooditem})

from flask import abort

@app.route('/fastfoodfast/api/v1/fooditem/<int:task_id>', methods=['GET'], endpoint='get_taskfooditem')
def get_taskfooditem(task_id):
    task = [task for task in fooditem if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

# Add food item
from flask import request

@app.route('/fastfoodfast/api/v1/fooditem', methods=['POST'], endpoint='create_taskfooditem')
def create_taskfooditem():
    if not request.json or not 'title' in request.json:
        abort(400)
    if not request.json or not 'description' in request.json:
        abort(400)
    if not request.json or not 'category' in request.json:
        abort(400)
    if not request.json or not 'price' in request.json:
        abort(400)
    task = {
        'id': fooditem[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'category': request.json.get('category', ""),
        'price': request.json.get('price', "")
    }
    fooditem.append(task)
    return jsonify({'task': task}), 201

# Update food item
@app.route('/fastfoodfast/api/v1/fooditem/<int:task_id>', methods=['PUT'], endpoint='update_taskfooditem')
def update_taskfooditem(task_id):
    task = [task for task in fooditem if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'category' in request.json and type(request.json['category']) is not unicode:
        abort(400)
    if 'suspend' in request.json and type(request.json['suspend']) is not bool:
        abort(400)
    if 'reason' in request.json and type(request.json['reason']) is not unicode:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['category'] = request.json.get('category', task[0]['category'])
    task[0]['suspend'] = request.json.get('suspend', task[0]['suspend'])
    task[0]['reason'] = request.json.get('reason', task[0]['reason'])
    return jsonify({'task': task[0]})

# Delete food item
@app.route('/fastfoodfast/api/v1/fooditem/<int:task_id>', methods=['DELETE'], endpoint='delete_taskfooditem')
def delete_taskfooditem(task_id):
    task = [task for task in fooditem if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    fooditem.remove(task[0])
    return jsonify({'result': True})

# End of food item manipulation

# Process orders
# Obtain a particular food order with jsonified error handler
@app.route('/fastfoodfast/api/v1/orders', methods=['GET'], endpoint='get_foodorder')
def get_foodorder():
    return jsonify({'foodorder': foodorder})

from flask import abort

@app.route('/fastfoodfast/api/v1/orders/<int:task_id>', methods=['GET'], endpoint='get_taskfoodorder')
def get_taskfoodorder(task_id):
    task = [task for task in foodorder if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

# Add food order
from flask import request

@app.route('/fastfoodfast/api/v1/orders', methods=['POST'], endpoint='create_taskfoodorder')
def create_taskfoodorder():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': foodorder[-1]['id'] + 1,
        'title': request.json['title'],
        'userid': request.json.get('userid', ""),
        'phone': request.json.get('phone', ""),
        'physicaladdress': request.json.get('physicaladdress', ""),
        'date': request.json.get('date', ""),
        'time': request.json.get('time', ""),
        'status': u'Pending',
        'food':request.json['food']
    }
    foodorder.append(task)
    return jsonify({'task': task}), 201

# Update food order status
@app.route('/fastfoodfast/api/v1/orders/<int:task_id>', methods=['PUT'], endpoint='update_taskfoodorder')
def update_taskfoodorder(task_id):
    task = [task for task in foodorder if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'userid' in request.json and type(request.json['userid']) != unicode:
        abort(400)
    if 'phone' in request.json and type(request.json['phone']) != unicode:
        abort(400)
    if 'physicaladdress' in request.json and type(request.json['physicaladdress']) != unicode:
        abort(400)
    if 'date' in request.json and type(request.json['date']) != unicode:
        abort(400)
    if 'time' in request.json and type(request.json['time']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'food' in request.json and type(request.json['food']) is not list:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['userid'] = request.json.get('userid', task[0]['userid'])
    task[0]['phone'] = request.json.get('phone', task[0]['phone'])
    task[0]['physicaladdress'] = request.json.get('physicaladdress', task[0]['physicaladdress'])
    task[0]['date'] = request.json.get('date', task[0]['date'])
    task[0]['time'] = request.json.get('time', task[0]['time'])
    task[0]['status'] = request.json.get('status', task[0]['status'])
    task[0]['food'] = request.json.get('food', task[0]['food'])
    return jsonify({'task': task[0]})

# End of processing orders

# User manipulation start
# Obtain a particular User with jsonified error handler
@app.route('/fastfoodfast/api/v1/user', methods=['GET'], endpoint='get_name')
def get_name():
    return jsonify({'user': user})

from flask import abort

@app.route('/fastfoodfast/api/v1/user/<int:task_id>', methods=['GET'], endpoint='get_user')
def get_user(task_id):
    task = [task for task in user if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

from flask import make_response

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# Add User
from flask import request

@app.route('/fastfoodfast/api/v1/user', methods=['POST'], endpoint='create_user')
def create_user():
    if not request.json:
        abort(400)
    if not 'title' in request.json:
        abort(400)
    if not 'description' in request.json:
        abort(400)
    if not 'login' in request.json:
        abort(400)
    if not 'expiry' in request.json:
        abort(400)
    if not 'roleadmin' in request.json or type(request.json['roleadmin']) is not bool:
        abort(400)
    if not 'rolegroup' in request.json or type(request.json['rolegroup']) is not bool:
        abort(400)
    if not 'group' in request.json:
        abort(400)
    if not 'logincode' in request.json:
        abort(400)
    if 'accessright' in request.json and type(request.json['accessright']) is not list:
        abort(400)

    # Encrypt password
    if request.json['logincode'].strip() != "":
        pw = hashlib.md5( request.json['logincode'].encode())
        passwd = pw.hexdigest()
    else:
        passwd = ""
    # End of encrypting password

    task = {
        'id': user[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'login': request.json.get('login', ""),
        'expiry': request.json.get('expiry', ""),
        'roleadmin': request.json.get('roleadmin', ""),
        'rolegroup': request.json.get('rolegroup', ""),
        'group': request.json.get('group', ""),
        'logincode': passwd,
        'suspend': False,
        'reason': u'',
        'accessright': request.json.get('accessright', "")
    }
    user.append(task)
    return jsonify({'task': task}), 201

# Update User
@app.route('/fastfoodfast/api/v1/user/<int:task_id>', methods=['PUT'], endpoint='update_user')
def update_user(task_id):
    task = [task for task in user if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'login' in request.json and type(request.json['login']) is not unicode:
        abort(400)
    if 'expiry' in request.json and type(request.json['expiry']) is not unicode:
        abort(400)
    if 'roleadmin' in request.json and type(request.json['roleadmin']) is not bool:
        abort(400)
    if 'rolegroup' in request.json and type(request.json['rolegroup']) is not bool:
        abort(400)
    if 'group' in request.json and type(request.json['group']) is not unicode:
        abort(400)
    if 'logincode' in request.json and type(request.json['logincode']) is not unicode:
        abort(400)
    if 'suspend' in request.json and type(request.json['suspend']) is not unicode:
        abort(400)
    if 'reason' in request.json and type(request.json['reason']) is not unicode:
        abort(400)
    if 'accessright' in request.json and type(request.json['accessright']) is not list:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['login'] = request.json.get('login', task[0]['login'])
    task[0]['expiry'] = request.json.get('expiry', task[0]['expiry'])
    task[0]['roleadmin'] = request.json.get('roleadmin', task[0]['roleadmin'])
    task[0]['rolegroup'] = request.json.get('rolegroup', task[0]['rolegroup'])
    task[0]['group'] = request.json.get('group', task[0]['group'])
    task[0]['logincode'] = request.json.get('logincode', task[0]['logincode'])
    task[0]['suspend'] = request.json.get('suspend', task[0]['suspend'])
    task[0]['reason'] = request.json.get('reason', task[0]['reason'])
    task[0]['accessright'] = request.json.get('accessright', task[0]['accessright'])
    return jsonify({'task': task[0]})

# Delete User
@app.route('/fastfoodfast/api/v1/user/<int:task_id>', methods=['DELETE'], endpoint='delete_user')
def delete_user(task_id):
    task = [task for task in user if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    user.remove(task[0])
    return jsonify({'result': True})

# End of User manipulation

# Start app on Flask
if __name__ == '__main__':
    app.run(debug=True)
