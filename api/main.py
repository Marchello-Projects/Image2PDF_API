from fastapi import FastAPI

app = FastAPI(
    title="Image2PDF API",
    description="Image2PDF API - A backend service for converting JPG and PNG images to PDF in the background. Users can upload images, track conversion status, and download the resulting PDF files. The system uses FastAPI, PostgreSQL, Redis, worker-based processing, Nginx, and Docker.",
    contact={
        "name": "Marchello",
        "url": "https://github.com/Marchello-Projects",
        "email": "paskalovmarkus@gmail.com",
    },
)