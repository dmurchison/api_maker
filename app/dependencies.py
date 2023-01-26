from fastapi import Response, HTTPException
import time



count = 0
start_time = time.time() # Silly bug, can you catch it?
reset_interval = 10
limit = 50

def rate_limit(response: Response) -> Response:
    global count, start_time

    if time.time() > start_time + reset_interval:
        count = 0
        start_time = time.time()
    if count >= limit:
        raise HTTPException(status_code=429, detail={"error": "Too Many Requests",
                                                    "timeout": round(start_time + reset_interval - time.time(), 2) + 0.01
                                                    })
    count += 1
    response.headers['X-App-RateLimit'] = f"{count}/{limit}"

    return Response
