from faker import Faker

fake = Faker()


class StellarBurgerTestData:
    FAKE_USER = {"email": fake.email(),
                 "password": fake.password(),
                 "name": fake.user_name()
                 }

    REAL_USER = {"email": "aarafff1192@ggmail.com",
                 "password": fake.password(),
                 "name": fake.user_name()
                 }

    ORDER_DATA = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6c"]
    }

    ORDER_DATA_WITHOUT_ING = {
        "ingredients": []
    }

    ORDER_DATA_WITH_WRONG_HASH = {
"ingredients": ["61c0c5a71d1f82001bda342332","61c0c5a71d1f82001bda342134"]
}
