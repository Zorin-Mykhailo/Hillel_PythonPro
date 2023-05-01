from abc import ABC, abstractmethod, abstractproperty
from ctypes import FormatError
from dataclasses import dataclass
from datetime import datetime



class SheduledPost:
    def __init__(self, message: str, timestamp: datetime):
        self.message = message
        self.timestamp = timestamp


class SocialChannel(ABC):
    @abstractproperty
    def chanel_type(): str

    @abstractproperty
    def amount_of_followerrs(): int

    @abstractmethod
    def post_a_message(message: str): None
    """Post a message in social the chanel"""


class Youtube(SocialChannel):
    ...


class Facebook(SocialChannel):
    ...


class Twitter(SocialChannel):
    ...



def process_schedule(sheduled_posts: list[SheduledPost], social_channels: list[SocialChannel]) -> None:
    for sheduled_post in sheduled_posts:
        message, timestamp = sheduled_post
        for channel in social_channels:
            if timestamp < time():
                channel.post_a_message(message)


def main():
    print("Homework 07")

    social_channels = [Youtube(), Facebook(), Twitter()]
    sheduled_posts: list[SheduledPost] = [
        SheduledPost("Message 01", datetime(2023, 5, 10, 10, 20)),
        SheduledPost("Message 02", datetime(2023, 5, 10, 10, 30)),
        SheduledPost("Message 03", datetime(2023, 5, 10, 10, 30))
        ]
    
    for post in sheduled_posts:
        print(f"{post.message=} {post.timestamp=}")


    ...

if __name__ == "__main__":
    main()
    