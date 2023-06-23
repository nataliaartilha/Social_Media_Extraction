import instaloader
import pandas as pd

# Create an instance of the Instaloader class
loader = instaloader.Instaloader()

# Login to Instagram (optional)
loader.context.log("Logging in...")
#loader.load_session_from_file("your_username")

# Get a profile object representing the user you want to extract data from
profile = instaloader.Profile.from_username(loader.context, "fea.dev")

# Create an empty list to store the data
data = []

# Iterate through the user's posts and extract the data
for post in profile.get_posts():
    data.append({
        "shortcode": post.shortcode,
        "caption": post.caption,
        "likes": post.likes,
        "comments": post.comments,
        "timestamp": post.date_utc,
        "owner_username": post.owner_username,
        "owner_id": post.owner_id,
        "video_view_count": post.video_view_count,
        "is_video": post.is_video,
        "location": post.location.name if post.location else None,
        #"tagged_users": [tagged_user.username for tagged_user in post.tagged_users],
        #"tagged_locations": [tagged_loc.name for tagged_loc in post.tagged_locations] if post.tagged_locations else None,
        #"tagged_posts": [tagged_post.shortcode for tagged_post in post.tagged_posts] if post.tagged_posts else None,
        "caption_hashtags": post.caption_hashtags,
        "caption_mentions": post.caption_mentions,
        #"is_ad": post.is_ad,
        #"edge_media_to_caption": post.edge_media_to_caption
    })

# Convert the list of dictionaries to a Pandas dataframe
df = pd.DataFrame(data)

from sqlalchemy import create_engine
engine = create_engine('postgresql://grupo_1:grupinho@database-dev.crlbgka5uijc.sa-east-1.rds.amazonaws.com:5432/grupinho', client_encoding="utf8")

df.to_sql('instagram', engine)
