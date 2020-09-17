from app import create_app, db
from app.models import (
    Admin,
    Secretary,
    User,
    Consult,
    StatusConsult,
    Doctor,
    OccupationArea,
    Specialty,
    Patient,
    )

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Admin': Admin,
        'Secretary': Secretary,
        'User': ,
        'Consult': Consult,
        'StatusConsult': StatusConsult,
        'Doctor': Doctor,
        'OccupationArea': OccupationArea,
        'Specialty': Specialty,
        'Patient': Patient,
    }
