import requests
import json
def get_response(action):
    prompt = "Predict common sense results of the following actions.\n--\nAction: I didn't water the plant for 3 weeks.\nResult: The plant died.\n--\nAction: I went to school.\nResult: I got a diploma.\n--\nAction: I left the AC on all day.\nResult: I got a high utility bill.\n--\nAction: I helped my neighbors when their car broke down.\nResult: My neighbors were grateful.\n--\nAction: I put the ice cream outside for an hour.\nResult: It got soft and melted.\n--\nAction: " + action
    response = requests.post("https://api.ai21.com/studio/v1/j1-jumbo/complete",
        headers={"Authorization": "Bearer a8HDpmAX8rM9r0AA8vHeRnFTvoq0ZOsw"},
        json={
            "prompt": prompt,
            "numResults": 1,
            "maxTokens": 40,
            "temperature": 0.0,
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

def fishing():
    result = get_response("I go fishing")
    print(result)
    return

def sleep():
    result = get_response("I go to sleep")
    print(result)
    return

def plant_potatoes():
    result = get_response("I plant potatoes")
    print(result)
    return

def fight_wolf():
    result = get_response("I fight wolf")
    print(result)
    return

def play_rabbit():
    result = get_response("I go to play with rabbit")
    print(result)
    return
def main():
    play_rabbit()

if __name__ == "__main__":
    main()

