from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from time import sleep


class SheduledPost:
    def __init__(self, message: str, timestamp: datetime):
        self.message = message
        self.timestamp = timestamp

    def __str__(self):
        return f"\nAt {self.timestamp}\n{self.message}"


class SocialChannel(ABC):
    @property
    @abstractmethod
    def channel_name(self):
        """Represents the type of chanel"""

    @property
    @abstractmethod
    def amount_of_followers(self):
        """Represents amount of folowers this channel"""

    @abstractmethod
    def post_a_message(self, message: str) -> None:
        """Post a message in social the chanel"""


class Youtube(SocialChannel):
    def __init__(self, folowers_amount: int):
        self.amount_of_followers = folowers_amount

    @property
    def channel_name(self):
        return "Youtube"

    @property
    def amount_of_followers(self):
        return getattr(self, "_amount_of_followers")

    @amount_of_followers.setter
    def amount_of_followers(self, value: int):
        setattr(self, "_amount_of_followers", value)

    def post_a_message(self, message: str) -> None:
        print(
            f"🔥 At {datetime.now()} on {self.channel_name} posted next message:\n{message}"
        )

    def __str__(self) -> str:
        return f"{self.channel_name} amount of followers: {self.amount_of_followers}"


class Facebook(SocialChannel):
    def __init__(self, folowers_amount: int):
        self.amount_of_followers = folowers_amount

    @property
    def channel_name(self):
        return "Facebook"

    @property
    def amount_of_followers(self):
        return getattr(self, "_amount_of_followers")

    @amount_of_followers.setter
    def amount_of_followers(self, value: int):
        setattr(self, "_amount_of_followers", value)

    def post_a_message(self, message: str) -> None:
        print(
            f"👍 At {datetime.now()} on {self.channel_name} posted next message:\n{message}"
        )

    def __str__(self) -> str:
        return f"{self.channel_name} amount of followers: {self.amount_of_followers}"


class Twitter(SocialChannel):
    def __init__(self, folowers_amount: int):
        self.amount_of_followers = folowers_amount

    @property
    def channel_name(self):
        return "Twitter"

    @property
    def amount_of_followers(self):
        return getattr(self, "_amount_of_followers")

    @amount_of_followers.setter
    def amount_of_followers(self, value: int):
        setattr(self, "_amount_of_followers", value)

    def post_a_message(self, message: str) -> None:
        print(
            f"✔ At {datetime.now()} on {self.channel_name} posted next message:\n{message}"
        )

    def __str__(self) -> str:
        return f"{self.channel_name} amount of followers: {self.amount_of_followers}"


def shift_time(start_time: datetime, miliseconds: int) -> datetime:
    delta = timedelta(milliseconds=miliseconds)
    end_time = start_time + delta
    return end_time


def process_schedule(
    sheduled_posts: list[SheduledPost], social_channels: list[SocialChannel]
) -> None:
    posts = [post for post in sheduled_posts]
    counter = 0
    while len(posts) > 0:
        counter += 1
        print(f"Cycle: {counter}")
        now = datetime.now()
        i = 0
        while i < len(posts):
            post = posts[i]
            if post.timestamp <= now:
                for channel in social_channels:
                    channel.post_a_message(post.message)
                posts.pop(i)
            else:
                i += 1
        sleep(1)


def main():
    now = datetime.now()

    social_channels = [Twitter(1000), Youtube(2000), Facebook(1500)]
    for channel in social_channels:
        print(channel)

    sheduled_posts: list[SheduledPost] = [
        SheduledPost("Message 01", shift_time(now, 3000)),
        SheduledPost("Message 02", shift_time(now, 6000)),
        SheduledPost("Message 03", shift_time(now, 9000)),
    ]

    for post in sheduled_posts:
        print(post)

    process_schedule(sheduled_posts, social_channels)


if __name__ == "__main__":
    main()
