terraform {
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_kinesis_stream" "demo_stream" {
  name             = "demo-event-stream"
  shard_count      = 1
  retention_period = 24
}
