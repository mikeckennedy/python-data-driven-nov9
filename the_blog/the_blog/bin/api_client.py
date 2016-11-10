import requests

url = 'http://localhost:6543/api/posts'

resp = requests.get(url)

if resp.status_code != 200:
    print("Error contacting service at {}, code {}".format(
        url, resp.status_code
    ))

# print(type(resp.json()), resp.json())
posts = resp.json().get('posts')

for p in posts:
    print("{} -- {}".format(p['id'], p['title']))

ip = input("Select action: [a]dd post, [d]etails of post: ")

if ip == 'd':

    theid = input('Enter post id to see details:')
    while theid:
        url = 'http://localhost:6543/api/posts/' + theid
        resp = requests.get(url)
        # print(resp.json())
        print("Details of {}".format(theid))
        print("Title: " + p['title'])
        print(p)
        # print("Content: " + p['content'])

        theid = input('Enter post id to see details:')

else:
    print('Create a post!')
    title = input("Enter the title: ")
    url = input("Enter the url: ")
    content = input("Enter the content: ")

    data = {
        'title': title,
        'url': url,
        'content': content
    }

    # print("To create: {}".format(data))
    resp = requests.post('http://localhost:6543/api/posts', None, data)
    print(resp.status_code)
    print(resp.text)

    print("Created new post with id {}".format(resp.json().get('id')))
