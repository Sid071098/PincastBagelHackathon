from flask import Flask, request, jsonify

app = Flask(__name__)

# Global variables to store coordinates
latitude = None
longitude = None

# Route to receive coordinates
@app.route('/receive-coordinates', methods=['POST'])
def receive_coordinates():
    global latitude, longitude
    data = request.get_json()
    print(f"Raw data received: {data}")  # Debugging line
    
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if latitude and longitude:
        print(f"Received coordinates: Latitude = {latitude}, Longitude = {longitude}")
    else:
        print("Invalid data received.")
    
    return jsonify({'status': 'Coordinates received', 'latitude': latitude, 'longitude': longitude}), 200

# Route to check saved coordinates
@app.route('/get-coordinates', methods=['GET'])
def get_coordinates():
    if latitude and longitude:
        return jsonify({'latitude': latitude, 'longitude': longitude}), 200
    else:
        return jsonify({'error': 'No coordinates received yet'}), 404

if __name__ == '__main__':
    app.run(debug=True)
