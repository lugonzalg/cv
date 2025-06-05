from backend.router.routes import (
    ListAppProjectsRoute,
    CreateAppProjecRoute,
    GetAppProjectRoute,
    UpdateAppProjectRoute,
    DeleteAppProjectRoute,
)

app.include_router(ListAppProjectsRoute.router)
app.include_router(CreateAppProjecRoute.router)
app.include_router(GetAppProjectRoute.route)
app.include_router(UpdateAppProjectRoute.route)
app.include_router(DeleteAppProjectRoute.route)
