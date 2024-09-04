import http.server
import socketserver
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading
import time

PORT = 8000

# Global variable to control the server
server = None
observer = None  # Global observer variable to access in multiple functions

class ReloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(('.html', '.css', '.js')):
            print(f'{event.src_path} changed, reloading...')
            restart_server()

def start_server():
    global server
    Handler = http.server.SimpleHTTPRequestHandler
    server = socketserver.TCPServer(("", PORT), Handler)
    print(f"Serving at port {PORT}")
    server.serve_forever()

def stop_server():
    global server
    if server:
        server.shutdown()
        server.server_close()

def restart_server():
    stop_server()
    time.sleep(1)  # Give the OS time to release the port
    start_server()

def main():
    global observer

    # Start server in a separate thread
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()

    # Start watchdog observer
    event_handler = ReloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("KeyboardInterrupt detected, stopping server and observer...")
        stop_server()
        observer.stop()
        observer.join()
    finally:
        print("Exiting program.")
        exit(0)

if __name__ == "__main__":
    main()