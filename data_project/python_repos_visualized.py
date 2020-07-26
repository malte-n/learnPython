import requests

from plotly.graph_objs import Bar
from plotly import offline


# Make an API and store the response
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store the API response in a dict
response_dict = r.json()
# Process results
repo_dicts = response_dict["items"]
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict["name"]
    repo_url = repo_dict["html_url"]
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict["stargazers_count"])

    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    label = f"{owner}<br />{description}"
    labels.append(label)

# Make visualisations
data = [{"type": "bar", "x": repo_links, "y": stars, "hovertext": labels,}]

my_layout = {
    "title": "Most-Starred Python Projects on GitHub",
    "xaxis": {
        "title": "Repository",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14},
    },
    "yaxis": {
        "title": "# of stars",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14},
    },
}

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="python_repos.html")

print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
