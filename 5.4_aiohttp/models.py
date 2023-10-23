from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine(URI)
Session = sessionmaker(bind=engine)


class Advertisement(Base):
    __tablename__ = 'advertisements'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)


description = db.Column(db.String(1000), nullable=False)
created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
owner = db.Column(db.String(50), nullable=False)

aiohttp_jinja2.template('index.html')


async def index_page():
    return {}
