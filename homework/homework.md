# Homework: Extend the Item-App

## Task Description

You are required to extend the existing Item-App by adding a new database table and implementing CRUD operations for it. The new table will be named `Category`, and it will allow users to categorize items in the application.

### 1. Add a New Database Table
- Create a new database table named `Category` with the following fields:
    - `id`: Primary key (integer).
    - `name`: Name of the category (string).
    - `description`: Description of the category (string).
- Add sample data to the `Category` table during app initialization.

### 2. Implement CRUD Operations for `Category`
- Add routes to perform the following operations:
    - **Create**: Add a new category.
    - **Read**: Retrieve all categories or a specific category by ID.
    - **Update**: Modify an existing category.
    - **Delete**: Remove a category by ID.

### 3. Redeploy the Application
- Update the application code to include the new table and routes.
- Build a new Docker image for the updated app and push it to DockerHub.
- Update the Kubernetes deployment to use the new image.
- Verify the app is working with the new functionality.

### 4. Extra: Add an Ingress Controller
- Configure an ingress controller to expose the application at the path `/myapp`.

#### Steps:
1. Create an Ingress resource:
   ```yaml
   apiVersion: networking.k8s.io/v1
   kind: Ingress
   metadata:
     name: item-app-ingress
     annotations:
       nginx.ingress.kubernetes.io/rewrite-target: /
   spec:
     rules:
     - http:
         paths:
         - path: /myapp
           pathType: Prefix
           backend:
             service:
               name: item-app-service
               port:
                 number: 80
    ```