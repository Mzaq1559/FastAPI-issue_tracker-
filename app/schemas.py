from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional

class IssueStatus(str, Enum):
    open = "open"
    inProgress = "inProgress"
    closed = "closed"

class IssuePriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class IssueCreate(BaseModel):
    Title: str = Field (min_length=3, max_length=100)
    Description: str = Field (min_length=5, max_length=1000A)
    Priority: IssuePriority = IssuePriority.medium

class IssueUpdate(BaseModel):
    Title: Optional[str] = Field (default=None, max_length=100)
    Description: Optional[str] = Field (default=None, max_length=1000)
    Priority: Optional[IssuePriority] = None
    Status: Optional[IssueStatus] = None

class IssueOut(BaseModel):
     id: str
     Title: str
     Description: str
     Priority: IssuePriority
     Status: IssueStatus