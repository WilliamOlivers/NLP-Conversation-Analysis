import cohere

# initialize Cohere client
co = cohere.Client("YOUR API KEY")

conversation = " Senior Dev: Hey, have you seen the latest pull request for the authentication module? Junior Dev: No, not yet. What’s in it? Senior Dev: They’ve added support for JWT tokens, so we can use that instead of session cookies for authentication. Junior Dev: Oh, that’s great. I’ve been wanting to switch to JWT for a while now. Senior Dev: Yeah, it’s definitely more secure and scalable. I’ve reviewed the code and it looks good, so go ahead and merge it if you’re comfortable with it. Junior Dev: Will do, thanks for the heads-up!"

response = co.summarize(conversation, model = 'summarize-xlarge', length = 'short', extractiveness = 'high', temperature = 0.5,)

summary = response.summary

print(summary)
