from sqlalchemy import Column, Integer, String, Date
from APIs.databaseconnection import Base

#here is the information of the student if any change we want in info of student we want to store we can do here
class studentinfo(Base):
    __tablename__="student"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,index=True)
    rollnumber = Column(String,primary_key=True,index=True)
    department = Column(String)
    hostel = Column(String)
    mobilenumber = Column(String,primary_key=True,index=True)
    emailid = Column(String,primary_key=True,index=True)

class outpassrequest(Base):
    __tablename__="outpassrequest"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    rollnumber = Column(String)
    department = Column(String)
    hostel = Column(String)
    mobilenumber = Column(String)
    purpose = Column(String)




