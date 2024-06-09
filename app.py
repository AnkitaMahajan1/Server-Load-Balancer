from flask import Flask, render_template_string, jsonify
import threading
import requests
import time
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Load Balancer with Health Check")
parser.add_argument('--health-check-interval', type=int, default=10, help='Health check interval in seconds')
parser.add_argument('--health-check-url', type=str, default='/health', help='Health check URL path')
args = parser.parse_args()

# List of servers
servers = [
    {'url': 'http://127.0.0.1:5001', 'status': 'UP'},
    {'url': 'http://127.0.0.1:5002', 'status': 'UP'},
    {'url': 'http://127.0.0.1:5003', 'status': 'UP'}
]

health_check_interval = args.health_check_interval
health_check_url = args.health_check_url

# Load balancer app
app = Flask(__name__)

# Function to perform health check
def health_check():
    while True:
        print('Starting health check...')
        for server in servers:
            try:
                response = requests.get(f"{server['url']}{health_check_url}")
                if response.status_code == 200:
                    server['status'] = 'UP'
                else:
                    server['status'] = 'DOWN'
                    print(f"Server {server['url']} is down (status code {response.status_code})")
            except requests.exceptions.RequestException as e:
                server['status'] = 'DOWN'
                print(f"Server {server['url']} is down (exception: {e})")
        print('Health check cycle complete')
        time.sleep(health_check_interval)

# Round-robin server index
server_index = 0

# Function to get the next available server
def get_next_server():
    global server_index
    available_servers = [server for server in servers if server['status'] == 'UP']
    if not available_servers:
        return None
    server_url = available_servers[server_index % len(available_servers)]['url']
    server_index += 1
    return server_url

@app.route('/status')
def status():
    return jsonify(servers)

@app.route('/ui')
def ui():
    selected_server = get_next_server()
    return render_template_string(open('ui.html').read(), selectedServer=selected_server)

if __name__ == "__main__":
    try:
        # Start health check thread
        print('Start the health check first')
        threading.Thread(target=health_check, daemon=True).start()
    except Exception as e:
        print(f"Failed to start health check thread: {e}")

    # Run the load balancer on port 80
    try:
        print('Starting Flask app on port 80')
        app.run(host='0.0.0.0', port=80)
    except Exception as e:
        print(f"Failed to start Flask app: {e}")
