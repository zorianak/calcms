"""
CalCMS API — bare-bones HTTP server entry point.

This module is intentionally left minimal: the HTTP server implementation
is yours to write. Below is a standard-library example to get you started.
Swap it for any framework (e.g. ASGI with Starlette, or a raw asyncio server).
"""

import http.server
import json
from http import HTTPStatus


class CalCMSRequestHandler(http.server.BaseHTTPRequestHandler):
    """Minimal request handler — extend this with your routing logic."""

    def do_GET(self) -> None:  # noqa: N802
        if self.path == "/health":
            self._send_json({"status": "ok"})
        else:
            self._send_json({"error": "Not found"}, status=HTTPStatus.NOT_FOUND)

    def do_POST(self) -> None:  # noqa: N802
        # Route POST /graphql to the GraphQL handler
        if self.path == "/graphql":
            # TODO: wire up the Strawberry schema here
            self._send_json({"error": "GraphQL not yet wired up"}, status=HTTPStatus.NOT_IMPLEMENTED)
        else:
            self._send_json({"error": "Not found"}, status=HTTPStatus.NOT_FOUND)

    def _send_json(self, payload: dict, status: HTTPStatus = HTTPStatus.OK) -> None:
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt: str, *args: object) -> None:  # type: ignore[override]
        print(f"[calcms-api] {fmt % args}")


def run(host: str = "0.0.0.0", port: int = 8000) -> None:
    """Start the HTTP server."""
    server = http.server.HTTPServer((host, port), CalCMSRequestHandler)
    print(f"CalCMS API listening on http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run()
