from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Bảng trung gian cho quan hệ N:M
user_laboratory = Table(
    "user_laboratory", Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("lab_id", ForeignKey("laboratories.id"), primary_key=True)
)

user_medical_incident = Table(
    "user_medical_incident", Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("incident_id", ForeignKey("medical_incidents.id"), primary_key=True)
)

user_health_record = Table(
    "user_health_record", Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("record_id", ForeignKey("health_records.id"), primary_key=True)
)

user_neurology = Table(
    "user_neurology", Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("neuro_id", ForeignKey("neurologies.id"), primary_key=True)
)

user_quarantine = Table(
    "user_quarantine", Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("quarantine_id", ForeignKey("quarantines.id"), primary_key=True)
)

user_health_check = Table(
    "user_health_check", Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("check_id", ForeignKey("periodic_health_checks.id"), primary_key=True)
)


# Các Entity chính
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    role = Column(String)  # Student / Nurse / Teacher
    email = Column(String, unique=True)
    phone_number = Column(String)

    laboratories = relationship("Laboratory", secondary=user_laboratory, back_populates="users")
    medical_incidents = relationship("MedicalIncident", secondary=user_medical_incident, back_populates="users")
    health_records = relationship("HealthRecord", secondary=user_health_record, back_populates="users")
    neurologies = relationship("Neurology", secondary=user_neurology, back_populates="users")
    quarantines = relationship("Quarantine", secondary=user_quarantine, back_populates="users")
    health_checks = relationship("PeriodicHealthCheck", secondary=user_health_check, back_populates="users")


class Laboratory(Base):
    __tablename__ = "laboratories"
    id = Column(Integer, primary_key=True)
    test_type = Column(String)
    test_date = Column(Date)
    test_result = Column(String)

    users = relationship("User", secondary=user_laboratory, back_populates="laboratories")


class MedicalIncident(Base):
    __tablename__ = "medical_incidents"
    id = Column(Integer, primary_key=True)
    severity_level = Column(String)
    action_taken = Column(String)

    users = relationship("User", secondary=user_medical_incident, back_populates="medical_incidents")


class HealthRecord(Base):
    __tablename__ = "health_records"
    id = Column(Integer, primary_key=True)
    blood_type = Column(String)
    allergies = Column(String)
    chronic_diseases = Column(String)

    users = relationship("User", secondary=user_health_record, back_populates="health_records")


class Neurology(Base):
    __tablename__ = "neurologies"
    id = Column(Integer, primary_key=True)
    diagnosis = Column(String)
    symptoms = Column(String)
    treatment_plan = Column(String)

    users = relationship("User", secondary=user_neurology, back_populates="neurologies")


class Quarantine(Base):
    __tablename__ = "quarantines"
    id = Column(Integer, primary_key=True)
    reason_for_quarantine = Column(String)
    location = Column(String)
    health_status_during_quarantine = Column(String)
    supervisor = Column(String)
    bmi = Column(Float)

    users = relationship("User", secondary=user_quarantine, back_populates="quarantines")


class PeriodicHealthCheck(Base):
    __tablename__ = "periodic_health_checks"
    id = Column(Integer, primary_key=True)
    heart_rate = Column(Integer)

    users = relationship("User", secondary=user_health_check, back_populates="health_checks")
