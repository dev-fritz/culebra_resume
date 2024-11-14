from fastapi import FastAPI
from culebra_resume.endpoints import endpoints

app = FastAPI()
app.include_router(endpoints.include_routes)

import sys
print(sys.path)
