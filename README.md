### Blogs API

This is a FastAPI-based API for managing blogs and users. It provides endpoints for creating, retrieving, updating, and deleting blogs, as well as creating and retrieving users.
Installation

    Clone the repository:

    bash
```
git clone <https://github.com/mishrarohit10/blogAPI>
```
### Install the required dependencies:
```
    pip install -r requirements.txt
```
### Usage

    Run the API server:

```
    uvicorn main:app --reload
```
    Open your web browser and navigate to http://localhost:8000/docs to access the Swagger UI. This interactive documentation provides detailed information about the available endpoints and allows you to make requests directly.

### Endpoints
### Blog Endpoints

    POST /blog - Create a new blog.
    GET /get - Retrieve all blogs.
    GET /getby/{id} - Retrieve a specific blog by ID.
    DELETE /blogs/delete/{id} - Delete a blog by ID.
    PUT /blog/{id} - Update a blog by ID.

### User Endpoints

    POST /user - Create a new user.
    GET /user/{id} - Retrieve a user by ID.

### Database

This API uses a SQL database to store blogs and users. The database connection details can be configured in the blogs/database.py file.

### Security

The API uses password hashing to securely store user passwords. The hashing functionality is implemented in the blogs/hashing.py module.

### Contributing

Contributions are welcome! If you find any issues or would like to suggest improvements, please open an issue or submit a pull request.