import pytest
import conftest

from unittest.mock import patch, MagicMock, AsyncMock

from src.repositories import AppProjectRepo
from src.models import AppProjectModel

def _assert_list_projects(result_list):
        assert isinstance(result_list, list)
        assert any(result_list)
        assert all(isinstance(result, AppProjectModel) for result in result_list)

@pytest.mark.asyncio(loop_scope="session")
async def test_MOCK_list_projects(mock_session):

    # SETUP MOCK
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = conftest.create_random_app_project_list()
    mock_session.execute.return_value = mock_result
    
    # PROCEDURE
    result_list = await AppProjectRepo.list_projects(mock_session)
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

def _assert_create_project(
        created_project: AppProjectModel, 
        random_app_project: AppProjectModel
    ):

    assert isinstance(created_project, AppProjectModel)
    assert created_project.name == random_app_project.name
    assert created_project.description == random_app_project.description
    assert created_project.skills == random_app_project.skills
    assert created_project.repo == random_app_project.repo

@pytest.mark.asyncio(loop_scope="session")
async def test_MOCK_create_project(mock_session):

    # REQUISITES
    random_app_project = conftest.create_random_app_project()

    # SETUP MOCK - make async methods return coroutines
    mock_session.add.return_value = None
    mock_session.commit = AsyncMock()
    mock_session.refresh = AsyncMock()

    # PROCEDURE
    created_project = await AppProjectRepo.create_project(mock_session, random_app_project)

    # ASSERTIONS
    _assert_create_project(created_project, random_app_project)
    mock_session.add.assert_called_once_with(random_app_project)
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once_with(random_app_project)

@pytest.mark.asyncio(loop_scope="session")
async def test_REAL_create_project(session):
    # REQUISITES
    random_app_project = conftest.create_random_app_project()

    # PROCEDURE
    created_project = await AppProjectRepo.create_project(session, random_app_project)

    # ASSERTIONS
    assert isinstance(created_project, AppProjectModel)
    assert created_project.name == random_app_project.name
    assert created_project.description == random_app_project.description
    assert created_project.skills == random_app_project.skills
    assert created_project.repo == random_app_project.repo

    # CLEAN-UP
    await AppProjectRepo.delete_project(session, created_project.id)