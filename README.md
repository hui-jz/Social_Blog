# Social_Blog
flask 开发的 社交博客应用


# 初始化数据库
```
1.数据配置
项目根目录 config.py 文件中配置数据选项

2.使用 init 子命令添加数据库迁移支持
项目根目录执行  flask db init 命令
(Social_Blog) $ flask db init
 Creating directory /home/flask/flasky/migrations...done
 Creating directory /home/flask/flasky/migrations/versions...done
 Generating /home/flask/flasky/migrations/alembic.ini...done
 Generating /home/flask/flasky/migrations/env.py...done
 Generating /home/flask/flasky/migrations/env.pyc...done
 Generating /home/flask/flasky/migrations/README...done
 Generating /home/flask/flasky/migrations/script.py.mako...done
 Please edit configuration/connection/logging settings in
 '/home/flask/flasky/migrations/alembic.ini' before proceeding.

3. 执行 flask db migrate 命令，自动创建一个迁移脚本。
(Social_Blog) $ flask db migrate -m "initial migration"
INFO [alembic.migration] Context impl SQLiteImpl.
INFO [alembic.migration] Will assume non-transactional DDL.
INFO [alembic.autogenerate] Detected added table 'roles'
INFO [alembic.autogenerate] Detected added table 'users'
INFO [alembic.autogenerate.compare] Detected added index
'ix_users_username' on '['username']'
 Generating /home/flask/flasky/migrations/versions/1bc
 594146bb5_initial_migration.py...done

4.检查自动生成的脚本，根据对模型的实际改动进行调整。
5.把迁移脚本纳入版本控制。

6. 执行 flask db upgrade 命令，把迁移应用到数据库中。
(Social_Blog)$ flask db upgrade
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 9b684698862e, empty message

```