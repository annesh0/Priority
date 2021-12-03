**Priority App**

Task app that lists items based on priority 

Link to IOS repo:

The purpose of Priority is to serve as an organization tool for the user to keep track of their tasks in the order of importance. Our app will list the items with highest priority on the top, and users will also be able to assign and sort tasks by category.

On the backend, we have implemented four routes. Our first route sends a GET request to return all tasks in all categories. Our second route sends a GET request to return all tasks in a specific category. Our third route is a POST request to create new categories, so that the user will be able to assign tasks to these categories. Our fourth route is a POST request to create a new task. Our backend features two tables, one for tasks and one for categories, resembling a one to many relationship since one category can have many tasks but not vice versa. The tables have a relationship.

API Specification

Values wrapped in < > are placeholders for what the field values should be.

Expected Functionality
Get all tasks for all categories
GET /api/categories/

Response: 
<HTTP STATUS CODE 200>
[
        {
            "id" 1,
            "category": "housework",
            "tasks": [
                           {‘id’: 1, ‘name’: ‘Do Laundry’, ‘description’: ‘Separate colors and whites’, ‘priority’: false, ‘username_id’: 1}
]
        },
        {
            "id": 2,
            "category": "schoolwork",
            "tasks": [
                           {‘id’: 2, ‘name’: ‘Spanish HW’, ‘description’: ‘Daily reading and responses’, ‘priority’: true, ‘username_id’: 2}, 
                {‘id’: 3, ‘name’: ‘Math HW’, ‘description’: ‘5 questions’, ‘priority’: false, ‘username_id’: 2}
]
        },
        ...
 ]


Get Tasks of Specific Category
GET /api/category/<int:category_id>/
Response: 

<HTTP STATUS CODE 200>

Response: 

{
    "id": 2,
    "category": "schoolwork",
    "tasks": [
                  {‘id’: 2, ‘name’: ‘Spanish HW’, ‘description’: ‘Daily reading and responses’, ‘priority’: true, ‘username_id’: 2}, 
      {‘id’: 3, ‘name’: ‘Math HW’, ‘description’: ‘5 questions’, ‘priority’: false, ‘username_id’: 2}
]
}


Create Category
POST /api/category/

Request:
{
    ‘category’: ‘misc’’
}

Response: 
<HTTP STATUS CODE 201>

{
    'id': 3,
    'category’': ‘misc’,
}


Create a task
POST /api/<int:category_id>/tasks/

Request: 
{
    "name": "Walk the Dog",
    "description": ‘Walk him for one mile’,
    “priority”: false
}
Response: 
<HTTP STATUS CODE 201>

{
    “id”: 4,
    “name”: “Walk the Dog”,
    “description”: ‘Walk him for one mile’,
    “priority”: false
    “category_id”: 2
}

http://anneshghoshdastidarpriority.herokuapp.com/
