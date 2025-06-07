from src.models import AppProjectDTO, AppProjectModel
from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories import AppProjectRepo


class CreateAppProjectController:
    @staticmethod
    async def handler(
        session: AsyncSession,
        app_project: AppProjectDTO,
    ) -> AppProjectDTO:
        """
        Handle creating a project.

        :param app_project: The project data to create.
        :param session: The database session.
        :return: The created AppProjectDTO.
        """

        app_project_model = AppProjectModel(**app_project.model_dump())
        app_project_model = await AppProjectRepo.create_project(
            session, app_project_model
        )
        app_project_dto = AppProjectDTO.model_validate(app_project_model)
        return app_project_dto
