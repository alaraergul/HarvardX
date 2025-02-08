import pytest
import datetime
from project import add_task, update_status, send_reminder, tasks

def test_add_task():
    tasks.clear()
    add_task("Test Task", "This is a test task", datetime.datetime(2024, 9, 30))
    assert len(tasks) == 1
    assert tasks[0]["name"] == "Test Task"
    assert tasks[0]["status"] == "pending"
    assert tasks[0]["due_date"] == datetime.datetime(2024, 9, 30)

def test_update_status():
    tasks.clear()
    add_task("Test Task 2", "This is another test task", datetime.datetime(2024, 10, 1))
    update_status(1, "completed")
    assert tasks[0]["status"] == "completed"

def test_send_reminder(capsys):
    tasks.clear()

    tomorrow = datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=1), datetime.time())
    add_task("Test Task 3", "Reminder test task", tomorrow)
    send_reminder(1)
    captured = capsys.readouterr()
    assert "1 day(s)" in captured.out


    today = datetime.datetime.combine(datetime.date.today(), datetime.time())
    add_task("Today Task", "Task due today", today)
    send_reminder(2)
    captured = capsys.readouterr()
    assert "due today" in captured.out  
