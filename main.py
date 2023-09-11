from datetime import timedelta, datetime
from fastapi import FastAPI, HTTPException, Query, status,APIRouter
from fastapi.encoders import jsonable_encoder


app = FastAPI()

api_router = APIRouter(
    prefix = '/api',
    tags = ['GET METHOD']
)


#@app.get('/api', tags=['GET REQUEST'])
@api_router.get('/')
async def get_request(slack_name: str = Query(..., description="Your Slack name"),
    track: str = Query(..., description="Your chosen track")):

     # Get current day of the week
    current_day = datetime.utcnow().strftime('%A')

    # Get current UTC time
    current_time = datetime.utcnow()
    utc_time = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Validate UTC time within +/-2 minutes
    two_minutes_ago = current_time - timedelta(minutes=2)
    two_minutes_later = current_time + timedelta(minutes=2)
    if not (two_minutes_ago <= current_time <= two_minutes_later):
        raise HTTPException(status_code=400, detail="UTC time validation failed")

    # GitHub URLs
    github_file_url = "https://github.com/sneekywhite/get-request/blob/main/main.py"
    github_repo_url = "https://github.com/sneekywhite/get-request.git"
    status_code:int = status.HTTP_200_OK


    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": status_code
    }

    
    return (response)

    
