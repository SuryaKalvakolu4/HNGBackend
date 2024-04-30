from challenges.models import Challenge

def create_test_challenge():
    return Challenge.objects.create(
        day = "Day 1",
        quote = "Test quote",
        author_name = "Test name",
        video_link = "test_video_link.com"
    )