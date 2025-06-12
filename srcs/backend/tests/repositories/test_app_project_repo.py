import pytest
import conftest

from unittest.mock import patch, MagicMock

from src.repositories import AppProjectRepo
from src.models import AppProjectModel

def _assert_list_projects(result_list):
        assert isinstance(result_list, list)
        assert any(result_list)
        assert all(isinstance(result, AppProjectModel) for result in result_list)

@pytest.mark.asyncio(loop_scope="session")
async def test_MOCK_list_projects(session):

    # PROCEDURE
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = conftest.create_random_app_project_list()
    
    with patch("sqlalchemy.ext.asyncio.AsyncSession.execute", return_value=mock_result):
        result_list = await AppProjectRepo.list_projects(session)
        _assert_list_projects(result_list)

@pytest.mark.asyncio(loop_scope="session")
async def test_REAL_list_projects(session):

    # REQUISITES
    random_app_project = conftest.create_random_app_project()
    created_project = await AppProjectRepo.create_project(session, random_app_project)

    # PROCEDURE
    result_list = await AppProjectRepo.list_projects(session)
    _assert_list_projects(result_list)

    # CLEAN-UP
    await AppProjectRepo.delete_project(session, created_project.id)