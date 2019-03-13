# import libraries
import pandas as pd
import praw
import csv
from psaw import PushshiftAPI

api = PushshiftAPI()

# Set up Reddit instance

# Import credentials
# Put this in our database_exists
import os
os.chdir("/Users/katelyons/Documents/Reddit")
from reddit import client_id, client_secret, user_agent

reddit = praw.Reddit(client_id = client_id,
                     client_secret = client_secret,
                     user_agent = user_agent)


print(reddit.read_only)  # Output: True


submission = reddit.submission(url='https://www.reddit.com/r/funny/comments/3g1jfi/buttons/')


for top_level_comment in submission.comments:
    print(top_level_comment.body)


submission = reddit.submission(url='https://www.reddit.com/r/childfree/comments/awi5vj/the_real_cause_of_the_wage_gap/')


# Iterate through all comments - help from here: https://praw.readthedocs.io/en/latest/tutorials/comments.html#extracting-comments
submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    print(comment.body)

# Access stuff in the tree
submission.comments.list()[1].replies[1].body

# I guess, write a loop to get all you can out of these comment trees
len(submission.comments.list())

# Get sub comments
len(submission.comments.list()[2].replies)

# Get more sub comments?
len(submission.comments.list()[2].replies[3].replies)

submission.comments.list()[2].replies[3].replies[0].replies[0].body

submission.comments.list()[2].replies[3].replies[0].replies[1].id

len(submission.comments.list()[2].replies[3].replies[0].replies[0].replies[0].replies)

# So what you'd do is just keep tacking on replies until you get 0.
# We want a RECURSIVE function that will keep calling itself until we get len of .replies 0
# What would be the best format for this?
# Each row is a comment, column 1 is comment, column 2 is parent comment id, column 3 is next layer parent id,
# then column 4 next parent level id, onwards to the actual comment id

# Then you could do something like filter on a column to just get a comment, or a thread of comments.
# They'd be in order too, because we'll traverse it step by step
my_lsit = [0,1,2]
x = 5
if x in my_lsit:
    print('Already there')
else:
    print('Not there')

# Start with a smaller thread so it's easier to visualize?
submission = reddit.submission(url='https://www.reddit.com/r/opera/comments/awqd0c/starting_to_read_about_the_history_of_opera_and/')

# Number of parent comments you want to go through
len(submission.comments)

main_comments = len(submission.comments)
for i, comment in enumerate(submission.comments):
    print (comment.parent_id)

# def get_all_commentsdf(submission):
submission.comments.replace_more(limit=None)
comment_id = []
text = []
parent_id = []
is_reply = []
for comment in submission.comments.list():
    comment_id.append(comment)
    text.append(comment.body)
    adj_id = comment.parent_id.split("_",1)[1]
    parent_id.append(adj_id)
    if adj_id in comment_id:
        is_reply.append(True)
    else:
        is_reply.append(False)

data = pd.DataFrame({'text': text,
                       'comment_id': comment_id,
                       'parent_id': parent_id,
                       'is_reply': is_reply})

data.sort_values(by=['parent_id','comment_id'])

data.comment_id = data.comment_id.astype('str')
data.info()
data.to_csv('the_real_cause_of_the_wage_gap.csv', sep = ',')

# Get all replies for one comment
submission.comments.list()[0].replies[0].replies[0].body
x = submission.comments.list()[0].replies[0]
while len(x.replies) > 0:
    print(x.body)
submission.comments.list()[0]

    main_comments = len(submission.comments)
    for i in
    text = []
    comment_id = []
    for i, comment in enumerate(submission.comments.list()):
        if len(comment.replies) < 1:
            parent1id.append(comment.id)
            text.append(comment.body)
        else:
            continue
        # parent1id.append(comment.id)
        # text.append(comment.body)
        # get_allcommentsdf(submission)

parent1id
    # print(len(comment.replies))


# What we want to do: just keep going through until we have all subcomments. I think the best thing would
# be to create a list for each comment level, and then turn those into lists...
# Or do like, slowly read each thing into a csv, each row a comment, and then have a column of whether or not
# it's nested and then a column of the parent comment id. It would be in sequential order hopefully from the way we've
# scraped

# Found a (potential) solution HERE: https://pythonprogramming.net/parsing-comments-python-reddit-api-wrapper-praw-tutorial/
# conversedict = {}
# hot_python = subreddit.hot(limit=3)
# for submission in hot_python:
    # if not submission.stickied:
conversedict = {}
print('Title: {}, upvotes: {}, downvotes: {}, subid: {}'.format(submission.title,
                                                                                      submission.ups,
                                                                                      submission.downs,
                                                                                      submission.id))
submission.comments.replace_more(limit=0)
for comment in submission.comments.list():
    if comment.id not in conversedict:
        conversedict[comment.id] = [comment.body,{}]
        if comment.parent() != submission.id:
            parent = str(comment.parent())
            conversedict[parent][1][comment.id] = [comment.ups, comment.body]

for post_id in conversedict:
    message = conversedict[post_id][0]
    replies = conversedict[post_id][1]
    if len(replies) > 1:
        print(35*'_')
        print('Original Message: {}'.format(message))

        print('Replies:')
        for reply in replies:
            print('--')
            print(replies[reply][1][:200]) # again, limiting to 200 characters for space-saving, not necessary
___________________________________

conversedict["ehob98d"]
for x in conversedict:
    print(x)


redditWriter = csv.writer(open('the_real_cause_of_the_wage_gap.csv', 'w'), delimiter=',')

for comment in submission.comments.list():
    redditWriter.writerow([comment.body.encode('ascii', 'ignore').decode('ascii')])

# Current problem is CSV is weird, doesn't match up one comment per row
# Also want to check for responses to comments, sub comments

# Another method
def process_comments(objects):
    for object in objects:
        if type(object).__name__ == "Comment":
            process_comments(object.replies) # Get replies of comment

            # Do stuff with comment (object)

        elif type(object).__name__ == "MoreComments":
            process_comments(object.comments())

thread = 'https://www.reddit.com/r/childfree/comments/awi5vj/the_real_cause_of_the_wage_gap/'

submission = reddit.submission(thread)
process_comments(submission.comments)


# Try pushshift for more comments?
