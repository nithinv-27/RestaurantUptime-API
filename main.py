from fastapi import FastAPI
from schemas import report_output

app = FastAPI()

@app.get("/")
def home():
    return {"succ":"ess"}

@app.post("/trigger_report")
def report_gen():
    # This will trigger report generation for each store_id and returns a report_id (random string)
    ...

@app.get("/get_report", response_class=report_output)
def report(id:str):
    # The report_id from /trigger_report will be used to get the report (in report_output schema) if generated or running if not.
    ...