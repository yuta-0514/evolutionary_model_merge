def score_mgsm_binary(pred, question, answer_number, answer) -> bool:
    if "." in pred:
        pred = pred.rstrip("0").rstrip(".")
    pred = pred.replace(",", "")
    if str(answer_number) == pred:
        return 1
    else:
        return 0

def score_mgsm(pred, question, answer_number, answer):
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

def process_results(doc, results):
    score = score_mgsm_binary(results[0], doc["question"], doc["answer_number"], doc["answer"])
    return {"acc": score}
