﻿# [Homework 07 •  Abstract classes](https://lms.ithillel.ua/groups/63c0179f2482232c29371552/homeworks/64419b161366a9108a6b7365)

You just landed a job ***"SocialHero"***. Their product allows you to schedule posts via the social network.

Unfortunately, the person you are replacing didn't use classes for some reason. So all data structures that are used are tuples.

Here is a code example:

```python
# each social channel has a type and the current number of followers
SocialChannel = tuple[str, int] = 

# each post has a message and the timestamp when it should be posted
Post = tuple[str, int]


def post_a_message(channel: SocialChannel, message: str) -> None:
   type, _ = channel
   if type == "youtube":
     post_to_youtube(channel, message)
   elif type == "facebook":
     post_to_facebook(channel, message)
   elif type == "twitter":
     post_to_twitter(channel, message)


def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
   for post in posts:
     message, timestamp = post
     for channel in channels:
       if timestamp <= time():
         post_a_message(channel, message)
```


**Acceptance criteria:**

- [x] **Classes** should be used instead of **tuples** to represent social channels and posts. As a starting point, use the code download for this exercise.
- [x] The `post_a_message` function is improved. The `if-statement` has to check for each different type of social network and then call a different method. 
If you want to add support for a new social network, you'll need to add an extra `elif` part, making the code harder and harder to read.
- [x] A new version of the code uses abstraction to solve the problem.