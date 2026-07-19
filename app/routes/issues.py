from fastapi import APIRouter

router = APIRouter(prefix = "/issues", tags = ["issues"])

@router.get("/")
def get_issues():
    return []