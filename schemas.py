from pydantic import BaseModel

class report_output(BaseModel):
    store_id:int
    uptime_last_hour:int #in min
    uptime_last_day:int #in hrs
    update_last_week:int #in hrs
    downtime_last_hour:int #in min
    downtime_last_day:int #in hrs
    downtime_last_week:int #in hrs