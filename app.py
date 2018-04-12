"""
probe
"""
import asyncio
from sanic import Sanic, response


HTTP_CODES = {
    100: "Continue",
    101: "Switching Protocols",
    102: "Processing",
    103: "Checkpoint/Early Hints",
    200: "OK",
    201: "Created",
    202: "Accepts",
    203: "Non-Authoritative Information",
    204: "No Content",
    205: "Reset Content",
    206: "Partial Content",
    207: "Multi-Status",
    208: "Already Reported",
    300: "Moved Permanently",
    302: "Found",
    303: "See Other",
    304: "Not Modified",
    305: "Use Proxy",
    306: "Switch Proxy",
    307: "Temporary Redirect",
    308: "Permanent Redirect",
    400: "Bad Request",
    401: "Unauthorized",
    402: "Payment Required",
    403: "Forbidden",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    407: "Conflict",
    408: "Request Time-out",
    409: "Conflict",
    410: "Gone",
    411: "Length Required",
    412: "Precondition Failed",
    413: "Payload Too Large",
    414: "URI Too Long",
    415: "Unsupported Media Type",
    416: "Range Not Satisfiable",
    417: "Expectation Failed",
    418: "I'm a teapot",
    419: "I'm a fox",
    420: "Method Failure",
    421: "Misdirected Request",
    422: "Unprocessable Entity",
    423: "Locked",
    424: "Failed Dependency",
    426: "Upgrade Required",
    428: "Precondition Required",
    429: "Too Many Requests",
    431: "Request Header Fields Too Large",
    440: "Login Time-out",
    444: "No Response/nginx",
    449: "Retry With",
    450: "Blocked by Windows Parental Controls Microsoft]",
    451: "Unavailable For Legal Reasons",
    495: "SSL Certificate Error/nginx",
    496: "SSL Certificate Required/nginx",
    497: "HTTP Request Sent to HTTPS Port/nginx",
    498: "Invalid Token Esri]",
    499: "Client Closed Request/nginx",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Time-out",
    505: "HTTP Version Not Supported",
    506: "Variant Also Negotiates",
    507: "Insufficient Storage",
    508: "Loop Detected",
    509: "Bandwidth Limit Exceeded Apache Web Server/cPanel]",
    510: "Not Extended",
    511: "Network Authentication Required",
    520: "Unknown Error/Cloudflare",
    521: "Web Server Is Down/Cloudflare",
    522: "Connection Timed Out/Cloudflare",
    523: "Origin Is Unreachable/Cloudflare",
    524: "A Timeout Occurred/Cloudflare",
    525: "SSL Handshake Failed/Cloudflare",
    526: "Invalid SSL Certificate/Cloudflare",
    527: "Railgun Error/Cloudflare",
    530: "Site is frozen",
    598: "Network read timeout error",
    599: "Network connect timeout error",
}

app = Sanic()

@app.route("/ping")
async def ping(_):
    """
    healthcheck
    """
    return response.json({"status": "ok"})

@app.route("/status/<status_code:int>")
async def status(request, status_code):
    """
    Custom status_code response
    """
    if int(status_code) not in HTTP_CODES:
        return response.text("Not found", status=404)

    return response.text(HTTP_CODES[status_code], status=status_code)

@app.route("/delay/<delay_sec:int>")
async def delay(request, delay_sec):
    """
    Custom delay response
    """
    await asyncio.sleep(delay_sec)
    return response.json({"status": "ok", "delay": delay_sec})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, access_log=False)
