from fastapi import FastAPI, BackgroundTasks, Depends, status
from app.schemas import NotificationRequest
from app.services import send_notification

app = FastAPI()

@app.post("/notify", status_code=status.HTTP_202_ACCEPTED)
async def notify_user(payload: NotificationRequest, background_tasks: BackgroundTasks = Depends()):
    pass
