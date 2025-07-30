### Task Overview

A customer engagement team at a SaaS company needs to notify users when their account information changes. The backend API is responsible for receiving notification requests and queuing email sends without making users wait, so that updates are as responsive as possible. Currently, notification tasks are not running as intended and users aren’t being informed promptly, affecting customer satisfaction and support workflows.

### Guidance

- Use FastAPI’s async programming features for non-blocking request handling
- Apply BackgroundTask or BackgroundTasks to ensure long-running tasks execute outside the request/response cycle
- Validate all input data using Pydantic models
- Use meaningful field validation to guarantee that all required information for notifications is present
- Avoid blocking or synchronous logic inside async endpoints or background tasks
- Separate request validation, background work, and database operations for clarity
- Follow sound architectural patterns and maintain clean code organization

### Objectives

- Implement an API endpoint that accepts user notification requests
- Configure the API so that sending the notification is performed asynchronously via a proper background task
- Ensure invalid requests are rejected with clear errors; valid requests should return promptly while the background task completes
- Use Pydantic for data modeling and validation of all incoming requests
- Demonstrate that the background operation does not block other API users or degrade main API response performance

### How to Verify

- Invoke the API endpoint with a valid notification payload and confirm that the response arrives immediately, not after the background work
- Confirm that the notification/tasks are actually executed after the request
- Test with multiple concurrent requests to ensure background tasks are correctly queued and handled without blocking
- Inspect FastAPI docs to see clear request/response models and endpoint behavior
- Review server logs to verify that background jobs are completed and not executed inline with the client response
