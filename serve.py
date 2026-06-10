#!/usr/bin/env python3
import os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
port = int(os.environ.get("PORT", sys.argv[1] if len(sys.argv) > 1 else 3456))
import http.server
handler = http.server.SimpleHTTPRequestHandler
with http.server.HTTPServer(("", port), handler) as httpd:
    print(f"Serving on port {port}", flush=True)
    httpd.serve_forever()
