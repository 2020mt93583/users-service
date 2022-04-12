from fastapi import FastAPI
from redis_om import get_redis_connection, HashModel

app = FastAPI()

redis = get_redis_connection(
    host="localhost",
    port=6379,
    password="eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81",
    decode_responses=True
)


class User(HashModel):
    name: str
    address: str

    class Meta:
        database = redis


def create_default_users():
    for pk in User.all_pks():
        if User.get(pk):
            print("Default users already exist")
            return
    for i in range(0, 5):
        user = User(
            name="testUser" + str(i),
            address="testAddress" + str(i)
        )
        user.save()
    print("Default users created")


create_default_users()


@app.post('/users/add')
def create(user: User):
    return user.save()


@app.get('/users/{pk}')
def get(pk: str):
    return User.get(pk)


@app.delete('/users/{pk}')
def delete(pk: str):
    return User.delete(pk)
