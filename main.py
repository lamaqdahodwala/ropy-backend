from sanic import Sanic
import ro_py
from sanic.response import json, html
client = ro_py.Client()

app = Sanic('app')

@app.route('/person/<username>')
async def data_from_username(req, username):
    try:
        data = await client.get_user_by_username(username)
    except Exception:
        return json({'error': 'user does not exist'}, status=404)
    status = await data.get_status()
    friend_count = await data.get_friends_count()
    followers_count = await data.get_followers_count()
    following_count = await data.get_followings_count()
    friends = await data.get_friends()
    id = data.id
    name = data.display_name
    banned = data.is_banned
    created = data.created
    friend_names = []
    for i in friends:
        friend_names.append(i.display_name)
    return json({
        'id': id,
        'name': name,
        'banned': banned,
        'status': status,
        'created': str(created),
        'friend_count': friend_count,
        'followers_count': followers_count,
        'following_count': following_count,
        'friend_names': friend_names
    }, status=200)


@app.route('/person/id/<id>')
async def data_from_user_id(req, id: int):
    try:
        data = await client.get_user(id)
    except Exception:
        return json({'error': 'user does not exist'}, status=404)
    url= data.profile_url
    status = await data.get_status()
    friend_count = await data.get_friends_count()
    followers_count = await data.get_followers_count()
    following_count = await data.get_followings_count()
    friends = await data.get_friends()
    id = data.id
    name = data.display_name
    banned = data.is_banned
    created = data.created
    friend_names = []
    for i in friends:
        friend_names.append(i.display_name)
    return json({
        'id': id,
        'name': name,
        'banned': banned,
        'status': status,
        'created': str(created),
        'friend_count': friend_count,
        'followers_count': followers_count,
        'following_count': following_count,
        'friend_names': friend_names,
        'url': url
    }, status=200)


@app.route('/')
async def home(req):
    return  html('<h1>Hello world </h1>')
app.run()