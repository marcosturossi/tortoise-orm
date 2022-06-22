from fastapi.routing import APIRouter
from src.models.teams import TeamIn_Pydantic, Team_Pydantic, Team

router = APIRouter()


@router.post("/team/", response_model=Team_Pydantic)
async def create_team(team: TeamIn_Pydantic):
    instance = await Team.create(**team.dict(exclude_unset=True))
    return await Team_Pydantic.from_tortoise_orm(instance)
