# Rest api test task

    Brief

We need an api for tracking empoyees in multiple organizations. Each `organization` has name and departments. `Departments` have names and employees. `Employees` have basic personal information and status. Status is basically a role of an employee inside that department (e.g. manager, developer, boss, etc). To change status title(e.g. 'manager') to a different one (e.g. 'Human resources manager') I should update `Status` entity and see updated value for all employees that are related to this entity.

### When I get organizations list I want to receive:

- all organization fields
- departments count
- total employees count

### Departments:

- all dep. fields
- total count
- total employees count for each department

### Employee:

- all fields

>

    Objectives (milestones/steps)

- Set up Postgresql/MySql database
- Create Models
- Create simple api
  - Serializers
  - Views
  - Urls
- Add filters ond ordering
- Set up user models
  - user model has (id, name, email, [...any neccessary]) fields
    (employee != user)
  - passwordless login:
    - user sends post request with email address
    - email with sign in token is sent to user
    - token is valid and is connected to user
- authorization
- permissions
  >
      HOW TO
- pipenv shell
- pipenv install
- cd main
- ./manage.py runserver
>
working folder is `api`
