# Dataflow Architecture
## Overview
The dataflow architecture for skill-scribe is designed to handle the ingestion, processing, storage, and querying of coding skills analysis data. The system will utilize AI to provide personalized feedback and suggestions for developers.

## External Data Sources
* GitHub API
* GitLab API
* Bitbucket API
* User input (coding skills data)

## Ingestion Layer
```
  +---------------+
  |  GitHub API  |
  +---------------+
           |
           |
           v
  +---------------+
  | GitLab API  |
  +---------------+
           |
           |
           v
  +---------------+
  | Bitbucket API|
  +---------------+
           |
           |
           v
  +---------------+
  |  User Input  |
  +---------------+
           |
           |
           v
  +---------------+
  |  Ingestion   |
  |  Service     |
  +---------------+
```
* Components:
  + GitHub API connector
  + GitLab API connector
  + Bitbucket API connector
  + User input API
  + Ingestion service (responsible for handling API requests and user input)

## Processing/Transform Layer
```
  +---------------+
  | Ingestion    |
  |  Service     |
  +---------------+
           |
           |
           v
  +---------------+
  |  AI Engine  |
  +---------------+
           |
           |
           v
  +---------------+
  |  Data       |
  |  Transformer|
  +---------------+
           |
           |
           v
  +---------------+
  |  Processing  |
  |  Service     |
  +---------------+
```
* Components:
  + AI engine (responsible for analyzing coding skills data and providing personalized feedback)
  + Data transformer (responsible for transforming raw data into a suitable format for analysis)
  + Processing service (responsible for handling data processing tasks)

## Storage Tier
```
  +---------------+
  |  Processing  |
  |  Service     |
  +---------------+
           |
           |
           v
  +---------------+
  |  Database    |
  +---------------+
           |
           |
           v
  +---------------+
  |  Data Warehouse|
  +---------------+
```
* Components:
  + Database (responsible for storing raw data)
  + Data warehouse (responsible for storing transformed data)

## Query/Serving Layer
```
  +---------------+
  |  Database    |
  +---------------+
           |
           |
           v
  +---------------+
  |  Query Service|
  +---------------+
           |
           |
           v
  +---------------+
  |  API Gateway |
  +---------------+
```
* Components:
  + Query service (responsible for handling database queries)
  + API gateway (responsible for handling API requests and routing them to the query service)

## Egress to User
```
  +---------------+
  |  API Gateway |
  +---------------+
           |
           |
           v
  +---------------+
  |  User Interface|
  +---------------+
```
* Components:
  + User interface (responsible for displaying personalized feedback and suggestions to the user)

## Auth Boundaries
* Ingestion layer: API keys and OAuth tokens for GitHub, GitLab, and Bitbucket APIs
* Processing/transform layer: internal auth tokens for AI engine and data transformer
* Storage tier: database credentials and access controls
* Query/serving layer: API keys and OAuth tokens for API gateway
* Egress to user: user authentication and authorization for user interface

Note: The auth boundaries are designed to ensure secure access to the system and protect sensitive data.