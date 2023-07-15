# Practice Mock application development API for jobs

## Requirements
For your practice tasks, we want you to make a set of endpoints for a "jobs" API.

For that set, please use /v1/jobs/ as the URL prefix. Please use ModelViewSet as the base class in views.py

End points:
- [ ] /v1/jobs/ - list all jobs
- [ ] /v1/jobs/<id>/ - detail API for a job
- [ ] /v1/jobs/<id>/apply/ - create an application for the job
- [ ] /v1/jobs/<id>/applications/ - list of applications for a job
- [ ] /v1/jobs/<job_id>/applications/<application_id>/accept/ - sets the status of the job application as "accepted". Only the creator of the job can do this
- [ ] /v1/jobs/<job_id>/applications/<application_id>/decline/ - sets the status of the job application as "declined". Only the creator of the job can do this
- [ ] /v1/jobs/<job_id>/applications/<application_id>/withdraw/ - sets the status of the job application as "withdrawn". Only the creator of the application can do this

Models:
- Jobs:
    - [x] should reside in jobs/models.py
    - [x] should have an owner field that's a foreign key to django.contrib.auth.models.User
    - [x] should have a created and modified timestamp
- Applications:
    - [x] should reside in applications/models.py
    - [x] should have an owner field that's a foreign key to django.contrib.auth.models.User
    - [x] should have a created and modified timestamp

# Running

Install the required dependencies `pip-sync requirements/base.txt`.

Make sure to create an `.env` on `./silkroad/` directory.
```
SECRET_KEY=<secret key>
DB_NAME=<database name>
DB_USER=<username>
DB_PASSWORD=<user password>
```

Start the server by running `python manage.py runserver`.
