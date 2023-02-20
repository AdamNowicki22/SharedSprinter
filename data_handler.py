import database_common

# STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']
# (title, user_story, acceptance_criteria, business_value)

@database_common.connection_handler
def get_all_user_stories(cursor):
    query = 'SELECT*FROM sprinter ORDER BY id'
    cursor.execute(query)
    desc = cursor.description
    column_names = [col[0] for col in desc]
    return [dict(zip(column_names, row)) for row in cursor.fetchall()]
    #returns list of dictionaries with sql columns as keys

@database_common.connection_handler
def get_user_story(cursor, id):
    query = 'SELECT*FROM sprinter WHERE id=%s'%(id)
    cursor.execute(query)
    return (cursor.fetchone())

@database_common.connection_handler
def add_story(cursor, title, user_story, acceptance_criteria, business_value,estimation):
    cursor.execute('INSERT INTO sprinter (title, user_story, acceptance_criteria, business_value,estimation) VALUES  (%s, %s, %s, %s, %s)',
    (title, user_story, acceptance_criteria, business_value,estimation))
    database_common.open_database().commit()

@database_common.connection_handler
def edit_story(cursor, id, title, user_story, acceptance_criteria, business_value, estimation, status):
    cursor.execute("""UPDATE sprinter
    SET title = %(new_title)s,
    user_story = %(new_user_story)s,
    acceptance_criteria = %(new_acceptance_criteria)s,
    business_value= %(new_business_value)s,
    estimation = %(new_estimation)s,
    status= %(new_status)s
    WHERE id=%(id)s""",
    {'new_title' : title,
    'new_user_story': user_story,
    'new_acceptance_criteria':acceptance_criteria,
    'new_business_value':int(business_value),
    'new_estimation':int(estimation),
    'new_status':status,
    'id':int(id)})