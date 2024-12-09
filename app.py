from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample 
data = [

 {'id': 1, 'name': 'Item 1'},

 {'id': 2, 'name': 'Item 2'},

 {'id': 3, 'name': 'Item 3'}

]

# GET request to retrieve all items

@app.route('/items', methods=['GET'])

def get_items():

 return jsonify({'items': data})

# GET request to retrieve a specific item by ID

@app.route('/items/<int:item_id>', methods=['GET'])

def get_item(item_id):

 item = next((item for item in data if item['id'] == item_id), None)

 if item:

 return jsonify({'item': item})

 else:

 return jsonify({'message': 'Item not found'}), 404

# POST request to add a new item

@app.route('/items', methods=['POST'])

def add_item():
 new_item = {'id': len(data) + 1, 'name': request.json['name']}

 data.append(new_item)

 return jsonify({'item': new_item}), 201

# PUT request to update a specific item by ID

@app.route('/items/<int:item_id>', methods=['PUT'])

def update_item(item_id):

 item = next((item for item in data if item['id'] == item_id), None)

 if item:

 item['name'] = request.json['name']

 return jsonify({'item': item})

 else:

 return jsonify({'message': 'Item not found'}), 404

# DELETE request to remove a specific item by ID

@app.route('/items/<int:item_id>', methods=['DELETE'])

def delete_item(item_id):

 global data

 data = [item for item in data if item['id'] != item_id]

 return jsonify({'message': 'Item deleted'}), 200

if __name__ == '__main__':

 app.run(debug=True)






























Install Flask

>>>pip install flask

Step 2: Start the Flask App

Save the code as app.py and execute 

>>>python app.py

Copy the url produced http://127.0.0.1:5000

Step 3: Use Postman to Test Endpoints

1. GET Request to Retrieve All Items:

 Set the request type to GET.

 Enter the URL: http://127.0.0.1:5000/items

 Click "Send."
GET Request to Retrieve a Specific Item by ID:

 Set the request type to GET.

 Enter the URL for a specific item ID, for example: 

http://127.0.0.1:5000/items/1

 Click "Send."
POST Request to Add a New Item:

 Set the request type to POST.

 Enter the URL: http://127.0.0.1:5000/items

 Go to the "Body" tab, select "raw" and choose "JSON (applica-

tion/json)".Enter the request body 

 Click "Send
PUT Request to Update an Existing Item:

 Set the request type to PUT.

 Enter the URL for a specific item ID, for example: 

http://127.0.0.1:5000/items/1
Go to the "Body" tab, select "raw" and choose "JSON (applica-

tion/json)".

 Enter the updated information 

 Click "Send."
DELETE Request to Remove a Specific Item by ID:

 Set the request type to DELETE.

 Enter the URL for a specific item ID, for example: 

http://127.0.0.1:5000/items/1

 Click "Send."

python app.py
