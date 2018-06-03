import requests
import json

def send_request(product_name, product_price, sentiment, keywords, emotion):
    # FeedBack
    # POST http://localhost:8000/demo/feedback
    try:
        response = requests.post(
            url="http://localhost:8000/demo/feedback",
            headers={
                "Content-Type": "application/json; charset=utf-8",
            },
            data=json.dumps({
                "product_name": product_name,
                "product_price": product_price,
                "sentiment": sentiment,
                "keywords": keywords,
                "emotion": emotion
            })
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')