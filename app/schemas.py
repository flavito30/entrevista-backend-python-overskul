from pydantic import BaseModel ,Field ,field_validator
from datetime import date

class TaskBase (BaseModel) :
    title : str = Field(... , min_length=1 )
    description : str = Field(... , min_length=1 )
    completed : bool = Field(default=False)
    due_date : date 

    @field_validator("due_date")
    def validate_due_date(cls , v):
        if v < date.today():
            raise ValueError("La fecha de vencimiento no puede ser en el pasado")
        return v
    

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel) : 
    title : str | None = None
    description : str | None = None
    completed : bool | None = None
    due_date : date | None = None

class Task (TaskBase):
    id : int 

    class Config:
        from_attributes = True