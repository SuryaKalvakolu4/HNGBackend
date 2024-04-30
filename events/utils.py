from .models import Event

def create_test_event():
    return Event.objects.create(
        day = "Day 1",
        title = "Test title",
        description = "Test description",
        start_time = "18:00",
        end_time = "18:00",
        date = "2024-10-10",
        link = "test_link.com",
        name = "Test name",
        requirements = "Test requirements",
    )