from fastapi import FastAPI

app = FastAPI()

todos = [{"id": 1, "task": "Integrasi Docker dan CI/CD"}]

@app.get("/tasks")
def get_tasks():
    return {"status": "healthy", "data": todos}
