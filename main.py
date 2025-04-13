#remenber this file is not working on len cable

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from APIs.databaseconnection import *
from APIs import models, dependencies
from datetime import date

app=FastAPI()

@app.get("/student/{student_id}")
async def get_student_info(student_id: int, db: Session = Depends(dependencies.get_db)):
    try:
        student = db.query(models.studentinfo).filter(models.studentinfo.id == student_id).first()
        if student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        return {"id": student.id, "name": student.name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")


@app.get('/request-outpass/')
async def requestoutpass(student_id:int,purpose:str,db: Session = Depends(dependencies.get_db)):
    student=db.query(models.studentinfo).filter(models.studentinfo.id==student_id).first()
    if student is None:
        raise HTTPException(status_code=404,detail="user not found")
    outpass=models.outpassrequest(
        student_id=student.id,
        name = student.name,
        rollnumber = student.rollnumber,
        department = student.department,
        hostel = student.hostel,
        mobilenumber = student.mobilenumber,
        purpose = purpose
    )

    db.add(outpass)
    db.commit()
    db.refresh(outpass)
    return {"message": "Outpass request submitted successfully", "outpass_id": outpass.id}


