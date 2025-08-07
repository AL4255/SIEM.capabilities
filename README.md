Splunk Demo Setup
A simple demonstration of Splunk's log analysis capabilities using Docker Compose to run both Splunk and a log generator.
Overview
This demo showcases basic Splunk functionality by:

Running Splunk in a Docker container
Running a log generator to create sample data
Demonstrating log ingestion and search capabilities

Quick Start
Prerequisites

Docker and Docker Compose installed
Basic familiarity with command line

Setup Steps

Create Docker Compose File
Create a docker-compose.yml file:
yamlversion: '3.8'

services:
  splunk:
    image: splunk/splunk:latest
    container_name: splunk-demo
    ports:
      - "8000:8000"
      - "9997:9997" 
      - "8088:8088"
      - "1514:1514"
    environment:
      - SPLUNK_START_ARGS=--accept-license
      - SPLUNK_PASSWORD=demo123456
    volumes:
      - splunk-data:/opt/splunk/var

  log-generator:
    image: your-log-generator-image
    container_name: log-generator
    depends_on:
      - splunk
    # Configure to send logs to splunk container

volumes:
  splunk-data:

Start the Demo Environment
bashdocker-compose up -d

Access Splunk Web Interface

Open browser to http://localhost:8000
Login: admin / demo123456


Verify Log Generation
Check that logs are being generated and ingested into Splunk

What You'll Demo

Log ingestion from the generator
Basic search queries and filtering
Simple dashboards and visualizations
Alert configuration basics

Cleanup
bashdocker-compose down -v
Perfect for showing off Splunk's core log management and analysis features with realistic data flow between containers.
