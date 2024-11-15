from sqlmodel import create_engine, SQLModel
from culebra_resume.models import education_model, experience_model, hability_model, resume_model, transaction_model, user_model

engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/resume", echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)
    print("Tabelas criadas ou verificadas com sucesso.")

init_db()