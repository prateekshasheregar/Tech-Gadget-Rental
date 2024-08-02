# Generated by Django 4.2 on 2023-04-09 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0003_alter_listing_category_alter_listing_state"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="category",
            field=models.CharField(
                choices=[
                    ("Bikes", "Bikes"),
                    ("Property", "Property"),
                    ("Mobiles", "Mobiles"),
                    ("Cars", "Cars"),
                    ("Books&Sports", "Books&Sports"),
                    ("Fashion", "Fashion"),
                    ("Jobs", "Jobs"),
                    ("Furniture", "Furniture"),
                    ("Electronics", "Electronics"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="state",
            field=models.CharField(
                choices=[
                    ("MZ", "Mizoram"),
                    ("TS", "Telegana"),
                    ("HP", "Haryana"),
                    ("WB", "West Bengal"),
                    ("AR", "Arunachal Pradesh"),
                    ("KA", "Karnataka"),
                    ("AP", "Andhra Pradesh"),
                    ("GA", "Goa"),
                    ("BR", "Bihar"),
                    ("RJ", "Rajasthan"),
                    ("TN", "Tamil Nadu"),
                    ("GJ", "Gujarat"),
                    ("UP", "Uttar Pradesh"),
                    ("TR", "Tripura"),
                    ("AS", "Assam"),
                    ("MP", "Madhya Pradesh"),
                    ("PB", "Punjab"),
                    ("ML", "Meghalaya"),
                    ("MI", "Sikkim"),
                    ("OD", "Odisha"),
                    ("UK", "Uttarakhand"),
                    ("MN", "Manipur"),
                    ("NL", "Nagaland"),
                    ("CG", "Chhattisgarh"),
                    ("MH", "Maharashtra"),
                    ("JH", "Jharkhand"),
                    ("KL", "Kerala"),
                ],
                max_length=100,
            ),
        ),
    ]
