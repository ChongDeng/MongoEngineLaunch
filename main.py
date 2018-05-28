from mongoengine import *

from models import User, TextPost, LinkPost

connect('Scuter')

def create_user_doc():
    ross = User(email='ross@example.com', first_name='Ross', last_name='Lawley').save()

def create_user_doc2():
    ross = User(email='ross@example.com')
    ross.first_name = 'Ross'
    ross.last_name = 'Lawley'
    ross.save()

def create_post_by_user():
    john = User(email='john@example.com')
    john.first_name = 'john'
    john.last_name = 'Lawley'
    john.save()

    post1 = TextPost(title='Fun with MongoEngine', author=john)
    post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
    post1.tags = ['mongodb', 'mongoengine']
    post1.save()

    post2 = LinkPost(title='MongoEngine Documentation', author=john)
    post2.link_url = 'http://docs.mongoengine.com/'
    post2.tags = ['mongoengine']
    post2.save() 

def main():
    # create_user_doc()
    # create_user_doc2()
    create_post_by_user()
if __name__ == '__main__':
    main()