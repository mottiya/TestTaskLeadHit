from fastapi import FastAPI, Request, Response
from tinydb import TinyDB, Query

from utils import get_type_value

app = FastAPI(title="Test task LeadHit")
db = TinyDB('db.json')

@app.post("/get_form")
async def get_form(request: Request):
    form_data = await request.form()
    try:
        search_scheme = {f_k:get_type_value(f_v) for f_k, f_v in form_data.items()}
    except ValueError:
        return Response(status_code=400)
    db_result = db.get(Query().fields.test(lambda x: search_scheme.items() <= x.items()))
    if db_result is None:
        return search_scheme
    return db_result['name']