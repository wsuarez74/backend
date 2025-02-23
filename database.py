from sqlalchemy import create_engine, MetaData
import os
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://wsuarez:Afsmnz78@mimysqlserver.mysql.database.azure.com:3306/ventas_db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata = MetaData()