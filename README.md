# Your Project Title Here
by {{ NAME }}
She Codes crowdfunding project - DRF Backend.

## About
Encourages children to reach goals by posting a goal and people pledge money towards their goal. The goal may not be financial - it may be to get certain grades, for example. 
Set the goal - and parents can post money towards it (eg in return for chores?) or gifts for birthdays also, they can also create a Giving pot; 
Chore Lists - children can do chores to earn money.
Help children reach their savings goals. 

Competitors/Inspiration: Rooster money app; Hyperjar; Spriggy. Barefoot Investor. 

## Features
{{ The features your MVP will include. (Remember this is a working document, you can change these as you go!) }}
* [] log in 
make project
edit project
delete project
make pledge
* [] group permissions - projects are private except in group

### Stretch Goals
{{ Outline three features that will be your stretch goals if you finish your MVP }}
* chore incentives - extra pledges when chores completed
* responsible citizenship - % put aside for charity 
* goal completion tracker (days to birthday / progress)

* [] Stretch goal one
* [] Stretch goal two
* [] Stretch goal three

## API Specification

| HTTP Method | Url | Purpose | Request Body | Successful Response Code | Authentication <br /> Authorization
| --- | ------- | ------ | ---- | -----| ----|
| GET | projects/ | Return all projects | N/A | 200 | N/A |
| POST | projects/ | Create a new project | project object | 201 | User must be logged in. |

## Database Schema
{{ Insert your database schema }}

![image info goes here](./docs/image.png)

## Wireframes
{{ Insert your wireframes }}

![image info goes here](./docs/image.png)

## Colour Scheme
{{ Insert your colour scheme }}

![image info goes here](./docs/image.png)

## Fonts
{{ outline your heading & body font(s) }}

## Submission Documentation
{{ Fill this section out for submission }}

Deployed Project: [Deployed website](http://linkhere.com/)

### How To Run
{{ What steps to take to run this code }}

### Updated Database Schema
{{ Updated schema }}

![image info goes here](./docs/image.png)

### Updated Wireframes
{{  Updated wireframes }}

![image info goes here](./docs/image.png)

### How To Register a New User
{{ Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data). }}

### Screenshots
* [] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
![image info goes here](./docs/image.png)

* [] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
![image info goes here](./docs/image.png)

* [] A screenshot of Insomnia, demonstrating a token being returned.
![image info goes here](./docs/image.png)