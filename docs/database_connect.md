## Using Database Data in the Framework

To use data from a database within the framework, you **must** have a `.env` file located in your current working directory. This file should contain the necessary configuration variables for database connection.

### Required `.env` Variables

Below is an example of the essential variables your `.env` file should include:


```env
DB_HOST=your_db_host
DB_PORT=your_db_port
DB_NAME=your_db_name
DB_USER=your_db_username
DB_PASSWORD=your_db_password
```

> **⚠️ Warning:**  
> The following SSH-related variables are **only required** if you are connecting to the database via an SSH tunnel.


```env
SSH_HOST=ssh_server
SSH_USER=ssh_user
SSH_KEY_PATH=path_to_your_key
```