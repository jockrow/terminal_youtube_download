from instaloader import Instaloader, Profile
# https://instaloader.github.io

PROFILE = "cultural_alfabeta"
L = Instaloader()
profile = Profile.from_username(L.context, PROFILE)

print("followees:" + str(profile.followees))
print("followers:" + str(profile.followers))

print("Fetching followers of profile {}.".format(profile.username))
followers = set(profile.get_followers())
print("follower:" + follower[0])
