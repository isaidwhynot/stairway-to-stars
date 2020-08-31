# stairway-to-stars
Automatically login to Bilkent STARS using selenium.

Needs 4 things:

1. Your Bilkent ID
2. Your SRS Password
3. E-mail address that code is sent to
4. That e-mail's password

There is "User configuration" part in the beginning of the script:

```python
# User configuration
STUDENT_ID = "your_id_here" 
SRS_PASSWORD = "srs_password"
MAIL_HANDLE = "your_mail_address_here"
MAIL_PASSWORD = "email_password"
```

If you change these appropriately, you are good to go.. Except the path of `chromedriver.exe` which you can set
with `DRIVER_PATH` variable. Default assumes it's in the same directory with the script.
