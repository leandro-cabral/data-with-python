from operator import itemgetter
import requests

# Cria uma chamada de API para obter os IDs das melhores histórias
url_top_stories = "https://hacker-news.firebaseio.com/v0/topstories.json"
r_top_stories = requests.get(url_top_stories)
print(f"Status code: {r_top_stories.status_code}")

# Processa os IDs das melhores histórias
top_story_ids = r_top_stories.json()[:30]

submission_dicts = []
for submission_id in top_story_ids:
    # Cria uma nova chamada de API para obter informações sobre cada contribuição de artigo
    url_submission = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r_submission = requests.get(url_submission)
    print(f"id: {submission_id}\tstatus: {r_submission.status_code}")
    response_dict = r_submission.json()

    # Cria um dicionário para cada artigo
    submission_dict = {
        'title': response_dict.get('title', 'N/A'),
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants', 0),  # Use get with a default value
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
