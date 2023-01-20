from django.db import models

class company(models.Model):
    company_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=55)
    location = models.CharField(max_length=255)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT','IT'),
                                                    ('Non IT', 'Non IT'),
                                                    ('Mobile Phones','Mobile Phones')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    emp_id=models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=155)
    email=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=20, choices=(
                                            ('Manager','Manager'),
                                            ('Software Dev','Software Dev'),
                                            ('HR','HR')
                                            ))
    c_id=models.ForeignKey(company, on_delete=models.CASCADE)

    
    