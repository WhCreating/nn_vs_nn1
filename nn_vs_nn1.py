from g4f.client import Client


class DialogNN():
    def __init__(self, nn1, nn2):
        self.nn1 = nn1
        self.nn2 = nn2

    def dialog(self):
        promtik = "Привет!"

        while True:
            promtik = self.nn_to_promt(self.nn1, promtik)
            print(f"{self.nn1}: {promtik}")
            promtik = self.nn_to_promt(self.nn2, promtik)
            print(f"{self.nn2}: {promtik}")


    def nn_to_promt(self, nn, promt):
        client = Client()
        response = client.chat.completions.create(
            model=nn,
            messages=[{"role": "user", "content": promt}],
            web_search=False
        )

        return response.choices[0].message.content
