# Server-Load-Balancer
Server Load Balancer is a simple Python application that acts as a load balancer for distributing incoming requests among multiple backend servers. It provides round-robin load balancing and health checks to ensure optimal performance and reliability.

https://github.com/AnkitaMahajan1/Server-Load-Balancer/assets/61576746/cf9163f5-eb2a-4a38-bf1b-5259f88d663c

Features
🔄 Round-Robin Load Balancing: Requests are evenly distributed among the available backend servers using a round-robin algorithm.

⚠️ Health Checks: The load balancer periodically checks the health status of backend servers and excludes unhealthy servers from the rotation.

🌐 UI Dashboard: The load balancer includes a web-based dashboard for monitoring the status of backend servers and their health.

Technologies Used
Python
Flask
HTML
CSS
JavaScript
How to Run Locally
To run the Server Load Balancer on your local machine, follow these steps:

Clone the Repository:

bash
Copy code
git clone [https://github.com/yourusername/server-load-balancer.git](https://github.com/AnkitaMahajan1/Server-Load-Balancer.git)
Install Dependencies:
cd server-load-balancer
create a virtual environment
cd to the virtual env and install below
pip install flask, requests

Start Backend Servers:
python backendServer.py
python backendServer2.py
Ensure that your backend servers are running on ports 5001, 5002, and 5003.(or any of these ports)

Run the Load Balancer:

python app.py --health-check-interval 10 --health-check-url /health
This command starts the load balancer on port 80 and configures it to perform health checks every 10 seconds using the /health endpoint.

Access the UI:

Open a web browser and navigate to http://127.0.0.1/ui to view the server status dashboard.

Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests to help improve this project.

License
This project is licensed under the MIT License - see the LICENSE file for details.
