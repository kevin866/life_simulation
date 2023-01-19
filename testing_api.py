import ai21
ai21.api_key = 'a8HDpmAX8rM9r0AA8vHeRnFTvoq0ZOsw'
def get_response(action):
    prompt = "Predict common sense results of the following actions.\n--\nAction: I didn't water the plant for 3 weeks.\nResult: The plant died.\n--\nAction: I went to school.\nResult: I got a diploma.\n--\nAction: I left the AC on all day.\nResult: I got a high utility bill.\n--\nAction: I helped my neighbors when their car broke down.\nResult: My neighbors were grateful.\n--\nAction: I put the ice cream outside for an hour.\nResult: It got soft and melted.\n--\nAction: " + action
    response = ai21.Completion.execute(model='j1-jumbo', prompt=prompt, maxTokens=20)
    return response.completions[0]['data'].text

print(get_response("I go to college"))
print(get_response("I studied computer science"))
print(get_response("I played football in college"))