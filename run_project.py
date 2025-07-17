import subprocess
import webbrowser
import time

print("Starting FastAPI server...")
# Start FastAPI (replace 'main:app' with your API file if needed)
fastapi_process = subprocess.Popen(["uvicorn", "main:app", "--reload"])

# Give FastAPI 2 seconds to start up
time.sleep(2)

print("Starting HTTP server for frontend...")
# Start HTTP server to serve your HTML
http_process = subprocess.Popen(["python", "-m", "http.server", "5500"])

# Open the web page
print("Opening browser...")
webbrowser.open("http://localhost:5500")

try:
    fastapi_process.wait()
    http_process.wait()
except KeyboardInterrupt:
    print("Shutting down...")
    fastapi_process.terminate()
    http_process.terminate()
