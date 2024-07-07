def build_prompt(question):
    template = [
        {"role": "user", "content": f"Question:{question}"},
        {"role": "user", "content": "Answer:"},
    ]
    return template
 
# プロンプトの生成
def generate_prompt(doc):
    prompt = build_prompt(doc["question"])
    return prompt

# 評価
def evaluate(pred, question, answer_number, answer):
    pred = pred.replace(".", "")
    try:
        if int(pred) == answer_number:
            return 1.
        else:
            error = abs(int(pred)-answer_number)/answer_number
            if error > 1:
                return 0.
            else:
                return 1 - error
    except ValueError:
        return 0.

# スコアの計算
def process_results(doc, results):
    score = evaluate(results[0], doc["question"], doc["answer_number"], doc["answer"])
    return {"acc": score}
