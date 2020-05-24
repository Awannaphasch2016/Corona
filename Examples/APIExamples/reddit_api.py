import pickle

import praw
import os

reddit = praw.Reddit(client_id='SxUkZZF8-aFt9A',
                     client_secret='LsbR2v3Td_vvg_KvlTL7XWnQRgA',
                     user_agent='Corona',
                     username='terngoodod',
                     password='Terng2258')

# print(reddit.read_only)

subreddits = reddit.subreddit("Corona")

print(subreddits.display_name)
print(subreddits.title)
print(subreddits.description)

# get 10 hot posts from the MachineLearning subreddit
import time
s = time.time()
for i, submissions in enumerate(subreddits.hot(limit=1)):
    # print(submission.comments.list())

# Creating an App
    # print(vars(submission))
    # for d in vars(submission):
    #     print(d)
    # for j in vars(submission.comments.list()[0] ):
    #     print(j)
    # print(type(submission.comments.list()[0]))
    # print(submission.comments.replace_more())
    print(submissions.comments)
f = time.time()
print(f - s)

# random_submission = reddit.submission(url='https://www.reddit.com/r/blog/comments/d14xg/everyone_on_team_reddit_would_like_to_raise_a/')
# random_submission = reddit.submission(url='https://www.reddit.com/r/redditdev/comments/16s64a/praw_more_comments/')
random_submission = reddit.submission(
    url='https://www.reddit.com/r/blog/comments/d14xg/everyone_on_team_reddit_would_like_to_raise_a/?limit=500')
# print(len(random_submission.comments))
# print( [type(i) for i in random_submission.comments[-5:]])
# print(len( random_submission.comments[-1].comments()))
# print(len(random_submission.comments))
# print(len(random_submission.comments.replace_more()))
# print(len(random_submission.comments))
# print([i.id for i in random_submission.comments.replace_more()])
from praw.models import MoreComments

for i in random_submission.comments:
    if isinstance(i, MoreComments):
        print(i)

# ---Comment Extraction and Parsing tutorial
import praw
reddit = praw.Reddit(client_id='SxUkZZF8-aFt9A',
                     client_secret='LsbR2v3Td_vvg_KvlTL7XWnQRgA',
                     user_agent='Corona',
                     username='terngoodod',
                     password='Terng2258')
url = "https://www.reddit.com/r/funny/comments/3g1jfi/buttons/"
submissions = reddit.submission(url=url)
print(f'number of submission.num_comments = {submissions.num_comments}')
submissions.comments.replace_more(limit=None)
for top_level_comment in submissions.comments.list():
    print(top_level_comment.body)

#=====================
#==create save file function for subreddit crawled data
#=====================
def save2file(file_name, dict_val, verbose):
    assert isinstance(file_name, str), f'file_name must have type = str '
    assert isinstance(dict_val, dict), f'val must have type = dickt '
    path = f'C:\\Users\\Anak\\PycharmProjects\\Corona\\Data\\Reddit\\'
    save_file = path + file_name
    #create directory if not alreayd exist
    os.makedirs(path, exist_ok=True)
    with open(save_file, 'wb') as f:
        pickle.dump(dict_val, f)
    if verbose:
        print(f'save file at {save_file}')

#=====================
#==attempt to get content (subreddit/submission/comments)
#=====================
# from the following subreddit
# General: Corona, COVID-19, CoronavirusUS
# Region: CoronavirusMidwest, CoronavirusSouth, CoronavirusSouthEast, CoronavirusWest
import praw
from tqdm import tqdm
channels = None
reddit = praw.Reddit(client_id='SxUkZZF8-aFt9A',
                     client_secret='LsbR2v3Td_vvg_KvlTL7XWnQRgA',
                     user_agent='Corona',
                     username='terngoodod',
                     password='Terng2258')
assert channels is not None, 'please select channels to apply reddit api'
sum = 0
for c in channels:
    comment_per_channel = {}
    subreddit = reddit.subreddit(c)
    submissions = list(subreddit.hot(limit=None))
    for submission in tqdm(submissions):
        submission.comments.replace_more(limit=None)
        all_submissions_comments = submission.comments.list()
        # print(len(all_submissions_comments))
        sum += len(all_submissions_comments)
        submission_id = submission.id
        for comment in all_submissions_comments:
            for attr in dir(comment):
                attr_val_dict = {attr: comment.__getattribute__(attr)}
                assert 'submission_id' not in comment_per_channel, 'dubplicate key id is found'
                comment_per_channel.setdefault(submission_id, {}).update(attr_val_dict)
    save2file(c, comment_per_channel, verbose=True)


#=====================
#==List of target subreddits
#=====================

#--------List of general Corona subreddits
general_reddit = ['Corona', 'COVID19']

#--------List of region Corona Subreddits
region_reddit = ['CoronavirusUS', 'CoronavirusMidwest',
            'CoronavirusSouth', 'CoronavirusSouthEast', 'CoronavirusWest']

#--------List of USA States
states_subreddit=['alabama','alaska','arizona','arkansas','california','colorado','connecticut','delaware','florida','georgia','hawaii','idaho',
                  'illinois','indiana','iowa','kansas','kentucky','louisiana','maine','maryland','massachusetts','michigan','minnesota','mississippi',
                  'missouri','montana','nebraska','nevada','newhampshire','newjersey','newmexico','newyork','northcarolina','northdakota','ohio',
                  'oklahoma','oregon','pennsylvania','rhodeisland','southcarolina','southdakota','tennessee','texas','utah','vermont','virginia',
                  'washington','westvirginia','wisconsin','wyoming']

#=====================
#==pause python console and start debugging mode
#=====================
import pdb
pdb.set_trace()

# save as pickle files so it is easy to convert to PyTables
# TODO save file in Data/Reddit/subredditname.csv

