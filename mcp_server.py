import sys
import json
from client import Quadtree

qt = Quadtree((0, 0, 1000, 1000), capacity=4)

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "quadtree_insert",
                        "description": "Insert 2D points into Quadtree spatial partition",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "points": {
                                    "type": "array",
                                    "items": {"type": "array", "items": {"type": "number"}}
                                }
                            },
                            "required": ["points"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "quadtree_insert":
            pts = [tuple(p) for p in args["points"]]
            results = [qt.insert(p) for p in pts]
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"inserted": all(results), "divided": qt.divided})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
