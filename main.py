from mongoengine import *

from models import User, TextPost, LinkPost, Post

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

def access_data():
    for post in Post.objects:
        print("post title: ", post.title)

def access_data2():
    for post in TextPost.objects:
        print("content: ", post.content)

    print("=======================")

    for post in Post.objects:
        print(post.title)
        print('*' * len(post.title))

        if isinstance(post, TextPost):
            print(post.content)

        if isinstance(post, LinkPost):
            print('Link: {}'.format(post.link_url))

def access_data3():
    for user in User.objects:
        print("user: ", user.email)

        print('*' * len(user.email))

    print('=' * 40)

    for user in User.objects(email='ross@example.com'):
        print("name: ", user.first_name)


def update_data():
    for post in LinkPost.objects(title='MongoEngine Documentation'):
        post.title = 'MongoEngine Documentation new'
        post.save()

def main():
    # create_user_doc()
    # create_user_doc2()
    # create_post_by_user()
    # access_data()
    # access_data2()
    # access_data3()
    update_data()

if __name__ == '__main__':
    main()