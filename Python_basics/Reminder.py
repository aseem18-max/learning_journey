from plyer import notification

notification.notify(
    title = "Reminder",
    message = "This is a water reminder",
    app_name = "Gloss",  
    timeout = 10, 
    toast = False
)
