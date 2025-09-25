from sqlalchemy import (Column, Integer, Text, Date, Numeric, BigInteger,
                        JSON, TIMESTAMP, UniqueConstraint, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    ticker = Column(Text, unique=True, nullable=False)
    name = Column(Text)
    sector = Column(Text)
    country = Column(Text)

class RawFile(Base):
    __tablename__ = "raw_files"
    id = Column(Integer, primary_key=True)
    filename = Column(Text, nullable=False)
    source = Column(Text)
    company_ticker = Column(Text)
    fetched_at = Column(TIMESTAMP, server_default=func.now())
    file_path = Column(Text, nullable=False)
    file_hash = Column(Text, unique=True)

class FinancialStatement(Base):
    __tablename__ = "financial_statements"
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    report_date = Column(Date)
    statement_type = Column(Text)
    data = Column(JSON)
    source = Column(Text)
    ingested_at = Column(TIMESTAMP, server_default=func.now())
    __table_args__ = (UniqueConstraint("company_id", "report_date", "statement_type"),)

class StockPrice(Base):
    __tablename__ = "stock_prices"
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    date = Column(Date, nullable=False)
    open = Column(Numeric)
    high = Column(Numeric)
    low = Column(Numeric)
    close = Column(Numeric)
    adj_close = Column(Numeric)
    volume = Column(BigInteger)
    __table_args__ = (UniqueConstraint("company_id", "date"),)

class Metric(Base):
    __tablename__ = "metrics"
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    metric_date = Column(Date)
    metric_name = Column(Text)
    value = Column(Numeric)
    __table_args__ = (UniqueConstraint("company_id", "metric_date", "metric_name"),)
