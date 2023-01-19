import requests
import json
def get_response(action):
    prompt = "Predict common sense results of the following actions.\n--\nAction: I didn't water the plant for 3 weeks.\nResult: The plant died.\n--\nAction: I went to school.\nResult: I got a diploma.\n--\nAction: I left the AC on all day.\nResult: I got a high utility bill.\n--\nAction: I helped my neighbors when their car broke down.\nResult: My neighbors were grateful.\n--\nAction: I put the ice cream outside for an hour.\nResult: It got soft and melted.\n--\nAction: " + action
    response = requests.post("https://api.ai21.com/studio/v1/j1-jumbo/complete",
        headers={"Authorization": "Bearer a8HDpmAX8rM9r0AA8vHeRnFTvoq0ZOsw"},
        json={
            "prompt": prompt,
            "numResults": 1,
            "maxTokens": 20,
            "temperature": 0.8,
            "topKReturn": 0,
            "topP":0.98,
            "countPenalty": {
                "scale": 0,
                "applyToNumbers": False,
                "applyToPunctuations": False,
                "applyToStopwords": False,
                "applyToWhitespaces": False,
                "applyToEmojis": False
            },
            "frequencyPenalty": {
                "scale": 0,
                "applyToNumbers": False,
                "applyToPunctuations": False,
                "applyToStopwords": False,
                "applyToWhitespaces": False,
                "applyToEmojis": False
            },
            "presencePenalty": {
                "scale": 0,
                "applyToNumbers": False,
                "applyToPunctuations": False,
                "applyToStopwords": False,
                "applyToWhitespaces": False,
                "applyToEmojis": False
        },
        "stopSequences":["--"]
        }
    )
    response = json.loads(response.content.decode('utf-8'))
    return response['completions'][0]['data']['text']

print(get_response("I give money to poor people"))