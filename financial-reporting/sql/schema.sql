-- Minimal schema for dev
CREATE TABLE IF NOT EXISTS companies (
  id SERIAL PRIMARY KEY,
  ticker TEXT UNIQUE NOT NULL,
  name TEXT,
  sector TEXT,
  country TEXT
);

CREATE TABLE IF NOT EXISTS raw_files (
  id SERIAL PRIMARY KEY,
  filename TEXT NOT NULL,
  source TEXT,
  company_ticker TEXT,
  fetched_at TIMESTAMP DEFAULT now(),
  file_path TEXT NOT NULL,
  file_hash TEXT,
  UNIQUE(file_hash)
);

CREATE TABLE IF NOT EXISTS financial_statements (
  id SERIAL PRIMARY KEY,
  company_id INTEGER REFERENCES companies(id),
  report_date DATE,
  statement_type TEXT,
  data JSONB,
  source TEXT,
  ingested_at TIMESTAMP DEFAULT now(),
  UNIQUE(company_id, report_date, statement_type)
);

CREATE TABLE IF NOT EXISTS stock_prices (
  id SERIAL PRIMARY KEY,
  company_id INTEGER REFERENCES companies(id),
  date DATE NOT NULL,
  open NUMERIC, high NUMERIC, low NUMERIC, close NUMERIC, adj_close NUMERIC, volume BIGINT,
  UNIQUE(company_id, date)
);

CREATE TABLE IF NOT EXISTS metrics (
  id SERIAL PRIMARY KEY,
  company_id INTEGER REFERENCES companies(id),
  metric_date DATE,
  metric_name TEXT,
  value NUMERIC,
  UNIQUE(company_id, metric_date, metric_name)
);
