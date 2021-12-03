**Priority App**

Task app that lists items based on priority 

Link to IOS repo:

The purpose of Priority is to serve as an organization tool for the user to keep track of their tasks in the order of importance. Our app will list the items with highest priority on the top, and users will also be able to assign and sort tasks by category.

On the backend, we have implemented four routes. Our first route sends a GET request to return all tasks in all categories. Our second route sends a GET request to return all tasks in a specific category. Our third route is a POST request to create new categories, so that the user will be able to assign tasks to these categories. Our fourth route is a POST request to create a new task. Our backend features two tables, one for tasks and one for categories, resembling a one to many relationship since one category can have many tasks but not vice versa. The tables have a relationship.

Priority API Specification: 
https://docs.google.com/document/d/112-BYZ5Ro5D_mL_vEN7zJn1PnrT2CnW8jg4pdVKehDw/edit?usp=sharing

http://anneshghoshdastidarpriority.herokuapp.com/
