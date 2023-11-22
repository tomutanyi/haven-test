from faker import Faker
import random
from random import choice as rc
from app import app
from models import db, User, GameEntry, GameGenre, GameReview, Genre

fake = Faker()

with app.app_context():
    # Begin with deleting existing data
    User.query.delete()
    GameEntry.query.delete()
    GameGenre.query.delete()
    GameReview.query.delete()
    Genre.query.delete()


    users = []

    for _ in range(20):
        user = User(
            username=fake.user_name(),
            email = fake.email()
        )
        users.append(user)

    db.session.add_all(users)

    # Genres
    game_genres = [
        "Action RPG",
        "Social Deduction",
        "Life Simulation",
        "Battle Royale",
        "Sandbox",
        "First-Person Shooter",
        "Augmented Reality",
        "Action-Adventure",
        "Open World",
        "Multiplayer Online Battle Arena (MOBA)"
    ]

    genres = []

    for _ in range(10):
        genre = Genre(
            name=rc(game_genres)
        )
        genres.append(genre)

    db.session.add_all(genres)


    # List of 10 game titles
    game_titles = [
        "The Witcher 3: Wild Hunt", 
        "Among Us",
        "Animal Crossing: New Horizons",
        "Fortnite",
        "Minecraft",
        "Call of Duty: Warzone",
        "Pokémon Go",
        "Grand Theft Auto V",
        "Cyberpunk 2077",
        "League of Legends"
    ]

    # List of corresponding platforms
    game_platforms = [
        "Mobile", "Desktop","PlayStation","Nintendo Switch",
        ]
    
    game_entries = []

    image_urls = [
    "https://i.pinimg.com/474x/1a/12/d0/1a12d079dae8a8fd2ac0387d0d541894.jpg",
    "https://i.pinimg.com/474x/41/21/a0/4121a08006046b845e1a1b4735fc196e.jpg",
    "https://i.pinimg.com/474x/3b/e1/b9/3be1b96a85580dfeb0e58a222da8455f.jpg",
    "https://i.pinimg.com/474x/87/42/8a/87428a44cf9fe9eafad3244b715b77c5.jpg",
    "https://i.pinimg.com/474x/84/70/18/847018b98a9a83c3995fb36f688eb4a3.jpg",
    "https://i.pinimg.com/474x/c4/f0/1c/c4f01cdd64fdca59eef4adb07ee43974.jpg",
    "https://i.pinimg.com/474x/36/ab/e7/36abe729702dd588196f11ecfdc17eda.jpg",
    "https://i.pinimg.com/474x/b8/2a/3f/b82a3f7b31e990e54600e62df8885c0e.jpg",
    "https://i.pinimg.com/474x/03/7a/88/037a883d8c7e7b0d2af0cdcb85b9a4e8.jpg",
    "https://i.pinimg.com/474x/0e/90/bc/0e90bcedeee6f2d0e0a8b023ccc4a2a0.jpg",
    "https://i.pinimg.com/474x/69/56/91/695691ed8517caabf802834d703c693b.jpg",
    "https://i.pinimg.com/474x/a4/97/ca/a497cafb64197f39c3db42f02f15004b.jpg",
    "https://i.pinimg.com/474x/5b/b8/60/5bb8609b6234aeb72408b6ca54db5cd3.jpg",
    "https://i.pinimg.com/474x/2f/7e/e7/2f7ee73f58715dc4844b049b389e4c36.jpg",
    "https://i.pinimg.com/474x/37/c0/27/37c027a8a043e6cfa8aeeeef3f72de4f.jpg",
    "https://i.pinimg.com/474x/ca/64/d9/ca64d9b14804bad5fbcc407c74c211dd.jpg",
    "https://i.pinimg.com/474x/59/e4/38/59e43801fe0d7fa0d1d8fdbd107222c4.jpg",
    "https://i.pinimg.com/474x/e1/6f/09/e16f09438d701a653d1d5f929cdcdf9c.jpg",
    "https://i.pinimg.com/474x/8d/a9/02/8da902d65bf6f3bfbf39fcd33f942ae3.jpg",
    "https://i.pinimg.com/474x/8f/c0/d0/8fc0d03bc7bd88a5eed45c6e47d1d3cb.jpg",
    "https://i.pinimg.com/474x/b8/25/dc/b825dc4a0028e931aa9efd71c6a91885.jpg",
    "https://i.pinimg.com/474x/64/6b/4f/646b4ff1cdcf0765e7a01ec6d6519f15.jpg",
    "https://i.pinimg.com/474x/52/80/a6/5280a6a6c18a215bd3e089c6cee667e7.jpg",
    "https://i.pinimg.com/474x/e9/ec/82/e9ec82393688528ecce0320ec3eb2a98.jpg",
    "https://i.pinimg.com/474x/05/ef/d4/05efd4033063c14ab85c47e835e39e2a.jpg",
    "https://i.pinimg.com/474x/53/ff/79/53ff794f967bec7b44111323cb33e4ae.jpg"
    ]

    
    for _ in range(20):
        game_entry = GameEntry(
            title=rc(game_titles),
            platform=rc(game_platforms),
            image_url=rc(image_urls),
            description=fake.sentence(15),
            # user=rc(users),
            # genre=rc(genres)
        )

        game_entries.append(game_entry)

    db.session.add_all(game_entries)

    game_reviews = []

    for _ in range(20):
        random_user = rc(users)
        random_game_entry = rc(game_entries)
        
        game_review = GameReview(
            rating = random.randint(0,10),
            comment=fake.sentence(),
            user=rc(users),
            game_entry=rc(game_entries)
        )

        game_reviews.append(game_review)

    db.session.add_all(game_reviews)

    game_genres = []

    for _ in range(20):
        game_genre = GameGenre(
            game_entry=rc(game_entries),
            genre=rc(genres)
        )
        game_genres.append(game_genre)

    db.session.add_all(game_genres)
    db.session.commit()