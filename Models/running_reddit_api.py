import os
import praw
from tqdm import tqdm
import pickle


def save2file(file_name, dict_val, verbose):
    assert isinstance(file_name, str), f'file_name must have type = str '
    assert isinstance(dict_val, dict), f'val must have type = dickt '
    path = f'C:\\Users\\Anak\\PycharmProjects\\Corona\\Data\\Reddit\\'
    save_file = path + file_name
    # create directory if not alreayd exist
    os.makedirs(path, exist_ok=True)
    with open(save_file, 'wb') as f:
        pickle.dump(dict_val, f)
        if verbose:
            print(f'save file at {f.name}')


# =====================
# ==attempt to get content (subreddit/submission/comments)
# =====================
# from the following subreddit
# General: Corona, COVID-19, CoronavirusUS
# Region: CoronavirusMidwest, CoronavirusSouth, CoronavirusSouthEast, CoronavirusWest
channels = None
reddit = praw.Reddit(client_id='SxUkZZF8-aFt9A',
                     client_secret='LsbR2v3Td_vvg_KvlTL7XWnQRgA',
                     user_agent='Corona',
                     username='terngoodod',
                     password='Terng2258')
# --------List of USA States
# states_subreddit = ['alabama', 'alaska', 'arizona', 'arkansas', 'california',
#                     'colorado', 'connecticut', 'delaware', 'florida', 'georgia',
#                     'hawaii', 'idaho',  'illinois', 'indiana', 'iowa']
states_subreddit = ['kansas', 'kentucky',
                    'louisiana', 'maine', 'maryland', 'massachusetts',
                    'michigan', 'minnesota', 'mississippi',
                    'missouri', 'montana', 'nebraska', 'nevada', 'newhampshire',
                    'newjersey', 'newmexico', 'newyork', 'northcarolina',
                    'northdakota', 'ohio',
                    'oklahoma', 'oregon', 'pennsylvania', 'rhodeisland',
                    'southcarolina', 'southdakota', 'tennessee', 'texas',
                    'utah', 'vermont', 'virginia',
                   'washington', 'westvirginia', 'wisconsin', 'wyoming']
channels = states_subreddit
assert len(channels) > 0, 'please select channels to apply reddit api'
sum = 0
for c in tqdm(channels):
    comment_per_channel = {}
    subreddit = reddit.subreddit(c)
    print(f'running subreddit = {c}..')
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

# =====================
# ==check that saved file are not empty
# =====================
import pickle
file = r'C:\Users\Anak\PycharmProjects\Corona\Data\Reddit\COVID19'
loaded_file = pickle.load(open(file, "rb"))

# save as pickle files so it is easy to convert to PyTables
# TODO save file in Data/Reddit/subredditname.csv
