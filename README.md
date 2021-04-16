# Elenas test

To build and deploy your application for the first time, run the following in your shell:

```bash
docker-compose build
```
if port 5432 is used:
```bash
sudo lsof -i :5432
sudo kill -9 <pid>
```
## Run Docker
```bash
docker-compose up
```
make migrations:

```bash
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
```

Create super user:
```bash
docker-compose run web python manage.py createsuperuser
```

rebuild:
```bash
docker-compose up -d --build
```

## QUERIES AND MUTATIONS


Create user
```bash
mutation CreateUser($name:String!, $password: String!, $username: String!){
  createUser(name: $name, password: $password, username: $username){
    user{ username, firstName }
  }
}
```
Auth User
```bash
mutation TokenAuth($username: String!, $password: String!) {
  tokenAuth(username: $username, password: $password) {
    token
    payload
    refreshExpiresIn
  }
}
```

Create Task
```bash
mutation CreateTask($title:String!, $description:String!){
  createTask(title: $title, description:$description){
    task{title, description, startDate}
  }
}
```

Task by User
```bash
query TaskByUser($page:Int!){
  taskByUser(page: $page){
    page
    pages
    objects{title}
  }
}
```

Update Task
```bash
Fiels to update: title, end_date, description, state
is_delete = True to delete a task

mutation UpdateTask($id: Int!, $end_date: Date ){
  updateTask(id: $id, endDate: $end_date )
  { 
    task {title, endDate, startDate} 
  }
}
```

Search task by description
```bash
query TaskByDescription($text: String!){
  taskByDescription(text: $text){
    title, description
  }
}
```

## Run unit test
```bash
docker-compose run web pytest
```