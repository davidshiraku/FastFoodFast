import json
import pytest

# While running pytest while inside tests sub-folder this was necessary
#import sys
#sys.path.append('..')
# End of unnecessary code while running tests while inside tests sub-folder

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from fastfoodfast import app

@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass # databases and resourses have to be freed at the end. But so far we don't have anything

    request.addfinalizer(teardown)
    return test_client

def post_json(client, url, json_dict):
    """Send dictionary json_dict as a json to the specified url """
    return client.post(url, data=json.dumps(json_dict), content_type='application/json')

def json_of_response(response):
    """Decode json from response"""
    return json.loads(response.data.decode('utf8'))

def test_FoodFategoryRespone(client):
    response = client.get('/fastfoodfast/api/v1/foodcategory')
    assert b'Soft drinks' in response.data

def test_FoodFategoryPost(client):
    #response = post_json(client, '/fastfoodfast/api/v1/foodcategory', {'key': 'value'})
    response = post_json(client, 'http://localhost:5000/fastfoodfast/api/v1/foodcategory', {'title':'Food category', 'description':'Accompaniments', 'suspend':'N', 'reason':''})
    print(response.status_code)
    assert response.status_code == 201
    #assert json_of_response(response) == {"answer": 'value' * 2}
    assert b'Accompaniments' in response.data
