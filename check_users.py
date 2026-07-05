from app import create_app
from app.models.user import User

app = create_app()

with app.app_context():

    users = User.query.all()

    print(f"\nTotal users: {len(users)}\n")

    for user in users:
        print("-------------------------")
        print(f"ID: {user.id}")
        print(f"Name: {user.full_name}")
        print(f"Email: {user.email}")
        print(f"Role: {user.role}")