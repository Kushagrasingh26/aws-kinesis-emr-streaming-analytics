# AWS Streaming Analytics Platform (Kinesis → EMR PySpark → Redshift)

This repo demonstrates a streaming analytics architecture:
- **Local Mode (runnable):** Simulated Kinesis → Spark Streaming → Parquet analytics
- **AWS Mode (optional):** Kinesis producer + EMR job skeleton + Redshift table DDL + Terraform

## Local Mode (Recommended)
### Run
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
mkdir outputs
