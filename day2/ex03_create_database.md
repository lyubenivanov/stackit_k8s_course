# Exercise 03: Create managed Database

## Create managed Postgres database instsance in STACKIT

```bash
stackit postgresflex instance create --name <NAME> --cpu 2 --ram 4 --acl 0.0.0.0/0
```

```bash
stackit postgresflex user create --instance-id <INSTANCE_ID> --username <PG_USERNAME>
```

```bash
stackit postgresflex user list --instance-id <INSTANCE_ID>
```

```bash
stackit postgresflex user update <USER_ID> --instance-id <INSTANCE_ID> --role "login,createdb"``
```

