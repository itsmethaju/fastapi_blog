# sql_queries.py



def create_table(table, url, desc, title):
    create_query = f'''
    CREATE TABLE IF NOT EXISTS {table} (
        id SERIAL PRIMARY KEY,
        {url} VARCHAR(255) NOT NULL,
        {desc} TEXT,
        {title} VARCHAR(255)
    )
    '''
    return create_query


CREATE_WORK_TABLE = '''
CREATE TABLE IF NOT EXISTS work (
    id SERIAL PRIMARY KEY,
    image_url VARCHAR(255) NOT NULL,
    description TEXT,
    title VARCHAR(255)
)
'''

CREATE_TEAM_TABLE = '''
CREATE TABLE IF NOT EXISTS team (
    id SERIAL PRIMARY KEY,
    image_url VARCHAR(255) NOT NULL,
    description TEXT,
    title VARCHAR(255)
)
'''

DELETE_VIDEO_BY_ID = '''
DELETE FROM blog
WHERE id = %s
'''

DELETE_WORK_BY_ID = '''
DELETE FROM work
WHERE id = %s
'''

DELETE_TEAM_MEMBER_BY_ID = '''
DELETE FROM team
WHERE id = %s
'''


create_table_query = '''
CREATE TABLE IF NOT EXISTS team (
    id SERIAL PRIMARY KEY,
    img_url VARCHAR(255) NOT NULL,
    description TEXT,
    title VARCHAR(255)
)
'''
# Execute the SQL query to create the table
# cursor.execute(create_table_query)