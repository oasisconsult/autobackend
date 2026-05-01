from fastapi import FastAPI
from app.api.routes import generation, projects, billing, health


from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import setup_logging
from app.middleware.enforcement import EnforcementMiddleware
from app.middleware.fraud_middleware import FraudMiddleware
from slowapi.middleware import SlowAPIMiddleware
from app.core.rate_limit import limiter
from app.core.exceptions import global_exception_handler

# Routers (added later)
# from app.api.routes import generation, projects

setup_logging()


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": settings.APP_NAME
    }

app = FastAPI(title="AutoBackend")


app.add_exception_handler(Exception, global_exception_handler)
app.middleware("http")(EnforcementMiddleware())
app.middleware("http")(FraudMiddleware())


app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

app.include_router(generation.router, prefix="/generation")
app.include_router(projects.router, prefix="/projects")
app.include_router(billing.router, prefix="/billing")
app.include_router(health.router, prefix="/health")

# app.include_router(generation.router, prefix="/generation")
# app.include_router(projects.router, prefix="/projects")