# Tech Spec
## Stack
* Language: Python 3.10
* Framework: FastAPI 0.92.0
* Runtime: uvicorn 0.20.0
* Database: PostgreSQL 14.5
* AI Library: transformers 4.24.0

## Hosting
* Platform: AWS (free tier)
* Services:
	+ API Gateway: AWS API Gateway
	+ Compute: AWS Lambda
	+ Database: AWS RDS (PostgreSQL)
	+ Storage: AWS S3
* Alternative platforms:
	+ Google Cloud Platform (GCP)
	+ Microsoft Azure

## Data Model
### Tables/Collections
#### Users
* `id` (primary key, UUID): unique user identifier
* `username`: username chosen by the user
* `email`: user's email address
* `password_hash`: hashed password for the user
#### Coding Skills
* `id` (primary key, UUID): unique coding skill identifier
* `user_id` (foreign key): reference to the user who owns the coding skill
* `skill_name`: name of the coding skill (e.g., Python, Java, etc.)
* `skill_level`: level of proficiency in the coding skill (e.g., beginner, intermediate, advanced)
#### Code Submissions
* `id` (primary key, UUID): unique code submission identifier
* `user_id` (foreign key): reference to the user who submitted the code
* `code`: the submitted code
* `skill_id` (foreign key): reference to the coding skill being assessed
* `feedback`: AI-generated feedback for the submitted code
#### Feedback
* `id` (primary key, UUID): unique feedback identifier
* `code_submission_id` (foreign key): reference to the code submission that generated the feedback
* `feedback_text`: text of the feedback

## API Surface
### Endpoints
1. **POST /users**: create a new user
	* Method: POST
	* Path: /users
	* Purpose: create a new user account
	* Request Body: `username`, `email`, `password`
2. **GET /users/{user_id}**: retrieve a user's profile
	* Method: GET
	* Path: /users/{user_id}
	* Purpose: retrieve a user's profile information
	* Response: `username`, `email`
3. **POST /code-submissions**: submit code for assessment
	* Method: POST
	* Path: /code-submissions
	* Purpose: submit code for assessment and feedback
	* Request Body: `code`, `skill_id`
4. **GET /code-submissions/{code_submission_id}**: retrieve a code submission's feedback
	* Method: GET
	* Path: /code-submissions/{code_submission_id}
	* Purpose: retrieve the feedback for a submitted code
	* Response: `feedback_text`
5. **GET /coding-skills**: retrieve a list of coding skills
	* Method: GET
	* Path: /coding-skills
	* Purpose: retrieve a list of available coding skills
	* Response: `skill_name`, `skill_level`
6. **POST /coding-skills**: create a new coding skill
	* Method: POST
	* Path: /coding-skills
	* Purpose: create a new coding skill
	* Request Body: `skill_name`, `skill_level`
7. **GET /users/{user_id}/coding-skills**: retrieve a user's coding skills
	* Method: GET
	* Path: /users/{user_id}/coding-skills
	* Purpose: retrieve a list of coding skills for a user
	* Response: `skill_name`, `skill_level`
8. **PUT /users/{user_id}/coding-skills/{skill_id}**: update a user's coding skill level
	* Method: PUT
	* Path: /users/{user_id}/coding-skills/{skill_id}
	* Purpose: update a user's coding skill level
	* Request Body: `skill_level`

## Security Model
* Authentication: JSON Web Tokens (JWT)
* Authorization: role-based access control (RBAC)
* Secrets Management: AWS Secrets Manager
* IAM: AWS IAM roles and policies

## Observability
* Logging: AWS CloudWatch Logs
* Metrics: AWS CloudWatch Metrics
* Tracing: AWS X-Ray

## Build/CI
* Build Tool: GitHub Actions
* CI Pipeline:
	1. Build and test the application
	2. Deploy to AWS
	3. Run integration tests
* CD Pipeline:
	1. Monitor application performance and logs
	2. Automatically deploy updates to AWS