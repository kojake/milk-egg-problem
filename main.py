shopping_list = ["milk", "egg"]
specific_product = "egg"
result = ""

def buy_milk(result):
    if specific_product in shopping_list:
        print("牛乳を3つ買ってきた")
    else:
        print("牛乳を買ってきた")

buy_milk(result)