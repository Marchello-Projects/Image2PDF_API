from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
from database.models import Taskstatus

class TaskBaseResponse(BaseModel):
    id: int = Field(..., examples=[1])
    source_filename: str = Field(..., examples=['photo.jpg'])
    status: str = Field(..., examples=["pending"])
    created_at: datetime = Field(..., examples=["2026-04-13T10:00:00"])

    model_config = ConfigDict(from_attributes=True)

class TaskCreateResponse(TaskBaseResponse):
    pass

class TaskListItemResponse(TaskBaseResponse):
    pass

class TaskDetailResponse(BaseModel):
    id: int = Field(..., examples=[1])
    source_filename: str = Field(..., examples=["photo.jpg"])
    status: Taskstatus = Field(..., examples=["done"])
    result_path: Optional[str] = Field(default=None, examples=["results/task_1.pdf"])
    download_url: Optional[str] = Field(default=None, examples=["/tasks/1/download"])
    error_message: Optional[str] = Field(default=None, examples=[None])
    created_at: datetime = Field(..., examples=["2026-04-13T10:00:00"])
    processed_at: Optional[datetime] = Field(default=None, examples=["2026-04-13T10:00:12"])

    model_config = ConfigDict(from_attributes=True)

class TaskDeleteResponse(BaseModel):
    message: str = Field(..., examples=["Task deleted"])

class MessageResponse(BaseModel):
    message: str = Field(..., examples=["OK"])

class TaskLogResponse(BaseModel):
    id: int = Field(..., examples=[1])
    task_id: int = Field(..., examples=[1])
    message: str = Field(..., examples=["Task added to Redis queue"])
    created_at: datetime = Field(..., examples=["2026-04-13T10:00:02"])

    model_config = ConfigDict(from_attributes=True)