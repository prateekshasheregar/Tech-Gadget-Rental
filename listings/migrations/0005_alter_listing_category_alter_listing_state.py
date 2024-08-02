# Generated by Django 4.2 on 2023-04-09 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0004_alter_listing_category_alter_listing_state"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="category",
            field=models.CharField(
                choices=[
                    ("Jobs", "Jobs"),
                    ("Electronics", "Electronics"),
                    ("Bikes", "Bikes"),
                    ("Furniture", "Furniture"),
                    ("Books&Sports", "Books&Sports"),
                    ("Fashion", "Fashion"),
                    ("Mobiles", "Mobiles"),
                    ("Property", "Property"),
                    ("Cars", "Cars"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="state",
            field=models.CharField(
                choices=[
                    ("NL", "Nagaland"),
                    ("RJ", "Rajasthan"),
                    ("JH", "Jharkhand"),
                    ("AS", "Assam"),
                    ("TS", "Telegana"),
                    ("WB", "West Bengal"),
                    ("KL", "Kerala"),
                    ("TR", "Tripura"),
                    ("MZ", "Mizoram"),
                    ("AR", "Arunachal Pradesh"),
                    ("CG", "Chhattisgarh"),
                    ("MP", "Madhya Pradesh"),
                    ("GJ", "Gujarat"),
                    ("UP", "Uttar Pradesh"),
                    ("GA", "Goa"),
                    ("MN", "Manipur"),
                    ("MH", "Maharashtra"),
                    ("UK", "Uttarakhand"),
                    ("PB", "Punjab"),
                    ("KA", "Karnataka"),
                    ("AP", "Andhra Pradesh"),
                    ("OD", "Odisha"),
                    ("HP", "Haryana"),
                    ("ML", "Meghalaya"),
                    ("BR", "Bihar"),
                    ("TN", "Tamil Nadu"),
                    ("MI", "Sikkim"),
                ],
                max_length=100,
            ),
        ),
    ]
