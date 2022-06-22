from fastapi.routing import APIRouter
from src.models.teams import TeamIn_Pydantic, Team_Pydantic, Team
from typing import List

router = APIRouter()


@router.post("/team/", response_model=Team_Pydantic)
async def create_team(team: TeamIn_Pydantic):
    instance = await Team.create(**team.dict(exclude_unset=True))
    return await Team_Pydantic.from_tortoise_orm(instance)


@router.get("/team/", response_model=List[Team_Pydantic])
async def get_team_all() -> List[Team_Pydantic]:
    return await Team_Pydantic.from_queryset(Team.all())


@router.get("/team/{team_id}", response_model=Team_Pydantic)
async def get_team_id(team_id: int):
    return await Team_Pydantic.from_queryset_single(Team.get(id=team_id))


@router.put("/team/{team_id}/", response_model=Team_Pydantic)
async def update_team_id(team_id: int, team: TeamIn_Pydantic):
    await Team.filter(id=team_id).update(**team.dict())
    return await Team_Pydantic.from_queryset_single(Team.get(id=team_id))
