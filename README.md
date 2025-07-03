### Simple Blog API with CRUD Operations
This Blog API is created with Django REST Framework

> [!NOTE]
> **This API uses MySQLClient Database which is used in Production Environment.**

> [!TIP]
> **If it doesn't work, you can use the the in-built SQLite3 Database from the Django Framework.**

> [!IMPORTANT]
> **It has JWT authentication so use Postman to test the API.**

### **Endpoints (In this Project):**
- To access the Django Administration page: ``` http://127.0.0.1:8000/admin/ ```
- To get all the Posts in the Blog API: ``` http://127.0.0.1:8000/api/post/ ```
- To retrieve specific Post with its id: ``` http://127.0.0.1:8000/api/post/<id>/ ```

- Go to the HTML Login Page: ``` http://127.0.0.1:8000/api/login/ ```
- To Register an user: ``` http://127.0.0.1:8000/auth/register/ ```
- To Login through DRF: ``` http://127.0.0.1:8000/auth/login/ ```
- To view User Details with JWT: ``` http://127.0.0.1:8000/auth/user/ ```
- To Generate JWT using Credentials: ``` http://127.0.0.1:8000/auth/token/ ```
- To Refresh the Access Token: ``` http://127.0.0.1:8000/auth/refresh/ ```
